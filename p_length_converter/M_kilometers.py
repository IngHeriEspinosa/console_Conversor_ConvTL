# Convertir logitudes a kilometros

def kilometerConverter (lengthCurrent: str, value: float):

    # Convertir de pies a kilometros
    if(lengthCurrent == "1"):
        return round(value * 0.0003048, 3)
    
    # Convertir de metros a kilometros
    if(lengthCurrent == "2"):
        return round(value * 0.001, 3)

    # Convertir de millas a kilometros
    if(lengthCurrent == "4"):
        return round(value * 1.6093, 3)
