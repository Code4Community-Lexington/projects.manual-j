from ..dao.types import *


# four walls and a roof in the winter (no floor)
def calculate_winter_j(
        location_weather: LocationWeather,
        winter_surfaces: list[tuple[WinterSurface, AreaSquareFeet]]
):
    temperature_loss_btus_per_hour = 0
    # TODO: no magic numbers
    temperature_delta = 70 - location_weather.winter_design_temperature_fahrenheit
    for surface in winter_surfaces:
        temperature_loss_btus_per_hour += surface[0].get_heat_transfer_multiplier(temperature_delta) * surface[1]
    return temperature_loss_btus_per_hour
