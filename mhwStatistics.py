from mhwAux import stackRanges

def climgMean(ds_sst, MHW_date, climY_start, climY_end, MHW_window):
    
    return stackRanges(ds_sst, MHW_date, climY_start, climY_end, MHW_window).mean(dim="time")

def climgThresh(ds_sst, MHW_date, climY_start, climY_end, MHW_window, thresh):
    
    return stackRanges(ds_sst, MHW_date, climY_start, climY_end, MHW_window).quantile(thresh, dim="time")

def climgDiff(ds_sst, MHW_date, climY_start, climY_end, MHW_window, thresh):

    mean = climgMean(ds_sst, MHW_date, climY_start, climY_end, MHW_window)
    thresh = climgThresh(ds_sst, MHW_date, climY_start, climY_end, MHW_window, thresh)

    return thresh - mean