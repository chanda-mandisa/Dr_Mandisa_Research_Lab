> ⚠️ **Note:** This tool is actively evolving. Future versions will include peak annotation, structure overlay, and export options.

# 📊 Spectroscopy Data Viewer

This tool displays and interprets spectroscopy data, including IR, NMR, UV-Vis, and MS. It helps students and researchers visualize spectral trends, identify peaks, and cross-reference structural data—all with an open, interactive interface.


## 🧬 Description

Supports:
- **Data input**:
  - CSV (e.g., wavenumber vs absorbance)
  - JCAMP-DX (planned)
  - Manually pasted data (wavenumber, shift, intensity)
- **Spectra types**:
  - Infrared (IR)  
  - NMR (¹H, ¹³C)  
  - UV-Vis  
  - Mass spectrometry (MS, planned)
- **Interactive features**:
  - Zoom, hover to view coordinates  
  - Peak labeling (manual or automatic)
  - Overlay multiple spectra for comparison


## 🎯 Use Cases

- Chemistry students learning peak assignment  
- Research projects involving IR/NMR/UV-Vis validation  
- Drug design and quality control labs  
- Data-driven structure analysis

As part of the **Dr. Mandisa Research Lab**, this project supports open, data-centric science with an emphasis on accessibility and beauty in chemical interpretation.


## 📁 Files



## 🧠 Next Steps

- Add JCAMP-DX file support  
- Enable spectrum overlay and peak comparison  
- Integrate peak-matching with IR-NMR Matcher and Functional Group Identifier  
- Build Streamlit GUI for live spectrum interaction  
- Support export of annotated spectra for reports or publication


## 🧰 Technologies Used

- **Python** – core logic  
- **Pandas / NumPy** – data input and manipulation  
- **Matplotlib / Plotly** – interactive spectrum plots  
- **SciPy** – signal processing and peak finding  
- **Streamlit** *(planned)* – GUI for drag-and-drop usage  
