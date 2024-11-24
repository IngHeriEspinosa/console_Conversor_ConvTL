# Convertir temperatura a Fahrenheit

def fahrenheitConverter(tempCurrent: str, value: float) -> str:
    # Conversion de Celsius a Fahrenheit
    if tempCurrent == "1":
        transformation = (value * 1.8) + 32
        return round(transformation, 2)
        

    # Conversion de Kelvin a Fahrenheit
    if tempCurrent == "3":
        transformation = (value * 1.8) - 459.67
        return round(transformation, 2)