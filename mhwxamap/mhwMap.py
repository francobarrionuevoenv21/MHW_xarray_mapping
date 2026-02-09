"""

Project description
-------------------
The MHW XArray Mapping (mhwXarrayMapping) consists in a Python implementation, under the XArray framework, of the
MHW computation methodology for multidimentional data according to Hobday et al. (2016) & Hobday et al., (2018). 
This implementation allows to compute MHW continuous and categorized intensity for a specific date, and from the 
results obtain maps of the event.

The code was developed to map MHW from daily SST data from OISST (Huang et al., 2021). Data con be downloaded from:
https://www.ncei.noaa.gov/products/optimum-interpolation-sst
Other SST data sources, but it may neccesary to posterior validation. 

Parameters description
----------------------
sst_path : str
        SST data path.
MHW_date : str
        MHW date in "YYYY-MM-DD" format.
climY_start : int
        Start year for climatology period.
climY_end : int
        End year for climatology period.
MHW_window : int, optional
        Number of days to add/subtract from MHW peak intensity date (default is 5).
percentile : int, optional
        Percentile threshold for climatology (default is 90).
mask : bool, optional
        Whether to mask negative anomalies (default is True).

References
----------
    Hobday, A. J. et al. (2016). A hierarchical approach to defining marine heatwaves. Progress in
Oceanography, 141, 227–238. https://doi.org/10.1016/j.pocean.2015.12.014
    Hobday, A.J. et al. (2018). Categorizing and naming marine heatwaves. Oceanography
31(2):162–173, https://doi.org/10.5670/oceanog.2018.205
    Huang, B. et al. (2021). Improvements of the Daily Optimum Interpolation Sea Surface Temperature 
(DOISST) Version 2.1. Journal of Climate, 34(8), 2923-2939. https://doi.org/10.1175/JCLI-D-20-0166.1

"""

# IMPORT MODULES
from .mhwAux import openSST
from .mhwIntensity import intensityCont, intensityCat

# DEFINE DEFAULT PARAMETERS VALUES (ACCORDING TO HOBDAY ET AL., 2016)
CLIMG_YSTART = 1983
CLIMG_YEND = 2012
WINDOW = 5
PERCENTILE = 90
MASK = True ## Not compulsory, but avoids negative intensity values (cold spells)

# DEFINE FUNCTIONS

def mapIntensityCont(sst_path, MHW_date, climY_start = CLIMG_YSTART, climY_end = CLIMG_YEND, MHW_window = WINDOW, percentile = PERCENTILE/100, mask = MASK):

    """

    Map continuous intensity anomaly for a given MHW event.
    For further details about the methodology see Hobday et al. (2016) & Hobday et al., (2018)

    Parameters
    ----------
    NOTE: See parameters description above

    Returns
    -------
    xarray.DataArray
        Continuous intensity anomaly map for the MHW event.
        
    """

    # Open SST dataset
    ds_sst = openSST(sst_path)

    # Compute continuous intensity
    intCont_map = intensityCont(ds_sst, MHW_date, climY_start, climY_end, MHW_window, percentile, mask)

    return intCont_map

def mapIntensityCat(sst_path, MHW_date, climY_start = CLIMG_YSTART, climY_end = CLIMG_YEND, MHW_window = WINDOW, percentile = PERCENTILE/100, mask = MASK):

    """
    Map categorized intensity anomaly for a given MHW event.

    Category 1: Moderate;
    Category 2: Strong;
    Category 3: Severe;
    Category 4: Extreme.

    For further details about the methodology and categories definition see Hobday et al. (2016) & Hobday et al., (2018)

    Parameters
    ----------
    NOTE: See parameters description above

    Returns
    -------
    xarray.DataArray
        Categorized intensity map for the MHW event.
    """

    # Open SST dataset
    ds_sst = openSST(sst_path)

    # Compute categorized intensity
    intCat_map = intensityCat(ds_sst, MHW_date, climY_start, climY_end, MHW_window, percentile, mask)

    return intCat_map
