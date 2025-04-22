> ⚠️ **Note:** This project is actively evolving. Upcoming features include diprotic titrations, animated dropwise additions, and indicator visualizations.

# ⚗️ Titration Simulator

This interactive tool models acid-base titrations, generating titration curves and key analytical values based on user input. It's ideal for chemistry students, instructors, and lab planners seeking to visualize and understand pH behavior in real time.


## 🧬 Description

Users can simulate:
- **Strong acid + strong base**
- **Weak acid + strong base**
- **Strong acid + weak base**
- (Planned) Diprotic and polyprotic acid systems

Inputs:
- Acid/base concentration  
- Initial volume of titrand  
- Titrant concentration  
- Ka or Kb (for weak systems)

Outputs:
- Titration curve (Volume vs pH)  
- Calculated:
  - Equivalence point(s)  
  - Half-equivalence point  
  - pKa/pKb and buffer region  


## 🎯 Use Cases

- Chemistry classroom demonstrations  
- pH curve sketching practice  
- Lab report planning or validation  
- Understanding buffer behavior and acid/base theory

This project is part of the **Dr. Mandisa Research Lab**, built to enhance visual learning, data-driven thinking, and open access to high-quality scientific tools.


## 📁 Files



## 🧠 Next Steps

- Add diprotic/polyprotic acid titration support  
- Simulate indicator color changes at endpoint  
- Include titration animation (drop-by-drop)  
- Allow export of data and plots for lab reports  
- Add quiz mode: "Predict the shape of this titration curve"


## 🧰 Technologies Used

- **Python** – core calculations  
- **NumPy / SciPy** – pH and buffer math  
- **Matplotlib / Plotly** – titration curve plotting  
- **Streamlit / Tkinter** *(planned)* – GUI for interactive simulation  
- **JSON** – for acid/base presets and indicator data  
