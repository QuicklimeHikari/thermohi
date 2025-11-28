# ThermoHi
_A lightweight Python toolkit for thermal kinetics data analysis and visualization._

[![PyPI Version](https://img.shields.io/pypi/v/thermohipy)](https://pypi.org/project/thermohipy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)]

---

## 📖 Introduction

**ThermoHi** is a small, research-oriented Python package for thermal kinetic analysis  
and data visualization, designed for TG/DTG analysis in polymer and biomass pyrolysis. 
It supports calculating apparent activation energy with model-free methods such as **FWO**, **KAS**, **Starink**, **Friedman**, and  **Vyazovkin method**
with clean APIs and ready-to-plot results. (You can also export the data and use your own software to create the plots.)

> An example file (`example.py`) is included to illustrate the usage of ThermoHi's main functionalities.

---
## examples
FWO method：
![FWO method](/Users/caoyang/Desktop/Cao_Python_Program/thermohi_package/plot_thermohi/Figure_1.png "FWO method")
KAS method:
![KAS method](/Users/caoyang/Desktop/Cao_Python_Program/thermohi_package/plot_thermohi/Figure_2.png "KAS method")
Starink method:
![Starink method](/Users/caoyang/Desktop/Cao_Python_Program/thermohi_package/plot_thermohi/Figure_3.png "Starink method")
Friedman method:
![Friedman method](/Users/caoyang/Desktop/Cao_Python_Program/thermohi_package/plot_thermohi/Figure_4.png "Friedman method")
Vyazovkin method:
![Vyazovkin method](/Users/caoyang/Desktop/Cao_Python_Program/thermohi_package/plot_thermohi/Figure_5.png "Vyazovkin method")

## 🔬 Planned Features
Future versions of **ThermoHi** will include:

- [ ] Support for importing experimental data directly from `.csv` or `.xlsx` files (via `pandas`)
- [ ] Unified plotting style for publication-ready figures (Matplotlib themes)
- [ ] Exporting results as `.csv`
- [ ] Directly read TG/DTG experimental data and automatically extract corresponding `(T, β, dα/dT)` values based on user-selected α

---
## 📄 License

Distributed under the **MIT License**.\
See [`LICENSE`]() for details.


##  Author

**Hikari Quicklime, Ph.D.**  
Forestry Industry Researcher & Independent Developer  
[GitHub: QuicklimeHikari](https://github.com/QuicklimeHikari)

## ⚙️ Installation

```bash
pip install thermohipy
