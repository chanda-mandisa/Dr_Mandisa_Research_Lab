> ⚠️ **Note:** This project is in early development and will continue to evolve as we add more symbolic math and visualization features.

# 📉 Error Propagation Tool

This tool helps scientists, students, and educators propagate measurement uncertainties through common operations and custom equations. It applies standard analytical chemistry rules to ensure accurate, reproducible reporting of error margins.


## 🧬 Description

Given one or more measured values with associated uncertainties, the tool calculates:
- Final result of the operation or equation  
- Combined uncertainty using appropriate propagation formulas  
- Optional breakdown of each step in the propagation

Supports:
- Addition and subtraction  
- Multiplication and division  
- Constants and exponents  
- (Planned) Arbitrary symbolic equations via LaTeX-style input


## 🎓 Educational + Research Goals

This tool is part of the **Dr. Mandisa Research Lab** initiative to build free, open-access scientific calculators and modeling tools.

Use cases include:
- Analytical chemistry and titration reports  
- Physical chemistry lab writeups  
- Biomedical device calibration  
- Any quantitative experiment involving compound uncertainty


## 📁 Files


## 🧠 Next Steps

- Add symbolic equation parsing (e.g., `z = a * b^2 / c`)  
- Build Streamlit GUI for drag-and-drop style data entry  
- Create exportable reports for lab documentation  
- Visualize uncertainty sensitivity (e.g., error bars, pie charts)  
- Integrate unit tracking and dimensional analysis (e.g., mol/L)


## 🧰 Technologies Used

- **Python** – main numerical and symbolic logic  
- **SymPy / NumPy** – for error math and symbolic handling  
- **Pandas** – for input/output of data files  
- **Streamlit** *(planned)* – GUI for accessibility  
- **Matplotlib** *(planned)* – for visualizations (error bars, distributions)  
