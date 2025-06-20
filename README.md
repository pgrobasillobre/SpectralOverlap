# Spectral Overlap Calculator

This is a small Python script for computing the **spectral overlap integral** between two molecular spectra — typically, the **emission spectrum** of a donor and the **absorption spectrum** of an acceptor. This quantity is often used in energy transfer studies, such as Förster Resonance Energy Transfer (FRET).

---

## What It Does

Given two CSV files with spectral data in the form:

```
Energy (eV), Intensity (or Absorbance)
```

the script:

- Interpolates both datasets to a fine energy grid
- Normalizes each spectrum
- Computes the spectral overlap integral:

$$
J = \int \text{Emission}(E) \cdot \text{Absorption}(E) \ dE
$$


- Outputs normalized spectra and prints the overlap in units of **eV⁻¹**

---

## Quick Start

### Requirements

- Python 3
- `numpy`, `scipy`, `matplotlib`

Install dependencies (if needed):

```
pip install numpy scipy matplotlib
```

### Run the Script

```
python3 spectral_overlap.py donor_emission.csv acceptor_absorption.csv
```

---

## Important

Before running, edit the script to define the desired energy window and resolution:

```python
# --> Input variables
min_energy    = 1.872   # Minimum Energy for the convoluted spectra in eV
max_energy    = 1.950   # Maximum Energy for the convoluted spectra in eV
grid_points   = 100000  # Number of energy points in the spectral range
```

---

## Example Included

Inside the folder `absorption-emission-example/`, you’ll find:

- `znpc-abs.csv` – Absorption spectrum of ZnPc
- `pdpc-em.csv` – Emission spectrum of PdPc

These data are digitized from:

> **S. Cao et al.**, Nature Chemistry (2022)  
> [https://doi.org/10.1038/s41557-021-00697-z](https://doi.org/10.1038/s41557-021-00697-z)

Use the example like this:

```
python3 spectral_overlap.py absorption-emission-example/pdpc-em.csv absorption-emission-example/znpc-abs.csv
```

---

## Output

- `data1_norm.csv`: Normalized emission data (donor)
- `data2_norm.csv`: Normalized absorption data (acceptor)
- Console output includes the **spectral overlap value**

---

## Author

Developed by **Pablo Grobas Illobre**  
contact: pgrobasillobre@gmail.com

---

## Funding

This project has been supported by the **FARE 2020** program — *"Framework per l’attrazione e il rafforzamento delle eccellenze per la ricerca in Italia."*

---

## License

This code is licensed under the **GNU General Public License v3.0**.
