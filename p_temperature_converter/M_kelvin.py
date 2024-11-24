# Convertir temperatura a Kelvin

def kelvinConverter(tempCurrent: str, value: float) -> str:
    # Conversion de Celsius a Kelvin
    if tempCurrent == "1":
        transformation = value + 273.15
        return round(transformation, 2)

    # Conversion de Fahrenheit a Kelvin
    if(tempCurrent == "2"):
        transformation = (value + 459.67) / 1.8
        return round(transformation, 2)