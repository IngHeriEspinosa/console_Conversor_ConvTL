# Convertir logitudes a millas

def milesConverter (lengthCurrent: str, value: float):

    # Convertir de pies a millas
    if(lengthCurrent == "1"):
        return round(value * 0.00018939, 3)
    
    # Convertir de metros a millas
    if(lengthCurrent == "2"):
        return round(value * 0.00062137, 3)

    # Convertir de kilometros a millas
    if(lengthCurrent == "3"):
        return round(value * 0.621371, 3)
