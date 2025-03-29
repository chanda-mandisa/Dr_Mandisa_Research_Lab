import sqlite3

conn = sqlite3.connect("drug_simulation.db")
cursor = conn.cursor()

# Create all necessary tables
cursor.executescript("""
CREATE TABLE IF NOT EXISTS drugs (
    id INTEGER PRIMARY KEY,
    name TEXT,
    smiles TEXT,
    inchi_key TEXT
);

CREATE TABLE IF NOT EXISTS targets (
    id INTEGER PRIMARY KEY,
    drug_id INTEGER,
    protein_name TEXT,
    uniprot_id TEXT,
    pdb_id TEXT,
    binding_affinity REAL,
    FOREIGN KEY(drug_id) REFERENCES drugs(id)
);

CREATE TABLE IF NOT EXISTS binding_sites (
    id INTEGER PRIMARY KEY,
    target_id INTEGER,
    residue TEXT,
    FOREIGN KEY(target_id) REFERENCES targets(id)
);

CREATE TABLE IF NOT EXISTS pharmacokinetics (
    id INTEGER PRIMARY KEY,
    drug_id INTEGER,
    half_life_hr REAL,
    bioavailability REAL,
    onset_min REAL,
    FOREIGN KEY(drug_id) REFERENCES drugs(id)
);

CREATE TABLE IF NOT EXISTS pharmacodynamics (
    id INTEGER PRIMARY KEY,
    drug_id INTEGER,
    effect_start_hr REAL,
    effect_end_hr REAL,
    model_type TEXT,
    IC50 REAL,
    FOREIGN KEY(drug_id) REFERENCES drugs(id)
);
""")

# Insert base Aspirin entry (only if it doesn't exist yet)
cursor.execute("SELECT COUNT(*) FROM drugs WHERE name = ?", ("Aspirin",))
if cursor.fetchone()[0] == 0:
    cursor.execute("""
        INSERT INTO drugs (name, smiles, inchi_key)
        VALUES (?, ?, ?)
    """, ("Aspirin", "CC(=O)OC1=CC=CC=C1C(=O)O", "BSYNRYMUTXBXSQ-UHFFFAOYSA-N"))

conn.commit()
conn.close()
