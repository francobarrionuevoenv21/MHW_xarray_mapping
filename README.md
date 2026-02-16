# MHW XArray Mapping
### Marine Heatwave Mapping with Xarray

A Python toolkit for mapping and analyzing **Marine Heatwaves (MHWs)** using gridded Sea Surface Temperature (SST) datasets and xarray.
This repository provides tools to compute ocean warm intensity continously or categorized during a MHW and map it according to the methodology defined by [Hobday et al. (2016)](https://www.sciencedirect.com/science/article/abs/pii/S0079661116000057

---

## 📖 Scientific Background

Marine Heatwaves (MHWs) are prolonged periods of anomalously warm ocean temperatures that can significantly impact marine ecosystems.

MHW detection typically follows the framework described by:

> Hobday et al. (2016) — A hierarchical approach to defining marine heatwaves.

This repository focuses on the **mapping and spatial analysis stage** once MHW dates or event windows are identified.

---

## 🔄 Recommended Workflow

To use this tool effectively, follow these steps:

### 1️⃣ Obtain Sea Surface Temperature Data

Download gridded SST data from a reliable source, such as:

- NOAA OISST  
- ERA5 reanalysis  
- CMEMS products  
- Other NetCDF SST datasets  

Ensure the dataset:
- Is in NetCDF format  
- Contains a time dimension  
- Uses consistent spatial coordinates (lat/lon)  

---

### 2️⃣ Detect Marine Heatwave Events

Detect MHW events using an established detection tool such as:

- The original Hobday et al. MATLAB implementation  
- A Python implementation of the Hobday framework  
- Your own MHW detection pipeline  

This step should provide:
- Event start and end dates  
- Event peak date  
- Event duration  
- Threshold percentile  

---

### 3️⃣ Clone This Repository

```bash
git clone https://github.com/yourusername/MHWxAMap.git
cd MHWxAMap
