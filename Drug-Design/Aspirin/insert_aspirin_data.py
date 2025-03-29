import sqlite3

conn = sqlite3.connect("drug_simulation.db")
cursor = conn.cursor()

# Get the aspirin drug_id
cursor.execute("SELECT id FROM drugs WHERE name = ?", ("Aspirin",))
drug_id = cursor.fetchone()[0]

# Insert targets
targets = [
    ("COX-1", "P23219", "3N8Z", -7.3),
    ("COX-2", "P35354", "5IKT", -6.8),
]

for protein_name, uniprot_id, pdb_id, affinity in targets:
    cursor.execute("""
        INSERT INTO targets (drug_id, protein_name, uniprot_id, pdb_id, binding_affinity)
        VALUES (?, ?, ?, ?, ?)
    """, (drug_id, protein_name, uniprot_id, pdb_id, affinity))

# Get target_ids for COX-1 and COX-2
cursor.execute("SELECT id FROM targets WHERE protein_name = 'COX-1'")
cox1_id = cursor.fetchone()[0]

cursor.execute("SELECT id FROM targets WHERE protein_name = 'COX-2'")
cox2_id = cursor.fetchone()[0]

# Insert binding sites
binding_sites = [
    (cox1_id, "Ser530"), (cox1_id, "Tyr385"), (cox1_id, "Arg120"),
    (cox2_id, "Ser516"), (cox2_id, "Tyr371"), (cox2_id, "Arg120"),
]

for target_id, residue in binding_sites:
    cursor.execute("""
        INSERT INTO binding_sites (target_id, residue)
        VALUES (?, ?)
    """, (target_id, residue))

# Insert pharmacokinetics
cursor.execute("""
    INSERT INTO pharmacokinetics (drug_id, half_life_hr, bioavailability, onset_min)
    VALUES (?, ?, ?, ?)
""", (drug_id, 0.25, 0.68, 15))

# Insert pharmacodynamics
cursor.execute("""
    INSERT INTO pharmacodynamics (drug_id, effect_start_hr, effect_end_hr, model_type, IC50)
    VALUES (?, ?, ?, ?, ?)
""", (drug_id, 0.25, 4.0, "sigmoid", 2.4))

conn.commit()
conn.close()

