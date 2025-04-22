> ⚠️ **Note:** This project is in active development. Support for user-defined potentials and time-dependent simulations is coming soon.

# 🧠 Schrödinger Equation Demo

This tool solves and visualizes solutions to the time-independent Schrödinger equation for 1D quantum systems. It helps learners explore quantum phenomena like wavefunctions, quantized energy, and tunneling—interactively and intuitively.


## 🧬 Description

The tool numerically solves:
- **Infinite potential well**
- **Finite square well**
- **Harmonic oscillator**
- **Potential step/barrier**

Users can:
- Set physical parameters (mass, well width, potential height)
- View calculated energy levels (Eₙ)  
- Plot wavefunctions (ψₙ(x)) and probability densities (|ψₙ(x)|²)  
- Overlay results on the potential energy graph  
- (Planned) Animate time-dependent wavefunction behavior


## 🎯 Use Cases

- Teaching and learning quantum chemistry or physics  
- Demonstrating quantization, tunneling, and boundary effects  
- Self-study, homework support, or exam review  
- Scientific outreach and visualization

This project supports the **Dr. Mandisa Research Lab** initiative to make quantum science beautiful, accessible, and hands-on for all.


## 📁 Files


## 🧠 Next Steps

- Add custom potential input mode  
- Implement time-dependent Schrödinger animation (wavepacket motion)  
- Support export of wavefunctions and energies  
- Build GUI with real-time sliders for mass, box width, energy level  
- Add 3D surface visualization of ψ(x, t) using Plotly or Mayavi


## 🧰 Technologies Used

- **Python** – for all simulation logic  
- **NumPy / SciPy** – numerical methods and eigenvalue solvers  
- **Matplotlib / Plotly** – wavefunction and energy plots  
- **Streamlit / Tkinter** *(planned)* – GUI interface  
- **SymPy** *(optional)* – symbolic verification for known solutions  
