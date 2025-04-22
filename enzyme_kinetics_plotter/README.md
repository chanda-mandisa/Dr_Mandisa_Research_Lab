> ⚠️ **Note:** This project is actively evolving. Expect regular updates as we expand modeling options and user features.

# ⚗️ Enzyme Kinetics Plotter

This tool models enzyme-substrate interactions using classical kinetic equations. It visualizes reaction rate data and calculates key parameters like Vₘₐₓ and Kₘ, offering a free, open-source alternative to costly biochemical analysis software.


## 🧬 Description

The plotter allows users to:
- Input experimental velocity vs substrate concentration data  
- Fit the data to the Michaelis-Menten equation  
- Output Vₘₐₓ and Kₘ values, with optional residual plots  
- Generate additional kinetic representations (planned):
  - Lineweaver-Burk
  - Eadie-Hofstee
  - Hanes-Woolf

It’s useful for biochemistry labs, drug metabolism studies, and teaching enzyme mechanisms.


## 🎯 Use Cases

- Undergraduate or graduate biochemistry labs  
- Pharmacokinetics and drug target modeling  
- Enzyme engineering and catalytic efficiency studies

This project directly supports the **Dr. Mandisa Research Lab** mission of building ethical, accessible, and extensible science tools.


## 📁 Files



## 🧠 Next Steps

- Add error estimation and residual visualization  
- Support CSV upload and batch fitting  
- Build GUI with sliders or inputs for simulation mode  
- Implement enzyme inhibition models (competitive, non-competitive, uncompetitive)  
- Export all outputs to CSV and PNG



## 🧰 Technologies Used

- **Python** – main logic and modeling  
- **Pandas** – data processing and input handling  
- **NumPy** – curve fitting and statistical analysis  
- **Matplotlib / Plotly** – graphing kinetic curves  
- **SciPy** – nonlinear regression (least-squares fitting)  
- **Streamlit** *(planned)* – for browser-based GUI  
