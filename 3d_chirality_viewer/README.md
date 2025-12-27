⚠️ **Note:** This project is under development. Future versions will include enantiomer comparison and symmetry detection.

# 🧬 3D Chirality Viewer

This interactive tool visualizes molecular chirality in 3D. It highlights stereocenters, enables real-time molecule rotation, and supports stereochemical interpretation through open-source cheminformatics.


## 🧬 Description

Users can:
- Upload or input a molecular structure:
  - SMILES  
  - SDF  
  - PDB  
- View a 3D rotatable model of the molecule  
- Automatically highlight:
  - Chiral centers  
  - Assigned configurations (R/S, if available)  
- Display wedge/dash bond notation

Planned:
- View enantiomers side-by-side  
- Mirror plane visualization  
- Assign R/S from coordinates (with explanation)  
- Export PNG snapshot of rotated view


## 🎯 Use Cases

- Organic chemistry students learning stereochemistry  
- Pharmaceutical researchers validating chirality in drug models  
- Structure-function exploration in biochemistry  
- Presentations, lectures, and lab reports

This project is part of the **Dr. Mandisa Research Lab** suite of visual, intuitive, and ethically open chemistry tools.



## 📁 Files



## 🧠 Next Steps

- Add enantiomer comparison mode  
- Show mirror planes and determine symmetry elements  
- Automate R/S configuration with visual overlays  
- Support molecule input via drag-and-drop or InChI key  
- Enable export of views for study or publication


## 🧰 Technologies Used

- **Python** – main logic and molecule parsing  
- **RDKit / Open Babel** – stereochemistry detection and structure generation  
- **Py3Dmol** – 3D molecule rendering  
- **Streamlit** *(planned)* – GUI for molecule upload and viewer  
- **JSON / SDF** – input and export formats  
