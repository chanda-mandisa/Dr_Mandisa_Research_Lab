import numpy as np
import matplotlib.pyplot as plt

# === Pharmacokinetics ===
dose_mg = 500  # mg
volume_L = 5   # Approx. blood volume in liters
initial_concentration = dose_mg / volume_L  # mg/L
half_life_hr = 0.25

# === Pharmacodynamics ===
IC50 = 2.4  # µM
hill_coefficient = 1
model_type = "sigmoid"

# === Time setup ===
hours = np.linspace(0, 4, 100)
decay_constant = np.log(2) / half_life_hr
concentration = initial_concentration * np.exp(-decay_constant * hours)

# Convert to µM assuming molar mass of aspirin ~180.16 g/mol
concentration_uM = (concentration * 1000) / 180.16

# Sigmoid model
effect = 100 * (concentration_uM**hill_coefficient) / (IC50**hill_coefficient + concentration_uM**hill_coefficient)

# === Plot ===
plt.figure(figsize=(10, 6))
plt.plot(hours, effect, label="Simulated Effect (%)", color="blue")
plt.plot(hours, concentration_uM, label="Concentration (µM)", color="orange", linestyle="--")
plt.xlabel("Time (hours)")
plt.ylabel("Effect / Concentration")
plt.title("Aspirin PK/PD Simulation")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

