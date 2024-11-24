# Convertir temperatura a Celsius

def celsiusConverter(tempCurrent: str, value: float) -> str:
    # Conversion de Fahrenheit a Celsius
    if tempCurrent == "2":
        value = value - 32
        transformation = value * 0.5556
        return round(transformation, 2)

    # Conversion de Kelvin a Celsius
    if(tempCurrent == "3"):
        transformation = value - 273.15
        return round(transformation, 2)
    