import matplotlib.pyplot as plt
from pymatgen.core import Structure
from pymatgen.io.cif import CifParser
from pymatgen.analysis.diffraction.xrd import XRDCalculator

def generate_xrd_plot(cif_string):
    """
    Calculates and plots the theoretical XRD pattern from a CIF string.
    """
    try:
        # 1. Parse the CIF string into a Pymatgen Structure object
        parser = CifParser.from_str(cif_string)
        structure = parser.get_structures()[0]

        # 2. Initialize the XRD Calculator (using Cu K-alpha radiation by default)
        # wavelength=1.5406 angstroms is standard for lab XRD
        calculator = XRDCalculator(wavelength="CuKa")

        # 3. Calculate the diffraction pattern (2-theta vs intensity)
        pattern = calculator.get_pattern(structure)

        # 4. Create the plot using Matplotlib
        fig, ax = plt.subplots(figsize=(5, 4))
        
        # We use 'vlines' because theoretical peaks are discrete points
        ax.vlines(pattern.x, 0, pattern.y, colors='red', lw=2, label="Theoretical Peaks")
        
        # Formatting the chart for a scientific look
        ax.set_xlabel("2θ (degrees)", fontsize=10)
        ax.set_ylabel("Intensity (a.u.)", fontsize=10)
        ax.set_title("Simulated Diffraction Pattern", fontsize=12)
        ax.set_xlim(10, 80)  # Standard range for most minerals/metals
        ax.set_ylim(0, 110) # Intensities are normalized to 100
        ax.grid(alpha=0.3)
        ax.legend()

        # Return the figure object so Streamlit can display it
        return fig

    except Exception as e:
        # If the CIF is invalid, we return None so the app doesn't crash
        print(f"Simulation Error: {e}")
        return None