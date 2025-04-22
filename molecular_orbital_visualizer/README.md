> ⚠️ **Note:** This project is being actively developed. Future features may include quantum-derived orbital shapes and animated hybridization sequences.

# 🌀 Molecular Orbital Visualizer

This tool generates interactive molecular orbital diagrams and 3D orbital illustrations to help students and researchers better understand electronic structure and bonding behavior.


## 🧬 Description

The visualizer can:
- Show atomic orbitals (s, p, d, f) with radial/nodal shapes  
- Generate energy diagrams for diatomic molecules:  
  - H₂, He₂, B₂, C₂, N₂, O₂, F₂  
  - Highlight bonding vs antibonding orbitals  
  - Indicate paramagnetism (e.g., for O₂)  
- (Planned) Visualize 3D isosurfaces of HOMO/LUMO from quantum outputs  
- (Planned) Display hybrid orbitals (e.g., sp², sp³)


## 🎯 Use Cases

- Teaching and learning molecular orbital theory  
- Visualizing paramagnetism, bond order, or orbital overlap  
- Preparing chemistry lecture slides or tutorials  
- Enhancing understanding of reactivity, bonding, and symmetry

As part of the **Dr. Mandisa Research Lab**, this project promotes hands-on quantum chemistry education using free and accessible tools.


## 📁 Files



## 🧠 Next Steps

- Add support for heteronuclear diatomics (e.g., CO, HF)  
- Animate orbital overlap and hybridization steps  
- Integrate output from quantum software (Gaussian, ORCA, PySCF)  
- Build GUI using Streamlit or Py3Dmol for real-time rendering  
- Export diagrams and models for educational content


## 🧰 Technologies Used

- **Python** – core logic and diagram generation  
- **Matplotlib / Plotly / Py3Dmol** – orbital and energy diagram visualizations  
- **NumPy / SymPy** – mathematical modeling of orbital shapes  
- **Streamlit / Tkinter** *(planned)* – GUI for interactive use  
- **RDKit / Open Babel** *(optional)* – molecule parsing and structure generation  
