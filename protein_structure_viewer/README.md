> ⚠️ **Note:** This tool is under active development. AlphaFold integration and structure annotation features are planned for future updates.

# 🧬 Protein Structure Viewer

This tool renders 3D protein structures from PDB files or online IDs. Designed for both educational and research use, it provides a fast, open, and interactive way to explore proteins at the atomic level.


## 🧬 Description

Key features:
- Load and visualize 3D structures from:
  - Local PDB files  
  - PDB accession codes (e.g., `1A2B`)  
  - (Planned) AlphaFold structure predictions  
- Display options:
  - Backbone  
  - Ribbon  
  - Surface model  
  - Stick/space-filling atoms  
- Highlight:
  - Specific residues or chains  
  - Ligand binding sites  
  - Structural motifs (e.g., beta sheets, helices)


## 🎯 Use Cases

- Protein folding and structure education  
- Structure review in bioinformatics research  
- Comparing known vs predicted models  
- Presentations, lectures, and journal clubs

This project supports the **Dr. Mandisa Research Lab** mission of open, visually intuitive science tools that bring complex molecular structures to life.


## 📁 Files



## 🧠 Next Steps

- Add AlphaFold model viewer with UniProt ID search  
- Implement structure annotation (e.g., binding sites, mutations)  
- Enable download of views as images  
- Add GUI filters (chains, secondary structure types, ligands)  
- Allow side-by-side structure comparisons


## 🧰 Technologies Used

- **Python** – core logic  
- **Py3Dmol** – interactive 3D molecular rendering  
- **Biopython** – protein metadata and sequence handling  
- **Streamlit** *(planned)* – GUI for real-time interaction  
- **RDKit / Open Babel** *(optional)* – for ligand parsing or hybrid visualizations  
