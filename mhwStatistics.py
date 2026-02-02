# IMPORT MODULES
from mhwAux import stackRanges

# DEFINE FUNCTIONS

def climgMean(ds_sst, MHW_date, climY_start, climY_end, MHW_window):

    """

    Compute mean SST value pixel by pixel within the window period during climatology range. 

    Parameters
    ----------
    NOTE: See parameters description in mhwMap.py module

    Returns
    -------
    xarray.DataArray ???
        Mean SST value pixel by pixel within the window period during climatology range.
        
    """
    
    return stackRanges(ds_sst, MHW_date, climY_start, climY_end, MHW_window).mean(dim="time")

def climgThresh(ds_sst, MHW_date, climY_start, climY_end, MHW_window, percentile):

    """

    Compute n percentile SST value pixel by pixel within the window period during climatology range. 

    Parameters
    ----------
    NOTE: See parameters description in mhwMap.py module

    Returns
    -------
    xarray.DataArray ???
        n percentile SST value pixel by pixel within the window period during climatology range.
        
    """
    
    return stackRanges(ds_sst, MHW_date, climY_start, climY_end, MHW_window).quantile(percentile, dim="time")

def climgDiff(ds_sst, MHW_date, climY_start, climY_end, MHW_window, percentile):

    """

    Compute the difference between the n percentile and mean SST value pixel by pixel within the window 
    period during climatology range. 

    Parameters
    ----------
    NOTE: See parameters description in mhwMap.py module

    Returns
    -------
    xarray.DataArray ???
        Difference between the n percentile and mean SST value pixel by pixel within the window 
    period during climatology range
        
    """

    mean = climgMean(ds_sst, MHW_date, climY_start, climY_end, MHW_window)
    thresh = climgThresh(ds_sst, MHW_date, climY_start, climY_end, MHW_window, percentile)

    return thresh - mean