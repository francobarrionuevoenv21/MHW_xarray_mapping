# LIBRARIES
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from datetime import timedelta
import xarray as xr

# FUNCTIONS

def get_datesWindow(date_str, window):
    """
    Compute a symmetric date window around a reference date.

    Parameters
    ----------
    date_str: str
        MHW peak intensity date in "YYYY-MM-DD" format
    window: int
        Number of days to add/subtract from the MHW peak intensity date

    Returns
    -------
    d_minus & d_plus : str
        Date corresponding to (date_str -/+ window days), in "YYYY-MM-DD" format.
    """
    d = dt.strptime(date_str, "%Y-%m-%d")
    d_minus = (d - timedelta(days=window)).strftime("%Y-%m-%d")
    d_plus  = (d + timedelta(days=window)).strftime("%Y-%m-%d")
    return d_minus, d_plus

# Function to get dates for climatology computing 
def get_datesClimg(date_str, window, climY_start, climY_end):
    '''
    Docstring for get_datesClimg
    
    :param date_str: Description
    :param window: Description
    :param climY_start: Description
    :param climY_end: Description
    '''

    # Get before and after MHW dates & Save them
    dateBef_str, dateAft_str = get_datesWindow(date_str, window)

    # Get year dates
    dateBefY = int(dateBef_str[:4]) # int
    dateAftY = int(dateAft_str[:4]) # int

    # Get and define MM-DD dates
    mmdd_y1 = dateBef_str[-6:] # str
    mmdd_y2 = dateAft_str[-6:] # str

    # Define years range
    range_y1 = climY_start
    range_y2 = climY_end + 1 # Add 1 extra year due to range() settings

    # Create list of tuples with dates +5 and -5 days during the base period
    listTup_dates = []

    # Iterate and get tuples of dates in the climatology period
    for y in range(range_y1, range_y2):
        if dateBefY != dateAftY: 
            listTup_dates.append((str(y-1)+mmdd_y1, str(y)+mmdd_y2))
        else:
            listTup_dates.append((str(y)+mmdd_y1, str(y)+mmdd_y2))

    return listTup_dates

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


def open_sst(file_path):
    '''
    Open SST dataset from a NetCDF file.

    Parameters
    ----------
    file_path : str
        Path to the NetCDF file containing SST data.

    Returns
    -------
    xarray.Dataset
        Dataset containing sea surface temperature data.
    '''

    try:
        ds_sst = xr.open_dataset(file_path)
    
    if "sst" not in ds_oisst:
        raise KeyError(
            f"Variable 'sst' not found in dataset. \n"
            "Update to use 'sst' as variable name for sea surface temperature data."
        )
    elif "time" not in ds_oisst:
        raise KeyError(
            f"Variable 'time' not found in dataset. \n"
            "Ensure the dataset contains a 'time' dimension."
            )

    return ds_sst