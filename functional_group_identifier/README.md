> ⚠️ **Note:** This tool is being actively developed to support structural parsing, group detection, and spectral matching. New features may be added regularly.

# 🧪 Functional Group Identifier

This tool detects and labels functional groups within organic molecules using SMILES or InChI strings. It provides a free, open-source cheminformatics tool for students, educators, and researchers.


## 🧬 Description

Users can input a molecular representation (e.g., `CC(=O)O`) and receive:
- A list of functional groups present (e.g., carboxylic acid, alkane)  
- Position or count of each group (when applicable)  
- Optional visualization with color-coded highlighting  
- (Planned) Correlation to IR and NMR spectra data  


## 🎯 Use Cases

- Organic chemistry study aid  
- Reaction prediction or retrosynthesis prep  
- Molecule validation for research reports  
- Teaching resource for spectroscopy and group identification

Part of the **Dr. Mandisa Research Lab**, this project promotes equity in science by building accessible, intelligent tools for molecule analysis.


## 📁 Files



## 🧠 Next Steps

- Add support for InChI, .mol, and .sdf file formats  
- Implement IR/NMR peak matching to structural groups  
- Build Streamlit or Tkinter-based GUI for accessibility  
- Enable export of annotated molecule diagrams  
- Add quiz mode for learning functional groups by spectrum


## 🧰 Technologies Used

- **Python** – core logic and parsing  
- **RDKit** – cheminformatics and molecular analysis  
- **Open Babel** *(optional)* – for format conversion and structure validation  
- **Matplotlib / RDKit Draw** – for molecule visualizations  
- **Streamlit** *(planned)* – GUI interface  
