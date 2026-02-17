# MHW XArray Mapping 🌡️🌊🗺️
### Marine Heatwave Mapping with Xarray

A Python toolkit for mapping and analyzing **Marine Heatwaves (MHWs)** using gridded Sea Surface Temperature (SST) datasets and XArray.
This repository provides tools to compute ocean warm intensity continously or categorized during a MHW and map it according to the methodology defined by Hobday et al. (2016).

---

## Marine Heatwaves

According to Hobday et al. (2016), a MHW is defined as a  “prolonged discrete anomalously warm water event that can be described by its duration, intensity, rate of evolution, and spatial extent”. These events are relevant because of the variety of impacts that have been associated with, including shifts in species ranges and local extinctions, and economic impacts on aquaculture and seafood industries through declines in important fishery species.

---

## Recommended Workflow

To use this tool effectively, follow these steps:

### 1. Obtain Sea Surface Temperature Data

Download gridded SST data from a reliable source with a daily temporal resolution. One of the most used products for this case is the OISST (Huang et al., 2021). Data con be downloaded from [here](https://www.ncei.noaa.gov/products/optimum-interpolation-sst)

Ensure the dataset:
- Has, at least, 30 years of data 
- Is in NetCDF or any other XArray supported format   
- Uses consistent spatial coordinates (lat/lon)  

---

### Detect Marine Heatwave Events

Detect MHW events for your study region using any of the available implementations of the Hobday et al. (2016) methodology. You can try with [Python implementation created by Eric C. J. Oliver] (https://github.com/ecjoliver/marineHeatWaves) or build your own one. 

This step should provide:
- Event start and end dates  
- Event peak date  

---

This repository provides tools to compute ocean warm intensity continously or categorized during a MHW and map it according to the methodology defined by [Hobday et al. (2016)](https://www.sciencedirect.com/science/article/abs/pii/S0079661116000057)


### 3️⃣ Clone This Repository

```bash
git clone https://github.com/yourusername/MHWxAMap.git
cd MHWxAMap
