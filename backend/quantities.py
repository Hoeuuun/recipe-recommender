from quantulum3 import parser

################################################################################
def parse_quantity(ingredient):
    """
    Extracts the ingredient's quantity

    Parameters
    ----------
    ingredient : str
        An ingredient needed for a recipe

    Returns
    -------
    ingredient_quantity : list
        A list containing the parsed quantity, i.e., the value, unit, entity

    """
    ingredient_quantity = 0

    # try to parse the quantity
    try:
        quant = parser.parse(ingredient)
        # ensure quantity is not empty; otherwise default value is zero
        if (len(quant) > 0):
            # ingredient_quantity = quant[0].surface (1/2 cup)
            ingredient_quantity = quant[0].value    # 0.5
            ingredient_quantity = quant[0].unit.name # cup

    # for now, pass if unable to parse
    except:
        pass    # TODO: optimize quantulum parser

    return ingredient_quantity

################################################################################
def convert_to_mL(value, unit):
    """
    Gets the value and unit of the ingredient, and calls the appropriate
    conversion function to convert it to milliliters (mL)

    Does NOT work with non-volume units (e.g., pound, ounce, "dimensionless")

    Parameters
    ----------
    value : float
        The quantity's value represented as a float
    unit : str
        The quantity's unit of measurement

    Returns
    -------
    mL : float
        The quantity in mL
    """
    if (unit == "ounce" or
        unit == "pound" or
        unit == "gram" or
        unit == "milligram" or
        unit == "dimensionless"):

        mL = "NULL"
        
    elif (unit == "cup"):
        mL = convert_cup(value)

    elif (unit == "tablespoon"):
        mL = convert_tbl(value)

    elif (unit == "teaspoon"):
        mL  = convert_tsp(value)

    elif (unit == "pint"):
        mL  = convert_pt(value)

    elif (unit == "quart"):
        mL  = convert_qt(value)

    elif (unit == "gallon"):
        mL  = convert_gal(value)

    else:
        mL = value

    return mL

################################################################################
"""
Helper functions to convert volume units to milliliters
"""
def convert_cup(value):
    return value * 236.5882365

def convert_tbl(value):
    return value * 14.78676478

def convert_tsp(value):
    return value * 4.92892159

def convert_pt(value):
    return value * 473.176473

def convert_qt(value):
    return value * 946.352946

def convert_gal(value):
    return value * 3785.411784
