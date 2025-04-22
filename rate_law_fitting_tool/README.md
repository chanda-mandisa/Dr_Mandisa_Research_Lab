> ⚠️ **Note:** This tool is actively evolving. Future updates will include support for custom rate laws, enzyme kinetics, and multi-step mechanisms.

# ⏱️ Rate Law Fitting Tool

This tool analyzes concentration vs time data to determine reaction rate laws and calculate rate constants. It supports core kinetic models and provides visual feedback for chemistry learners and researchers.


## 🧬 Description

Users can:
- Input experimental data as a CSV or manual entry  
- Fit data to:
  - Zero-order: [A] = [A]₀ - kt  
  - First-order: ln[A] = ln[A]₀ - kt  
  - Second-order: 1/[A] = 1/[A]₀ + kt  
- Receive:
  - Best-fit curve and equation  
  - Rate constant `k`  
  - R² value and residual analysis  
  - Graph with fitted curve and raw data


## 🎯 Use Cases

- General and physical chemistry labs  
- Reaction mechanism evaluation  
- Undergraduate research projects  
- Pharmaceutical reaction kinetics

This project supports the **Dr. Mandisa Research Lab** initiative to build data-literate, accessible chemistry tools that empower both students and professionals.


## 📁 Files


## 🧠 Next Steps

- Add support for reversible or equilibrium rate laws  
- Enable custom user-defined rate laws (ODE format)  
- Implement enzyme kinetics models (Michaelis-Menten, inhibition types)  
- Include export options: graphs, fit report, data table  
- Add dynamic visualization and slider-based simulations


## 🧰 Technologies Used

- **Python** – core logic and modeling  
- **NumPy / SciPy** – curve fitting and regression  
- **Pandas** – for CSV data input/output  
- **Matplotlib / Seaborn** – for data and residual plots  
- **Streamlit** *(planned)* – browser interface  
