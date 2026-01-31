from mhw_statistics import climg_thresh


def anomaly_cont(ds_sst, MHW_date, climY_start, climY_end, MHW_window = 5, thresh = 90, mask = True):
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


