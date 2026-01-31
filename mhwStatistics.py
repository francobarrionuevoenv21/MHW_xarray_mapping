from mhwAux import stack_ranges

def climg_mean(ds_sst, MHW_date, climY_start, climY_end, MHW_window = 5):
    
    return stack_ranges(ds_sst, MHW_date, climY_start, climY_end, MHW_window).mean()

def climg_thresh(ds_sst, MHW_date, climY_start, climY_end, MHW_window = 5, thresh = 90):
    
    return stack_ranges(ds_sst, MHW_date, climY_start, climY_end, MHW_window).quantile(thresh/100, dim="time")

def climg_diff(ds_sst, MHW_date, climY_start, climY_end, MHW_window = 5, thresh = 90):

    mean = climg_mean(ds_sst, MHW_date, climY_start, climY_end, MHW_window = 5)
    thresh = climg_thresh(ds_sst, MHW_date, climY_start, climY_end, MHW_window, thresh)

    return mean - thresh