
> ⚠️ **Note:** This tool is actively evolving. Additional features such as residue labeling, contact mapping, and batch mode will be added in future updates.

# 🧬 Protein-Ligand Docking Viewer

This tool visualizes protein-ligand docking interactions in 3D. Designed for researchers, students, and bioinformatics educators, it helps interpret docking results and understand binding behavior—completely free and open-source.


## 🧬 Description

The viewer can:
- Load protein and ligand structures in PDB, PDBQT, or SDF formats  
- Display:
  - Protein backbone (ribbon or surface)  
  - Ligand pose in binding pocket  
  - Optional: Hydrogen bonding, hydrophobic contact highlights  
- Rotate, zoom, and pan for full inspection  
- Color-code atoms or residues by type or interaction  

Planned:
- Score overlays (docking affinity, RMSD between poses)  
- Multiple docking pose viewer  
- Residue label tool + export options


## 🎯 Use Cases

- Drug discovery education (e.g., docking 101)  
- Structural biology walkthroughs  
- Medicinal chemistry or molecular modeling analysis  
- Research visualization in presentations or publications

This project supports the **Dr. Mandisa Research Lab** mission to build equitable and visually rich science tools that are accessible globally.


## 📁 Files



## 🧠 Next Steps

- Add hydrogen bond and interaction overlays  
- Support multi-pose docking analysis (with pose comparison)  
- Build a Streamlit GUI with file upload and viewer  
- Enable exporting of views as PNGs or annotated PDFs  
- Connect with ligand library for docking-from-database support


## 🧰 Technologies Used

- **Python** – backend and logic  
- **Py3Dmol** – interactive molecular visualization  
- **RDKit / Open Babel** – structure conversion and analysis  
- **Biopython** – (optional) for protein sequence handling  
- **Streamlit** *(planned)* – browser GUI for accessibility  
