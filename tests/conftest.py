import os
import matplotlib

# Force headless non-interactive Agg backend to prevent Tkinter GUI thread crashes on Windows/Python 3.14
os.environ["MPLBACKEND"] = "Agg"
matplotlib.use("Agg")
