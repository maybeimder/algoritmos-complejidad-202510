def base(entry: str, cc: int = 0):
    if cc == len(entry):
        return f"La cadena '{entry}' es rechazada."
    
    match entry[cc]:
        case "I":
            return I(entry, cc+1)
        case "V":
            return V(entry, cc+1)
        case "X":
            return X(entry, cc+1)
        case "L":
            return III(entry, cc+1)
        case _:
            return error(entry)
        
def I(entry: str, cc: int):
    if cc == len(entry):
        return f"La cadena '{entry}' es aceptada."
    
    match entry[cc]:
        case "I":
            return II(entry, cc+1)
        case "V":
            return III(entry, cc+1)
        case "X":
            return III(entry, cc+1)
        case _:
            return error(entry)

def II(entry: str, cc: int):
    if cc == len(entry):
        return f"La cadena '{entry}' es aceptada."
    
    match entry[cc]:
        case "I":
            return III(entry, cc+1)
        case _:
            return error(entry)

def III(entry: str, cc: int):
    if cc == len(entry):
        return f"La cadena '{entry}' es aceptada."
    
    return error(entry)

def V(entry: str, cc: int):
    if cc == len(entry):
        return f"La cadena '{entry}' es aceptada."
    
    match entry[cc]:
        case "I":
            return I(entry, cc+1)
        case _:
            return error(entry)

def X(entry: str, cc: int):
    if cc == len(entry):
        return f"La cadena '{entry}' es aceptada."
    
    match entry[cc]:
        case "I":
            return I(entry, cc+1)
        case "V":
            return V(entry, cc+1)
        case "X":
            return XX(entry, cc+1)
        case "L":
            return XXX(entry, cc+1)
        case _:
            return error(entry)

def XX(entry: str, cc: int):
    if cc == len(entry):
        return f"La cadena '{entry}' es aceptada."
    
    match entry[cc]:
        case "I":
            return I(entry, cc+1)
        case "V":
            return V(entry, cc+1)
        case "X":
            return XXX(entry, cc+1)
        case _:
            return error(entry)

def XXX(entry: str, cc: int):
    if cc == len(entry):
        return f"La cadena '{entry}' es aceptada."
    
    match entry[cc]:
        case "I":
            return I(entry, cc+1)
        case "V":
            return V(entry, cc+1)
        case _:
            return error(entry)
        
def error(entry):
    return f"La cadena '{entry}' se encuentra en un formato no válido."

if __name__ == "__main__":
    
    roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
    "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX",
    "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL",
    "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L"
    "IIII",     # IV es el correcto
    "VV",       # V no se repite
    "IC",       # No se puede restar I de C
    "IL",       # No se puede restar I de L
    "VX",       # V no puede preceder a X
    "LC",       # L no puede preceder a C
    "DM",       # D no puede preceder a M
    "XM",       # X no puede preceder a M
    "IIIIII",   # Repetición excesiva de I
    "ABC",      # Letras no válidas
    "XVV",      # V no se repite
    "MCMC",     # Orden incorrecto
    "IXX",      # I no puede preceder a XX
    "LL",       # L no se repite
    "CMM"       
    ]
    
    for num in roman:
        print(base(num))