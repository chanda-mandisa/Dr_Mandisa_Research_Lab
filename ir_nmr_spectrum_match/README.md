> ⚠️ **Note:** This tool is under development. Future updates will include expanded group libraries, spectral image parsing, and multi-spectrum integration.

# 🔍 IR/NMR Spectrum Match

This tool identifies functional groups and structural features by comparing IR and NMR spectral data to known chemical signatures. It brings open-source spectral analysis to classrooms, researchers, and independent scientists.


## 🧬 Description

Users can input:
- IR peak values in cm⁻¹
- NMR shifts in ppm (¹H and ¹³C, optional multiplicity/integration)

The tool:
- Matches peaks to known functional groups (e.g., alcohols, amides, ketones)
- Identifies overlapping patterns across IR and NMR data
- Suggests likely compound classes or fragments
- Outputs predictions with optional confidence scores


## 🎯 Use Cases

- Spectroscopy education and lab reports  
- Quick ID of compounds based on partial spectra  
- Cross-checking assigned peaks in unknowns  
- Simulating expected spectra for known compounds

This tool supports the **Dr. Mandisa Research Lab** initiative for open-access chemistry education and data-driven interpretation.


## 📁 Files


## 🧠 Next Steps

- Add image upload with OCR/AI to detect peaks from spectrum scans  
- Improve peak matching logic for multiple overlapping groups  
- Integrate real compound suggestions via PubChem or ChEMBL  
- Build Streamlit GUI for step-by-step matching and visualization  
- Enable spectrum prediction for entered compounds (reverse mode)


## 🧰 Technologies Used

- **Python** – main scripting and logic  
- **Pandas** – reading CSV input and formatting output  
- **RDKit / Open Babel** – molecular structure support (planned)  
- **Matplotlib / Plotly** – peak visualizations and overlays (planned)  
- **Streamlit** *(planned)* – GUI interface for accessibility  
