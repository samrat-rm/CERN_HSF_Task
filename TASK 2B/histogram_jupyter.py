import pyhepmc
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
from ipywidgets import interact

hepmc_file = "data/top.hepmc"

electron_pids = {11, -11}  # e⁻, e⁺
muon_pids = {13, -13}  # μ⁻, μ⁺

def calculate_kinematics(p):
    pt = np.sqrt(p.px**2 + p.py**2)
    eta = 0.5 * np.log((p.e + p.pz) / (p.e - p.pz)) if abs(p.e - p.pz) > 0 else 0
    return pt, abs(eta)

def load_events(hepmc_file):
    electrons = []
    muons = []

    with pyhepmc.open(hepmc_file) as f:
        for event in f:
            for particle in event.particles:
                if particle.status == 1: 
                    pt, eta = calculate_kinematics(particle.momentum)

                    if particle.pid in electron_pids:
                        electrons.append((pt, eta))
                    elif particle.pid in muon_pids:
                        muons.append((pt, eta))

    return electrons, muons

electrons, muons = load_events(hepmc_file)

def plot_pt_distribution(max_eta=2.5):

    filtered_electrons = [pt for pt, eta in electrons if eta <= max_eta]
    filtered_muons = [pt for pt, eta in muons if eta <= max_eta]

    plt.figure(figsize=(8, 6))
    plt.hist(filtered_electrons, bins=50, alpha=0.6, color='blue', edgecolor='black', label="Electrons")
    plt.hist(filtered_muons, bins=50, alpha=0.6, color='red', edgecolor='black', label="Muons")

    plt.xlabel("Transverse Momentum (GeV)")
    plt.ylabel("Frequency")
    plt.title(f"Transverse Momentum Distribution (|η| ≤ {max_eta})")
    plt.yscale("log") 
    plt.legend()
    plt.grid(True)
    plt.show()

# Create an interactive slider for η restriction
interact(plot_pt_distribution, max_eta=widgets.FloatSlider(min=0, max=3.0, step=0.1, value=2.5, description="Max |η|"));