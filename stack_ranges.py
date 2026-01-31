import xarray as xr
from preliminar.get_dates import get_datesClimg

def stack_ranges(ds_sst, MHW_date, climY_start, climY_end, MHW_window = 5):
    '''
    Stack date ranges from climatology period into a single xarray DataArray.

    Parameters
    ----------
    ds_sst : xarray.Dataset
        Dataset containing sea surface temperature data with a 'time' dimension.
    MHW_date : str
        MHW peak intensity date in "YYYY-MM-DD" format.
    climY_start : int
        Start year for the climatology period.
    climY_end : int
        End year for the climatology period.
    MHW_window : int, optional
        Number of days to add/subtract from the MHW peak intensity date (default is 5).

    Returns
    -------
    xarray.DataArray
        Stacked DataArray containing data from all specified date ranges.
    '''
    
    # Get list of date tuples for climatology period
    listTup_dates = get_datesClimg(MHW_date, MHW_window, climY_start, climY_end)
    
    # Initialize an empty list to hold DataArrays
    list_da = []
    
    # Iterate over each date tuple and extract corresponding data
    for date_start, date_end in listTup_dates:
        da_range = ds_sst.sel(time=slice(date_start, date_end)).sst # INCLUDE VARIABLE CHECK
        list_da.append(da_range)
    
    # Concatenate all DataArrays along the time dimension
    stacked_da = xr.concat(list_da, dim="time") # INCLUDE VARIABLE CHECK
    
    return stacked_da