# Import libraries
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from datetime import timedelta

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

    # Get MM-DD dates
    dateBefMMDD = dateBef_str[-6:] # str
    dateAftMMDD = dateAft_str[-6:] # str

    # Define MM-DD
    mmdd_y1 = dateBefMMDD
    mmdd_y2 = dateAftMMDD

    # Define years range
    range_y1 = int(climY_start[:4])
    range_y2 = int(climY_end[:4]) + 1 # Add 1 extra year because range settings

    # Create list of tuples with dates +5 and -5 days during the base period
    listTup_dates = []

    # Iterate and get tuples of dates in the climatology period
    for y in range(range_y1, range_y2):
        if dateBefY != dateAftY: 
            listTup_dates.append((str(y-1)+mmdd_y1, str(y)+mmdd_y2))
        else:
            listTup_dates.append((str(y)+mmdd_y1, str(y)+mmdd_y2))

    return listTup_dates