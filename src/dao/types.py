type AreaSquareFeet = float
type City = str
type DailyTemperatureRangeFahrenheit = int
type DailyRangeClass = str  # change this to an enum ('L', 'M', 'H')
type HeatTransferCoefficient = float
type HeatTransferMultiplier = float
type Modifier = str
type State = str  # change this to an enum
type SummerDesignTemperatureFahrenheit = int
type SummerHumidityDeltaMax = int
type SummerHumidityDeltaMin = int
type Surface = str
type WinterDesignTemperatureFahrenheit = int

type ExternalShade = float  # range 0..1
type IsSkyLight = bool
type Tint = str  # enum ('CLEAR', 'TINTED', 'REFLECTIVE')
type InternalShade = str
type PaneClass = str
type Direction = str  # enum ('N', 'NW', 'W', 'SW', 'S', 'SE', 'E', 'NE')


# table 1
class LocationWeather:
    def __init__(
            self,
            state: State,
            city: City,
            winter_design_temperature_fahrenheit: WinterDesignTemperatureFahrenheit,
            summer_design_temperature_fahrenheit: SummerDesignTemperatureFahrenheit,
            summer_humidity_delta_min: SummerHumidityDeltaMin,
            summer_humidity_delta_max: SummerHumidityDeltaMax,
            daily_temperature_range_fahrenheit: DailyTemperatureRangeFahrenheit,
            daily_range_class: DailyRangeClass
    ):
        self.state = state
        self.city = city
        self.winter_design_temperature_fahrenheit = winter_design_temperature_fahrenheit
        self.summer_design_temperature_fahrenheit = summer_design_temperature_fahrenheit
        self.summer_humidity_delta_min = summer_humidity_delta_min
        self.summer_humidity_delta_max = summer_humidity_delta_max
        self.daily_temperature_range_fahrenheit = daily_temperature_range_fahrenheit
        self.daily_range_class = daily_range_class


# table 2
class WinterSurface:
    def __init__(
            self,
            surface: Surface,
            modifiers: list(Modifier),
            heat_transfer_multipliers: list(HeatTransferMultiplier),
            heat_transfer_coefficient: HeatTransferCoefficient
    ):
        self.surface = surface,
        self.modifiers = modifiers,
        self.heat_transfer_multipliers = heat_transfer_multipliers,
        self.heat_transfer_coefficient = heat_transfer_coefficient

    def get_heat_transfer_multiplier(self, temperature_delta: float) -> float:
        pass

# table 3
type SummerSurfaceGlass = tuple[
ExternalShade,
IsSkyLight,
Tint,
InternalShade,
PaneClass,
Direction,
list(HeatTransferMultiplier)
]

# table 4
type SummerSurface = tuple[
Surface,
list(Modifier),
DailyRangeClass,
list(HeatTransferMultiplier),
HeatTransferCoefficient
]
