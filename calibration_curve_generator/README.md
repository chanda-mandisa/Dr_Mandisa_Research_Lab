> ⚠️ **Note:** This project is under active development and may evolve as new features and tools are integrated.

# 📈 Calibration Curve Generator

This tool creates calibration curves from known standard data, allowing users to quantify unknown samples using best-fit models. Designed for researchers, students, and educators, it replaces expensive proprietary software with a free and open-source alternative.


## 🧬 Description

The Calibration Curve Generator accepts numerical input for known concentrations and corresponding instrument responses (e.g., absorbance, fluorescence). It outputs:

- A best-fit curve (linear by default, nonlinear planned)
- Slope, intercept, and R² values
- Estimated concentration of unknown samples
- A visual plot of data and regression line


## 🎯 Use Cases

- Spectrophotometric quantification  
- Drug assays and dissolution studies  
- Food and beverage testing  
- Environmental monitoring (e.g., water contaminants)

This project supports the **Dr. Mandisa Research Lab** mission of creating accessible, ethical, and open scientific tools.


## 📁 Files

| File                     | Purpose                                         |
|--------------------------|-------------------------------------------------|
| `calibration_curve.py`   | Core regression logic and plotting              |
| `analyze_unknowns.py`    | Applies model to unknowns and estimates values  |
| `demo_dataset.csv`       | Sample input data for testing                   |
| `generate_report.py`     | (Planned) Export summary and plots to PDF/PNG   |


## 🧠 Next Steps



## 🧰 Technologies Used

- **Python** – core logic and modeling  
- **Pandas** – data input/output and manipulation  
- **NumPy** – statistical calculations  
- **Matplotlib / Seaborn** – graphing and curve visualization  
- **Scikit-learn / SciPy** – regression models and curve fitting  
- **Streamlit** *(planned)* – browser-based GUI for interaction  
