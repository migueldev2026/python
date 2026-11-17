"""Functions to help the company calculate their power usage."""


def get_extra_hours(hours):
    """Return the number of hours.

    :param: hours: int - number of hours.
    :return: int - number of "extra" hours.
    """
    rest= hours % 24
    if rest == 21:
        return 0
    else:
        return rest+3


def get_kW_amount(watts):
    """Return the kW amount of a given watt amount.

    :param: watts: int - watt amount.
    :return: float - kW amount.
    """
    answer = watts / 1000
    return round(answer, 1)

def get_kwh_amount(watts):
    """Return the kWh amount of a given watt amount and hours.

    :param: watts: int - watt amount.
    :return: int - kilowatt hour amount.
    """
    get_kW = get_kW_amount(watts)
    return get_kW//3600


def get_efficiency(power_factor):
    """Return the efficiency calculated from the power factor.

    :param: power_factor: float.
    :return: float - efficiency.
    """
    return power_factor/ 100


def get_cost(watts, power_factor, price):
    """Calculate the cost of a given kWh value, efficiency and price.

    :param: watts: int - watt value.
    :param: power_factor: float - efficiency.
    :param: price: float - price of kWh.
    :return: float - cost of kWh.
    """
    efeficiency = get_efficiency(power_factor)
    kwh_amount = get_kwh_amount(watts)
    return (kwh_amount * price)/efeficiency 
