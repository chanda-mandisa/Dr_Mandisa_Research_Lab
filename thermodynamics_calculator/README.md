> ⚠️ **Note:** This tool is actively evolving. Compound data integration and advanced solver features will be added soon.

# ♨️ Thermodynamics Calculator

This calculator helps users compute key thermodynamic values—including ΔG, ΔH, ΔS, and K—using well-known equations and user-defined inputs. It's designed for learners, teachers, and researchers seeking accurate, open-source chemical tools.


## 🧬 Description

Supports the following calculations:
- Gibbs Free Energy:
  - ΔG = ΔH - TΔS  
  - ΔG = -RT ln(K)
- Equilibrium Constant:
  - K = e^(-ΔG/RT)
- Temperature conversions (°C ↔ K)
- Unit conversions (J, kJ, cal)
- Step-by-step logic for all calculations (optional)

Users can input:
- Temperature (K or °C)  
- ΔH, ΔS, ΔG (with unit selector)  
- Equilibrium constant K


## 🎯 Use Cases

- General and physical chemistry students learning thermodynamics  
- Researchers validating equilibrium or energy data  
- Lab reports and scientific calculations  
- Cross-checking theoretical vs experimental values

This tool is part of the **Dr. Mandisa Research Lab**, built to support open, reliable, and thoughtful scientific education.


## 📁 Files


## 🧠 Next Steps

- Add compound lookup database (ΔHf°, S°, etc.)  
- Support Hess’s Law calculations and multiple-step reactions  
- Enable saving/exporting worked problems  
- Add graphical view (e.g., ΔG vs T plot)  
- Build GUI with Streamlit or Tkinter for classroom/demo use


## 🧰 Technologies Used

- **Python** – primary computation engine  
- **NumPy / SymPy** – for numeric and symbolic math  
- **Streamlit / Tkinter** *(planned)* – interactive calculator UI  
- **JSON** – planned data source for compound values  
