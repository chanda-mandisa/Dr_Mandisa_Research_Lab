> ⚠️ **Note:** This tool is under active development and may be updated to include redox, ionic, and advanced formatting options.

# ⚖️ Equation Balancing Tool

This project balances chemical equations using symbolic parsing and linear algebra. Built for education and research, it offers a free and open-source alternative to proprietary chemistry software.


## 🧬 Description

Users can input an unbalanced chemical equation in plain text (e.g., `H2 + O2 -> H2O`), and the tool will:
- Parse molecular formulas and elements  
- Apply conservation of mass principles  
- Return a balanced equation with integer coefficients  
- (Planned) Show optional step-by-step solution and oxidation state tracking

Supports:
- Polyatomic ions and parentheses  
- Basic redox balancing (planned)  
- Both gas-phase and aqueous systems


## 🎓 Educational + Research Goals

This tool helps students, educators, and researchers by:
- Reinforcing stoichiometric concepts  
- Simplifying reaction setup for lab reports  
- Providing copy-ready outputs for publications or slides

Part of the **Dr. Mandisa Research Lab**, this project supports transparent, accessible, and reusable scientific tooling.


## 📁 Files




## 🧠 Next Steps

- Implement redox balancing with oxidation number tracking  
- Add support for ionic and net ionic equations  
- Create GUI or web interface using Streamlit  
- Enable batch processing of reaction files  
- Add interactive visualization for educational use


## 🧰 Technologies Used

- **Python** – main parsing and balancing logic  
- **SymPy / NumPy** – symbolic math and matrix solutions  
- **Regular expressions** – chemical formula recognition  
- **Streamlit** *(planned)* – for web-based interface  
