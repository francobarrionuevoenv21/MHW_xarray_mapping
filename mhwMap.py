"""
BRIEF SUMMARY

PARAMETERS EXPLANATION

RESULTS EXPLANATION

"""

# IMPORT MODULES
from mhwAux import openSST
from mhwIntensity import intensityCont, intensityCat

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

    Parameters
    ----------
    NOTE: See parameters explanation in above

    Returns
    -------
    xarray.DataArray
        Continuous intensity anomaly map for the MHW event.
    """

    # Open SST dataset
    ds_sst = openSST(sst_path)

    # Compute continuous intensity anomaly
    intCont_map = intensityCont(ds_sst, MHW_date, climY_start, climY_end, MHW_window, percentile, mask)

    return intCont_map

def mapIntensityCat(sst_path, MHW_date, climY_start = CLIMG_YSTART, climY_end = CLIMG_YEND, MHW_window = WINDOW, percentile = PERCENTILE/100, mask = MASK):

    """
    Map continuous intensity anomaly for a given MHW event.

    Parameters
    ----------
    NOTE: See parameters explanation in above

    Returns
    -------
    xarray.DataArray
        Continuous intensity anomaly map for the MHW event.
    """

    # Open SST dataset
    ds_sst = openSST(sst_path)

    # Compute continuous intensity anomaly
    intCat_map = intensityCat(ds_sst, MHW_date, climY_start, climY_end, MHW_window, percentile, mask)

    return intCat_map
