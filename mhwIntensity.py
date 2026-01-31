from mhwStatistics import climg_thresh


def intensityCont(ds_sst, MHW_date, climY_start, climY_end, MHW_window = 5, thresh = 90, mask = True):
    """
    Compute the anomaly between MHW peak intensity and climatology threshold.

    Parameters
    ----------
    ds_sst : xarray.DataArray
        SST dataset.
    MHW_date : str
        MHW peak intensity date in "YYYY-MM-DD" format.
    climY_start : int
        Start year for climatology period.
    climY_end : int
        End year for climatology period.
    MHW_window : int, optional
        Number of days to add/subtract from MHW peak intensity date (default is 5).
    thresh : float, optional
        Percentile threshold for climatology (default is 90).
    mask : bool, optional
        Whether to mask negative anomalies (default is True).
    Returns
    -------
    xarray.DataArray
        Anomaly between MHW peak intensity and climatology threshold.
    """

    # Get peak intensity MHW scene
    sst_MHWDate = ds_sst.sel(time = MHW_date)

    # Get sst threshold within the climatology period (predefinded: 90th percentile)
    sst_thresh = climg_thresh(ds_sst, MHW_date, climY_start, climY_end, MHW_window, thresh)

    # Get continuous intensity anomaly at MHW date 
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
    ds_sst : xarray.DataArray
        SST dataset.
    MHW_date : str
        MHW peak intensity date in "YYYY-MM-DD" format.
    climY_start : int
        Start year for climatology period.
    climY_end : int
        End year for climatology period.
    MHW_window : int, optional
        Number of days to add/subtract from MHW peak intensity date (default is 5).
    thresh : float, optional
        Percentile threshold for climatology (default is 90).
    mask : bool, optional
        Whether to mask negative anomalies (default is True).
    Returns
    -------
    xarray.DataArray
        Anomaly between MHW peak intensity and climatology threshold.
    """

    # Get peak intensity MHW scene
    sst_MHWDate = ds_sst.sel(time = MHW_date)

    #
    sst_climgDiff = climg_diff(ds_sst, MHW_date, climY_start, climY_end, MHW_window = 5, thresh = 90)

    ratio = sst_MHWDate / sst_climgDiff ## Set the ratio intensity/(thresh-clim)
    
    intCat_MHWDate = xr.full_like(ratio, fill_value = np.nan) ## Initialize the categorical dataset with nan values
    
    ## fill with categorical data
    intCat_MHWDate = xr.where(ratio >= 3, 4, intCat_MHWDate)
    intCat_MHWDate = xr.where((ratio >= 2) & (ratio < 3), 3, intCat_MHWDate)
    intCat_MHWDate = xr.where((ratio >= 1) & (ratio < 2), 2, intCat_MHWDate)
    intCat_MHWDate = xr.where((ratio >= 0) & (ratio < 1), 1, intCat_MHWDate)
    
    return intCat_MHWDate