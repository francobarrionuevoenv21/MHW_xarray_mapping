# IMPORT LIBRARIES AND MODULES
import xarray as xr
import numpy as np
from .mhwStatistics import climgThresh, climgDiff

# DEFINE FUNCTIONS
def intensityCont(ds_sst, MHW_date, climY_start, climY_end, MHW_window, thresh, mask):

    """
    Compute the anomaly between MHW peak intensity and climatology threshold.

    Parameters
    ----------
    NOTE: See parameters description in mhwMap.py module

    Returns
    -------
    xarray.DataArray
        Anomaly between MHW peak intensity and climatology threshold.
    """

    # Get peak intensity MHW data
    sst_MHWDate = ds_sst.sel(time = MHW_date)

    # Get sst threshold within the climatology period (predefinded: 90th percentile)
    sst_thresh = climgThresh(ds_sst, MHW_date, climY_start, climY_end, MHW_window, thresh)

    # Get continuous intensity value at the MHW date 
    intCont_MHWDate = sst_MHWDate - sst_thresh

    # Mask negative values
    ## NOTE: future work will include cold spells (intensity < 0) analysis
    if mask == True:
        intCont_MHWDate = intCont_MHWDate.where(intCont_MHWDate > 0)

    return intCont_MHWDate

def intensityCat(ds_sst, MHW_date, climY_start, climY_end, MHW_window, thresh, mask):
    
    """
    Compute the anomaly between MHW peak intensity and climatology threshold.

    Parameters
    ----------
    NOTE: See parameters description in mhwMap.py module

    Returns
    -------
    xarray.DataArray
        Anomaly between MHW peak intensity and climatology threshold.
    """

    # Get peak intensity MHW data
    intCont_MHWDate = intensityCont(ds_sst, MHW_date, climY_start, climY_end, MHW_window, thresh, mask)

    # Get sst climatology difference between the threshold and the climatology mean
    sst_climgDiff = climgDiff(ds_sst, MHW_date, climY_start, climY_end, MHW_window, thresh)

    # Compute the intensity/(thresh-clim) ratio
    ratio = intCont_MHWDate / sst_climgDiff
    
    # Initialize the categorical dataset with nan values
    intCat_MHWDate = xr.full_like(ratio, fill_value = np.nan) 
    
    # Fill with the category value according to the range
    intCat_MHWDate = xr.where(ratio > 3, 4, intCat_MHWDate)
    intCat_MHWDate = xr.where((ratio > 2) & (ratio <= 3), 3, intCat_MHWDate)
    intCat_MHWDate = xr.where((ratio > 1) & (ratio <= 2), 2, intCat_MHWDate)
    intCat_MHWDate = xr.where((ratio > 0) & (ratio <= 1), 1, intCat_MHWDate)
    
    return intCat_MHWDate
