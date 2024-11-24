# Convertir logitudes a pies

def feetConverter (lengthCurrent: str, value: float):
    
    # Convertir de metros a pies
    if lengthCurrent == "2":
        return round(value * 3.28084, 3)
    
    # Convertir de kilometros a pies
    if lengthCurrent == "3":
        return round(value * 3280.84, 3)

    # Convertir de millas a pies
    if lengthCurrent == "4":
        return round(value * 5280, 3)