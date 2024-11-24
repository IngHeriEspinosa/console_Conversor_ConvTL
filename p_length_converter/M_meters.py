# Convertir logitudes a metros

def meterConverter (lengthCurrent: str, value: float):

    # Convertir de pies a metros
    if(lengthCurrent == "1"):
        return round(value * 0.3048, 3)
    
    # Convertir de kilometros a metros
    if(lengthCurrent == "3"):
        return round(value * 1000, 3)

    # Convertir de millas a metros
    if(lengthCurrent == "4"):
        return round(value * 1609.34, 3)
