# 🧪 Aspirin PK/PD Simulation

This subproject simulates how aspirin interacts with the human body using real pharmacological data.

## 🧬 Description
Using SQLite and Python, this simulation models:
- Aspirin’s blood concentration over time
- Its pharmacodynamic effect based on a sigmoid IC50 model

## 📈 Visualization
The graph below shows blood concentration (orange) and simulated effect strength (blue):

![output](https://github.com/user-attachments/assets/fc585e5e-2f0b-48c1-ba5d-bfdb42df0f58)


## 📚 Data Sources
- [DrugBank](https://go.drugbank.com/drugs/DB00945)
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/compound/aspirin)
- [ChEMBL](https://www.ebi.ac.uk/chembl/)
- [Protein Data Bank - 3N8Z](https://www.rcsb.org/structure/3N8Z)

## 📁 Files
| File                  | Purpose                                  |
|-----------------------|------------------------------------------|
| `setup_database.py`   | Creates schema and inserts base drug     |
| `insert_aspirin_data.py` | Adds targets, binding, PK/PD           |
| `simulate_aspirin.py` | Runs the simulation and plots graphs     |
| `view_all.py`         | Prints out entire database for inspection|

## 🧠 Next Steps
- Add support for Ibuprofen, Acetaminophen, etc.
- Simulate multi-dose regimens
- Visualize receptor occupancy dynamically
- Create interactive UI or API
