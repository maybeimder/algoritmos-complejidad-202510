digits = [str(i) for i in range(9)]
signs = ["+", "-"]

def base (entry: str, cc: int = 0):
    if cc == len(entry):
        return f"la cadena '{entry}' es rechazada."
    
    if entry[cc] in digits:
        return digit(entry, cc+1)
    elif entry[cc] == ".":
        return point(entry, cc+1)
    elif entry[cc] in signs:
        return sign(entry, cc+1)
    elif entry[cc].upper() == "E":
        return exponent(entry, cc+1)
    else:
        return error(entry)

def digit (entry: str, cc: int):
    if cc == len(entry):
        return f"la cadena '{entry}' es aceptada."
    
    if entry[cc] in digits:
        return digit(entry, cc+1)
    elif entry[cc] == ".":
        return point(entry, cc+1)
    elif entry[cc].upper() == "E":
        return exponent(entry, cc+1)
    else:
        return error(entry)

def point (entry: str, cc: int):
    if cc == len(entry):
        return f"la cadena '{entry}' es aceptada."
    
    if entry[cc] in digits:
        return digit(entry, cc+1)
    elif entry[cc].upper() == "E":
        return exponent(entry, cc+1)
    else:
        return error(entry)

def exponent (entry: str, cc: int):
    if cc == len(entry):
        return f"la cadena '{entry}' es aceptada."
    
    if entry[cc] in digits:
        return e_digit(entry, cc+1)
    elif entry[cc] in signs:
        return e_sign(entry, cc+1)
    else:
        return error(entry)
    
def sign (entry: str, cc: int):
    if cc == len(entry):
        return f"la cadena '{entry}' es aceptada."
    
    if entry[cc] in digits:
        return digit(entry, cc+1)
    elif entry[cc] == ".":
        return point(entry, cc+1)
    elif entry[cc].upper() == "E":
        return exponent(entry, cc+1)
    else:
        return error(entry)
    
def e_digit (entry: str, cc: int):
    if cc == len(entry):
        return f"la cadena '{entry}' es aceptada."
    
    if entry[cc] in digits:
        return e_digit(entry, cc+1)
    else:
        return error(entry)

def e_sign (entry: str, cc: int):
    if cc == len(entry):
        return f"la cadena '{entry}' es aceptada."
    
    if entry[cc] in digits:
        return e_digit(entry, cc+1)
    else:
        return error(entry)
    
def error(entry):
    return f"La cadena '{entry}' se encuentra en un formato no válido."

if __name__ == "__main__":
    test = ["1.23e+10", "-4.56e-3", "7.89",
    "+0.001", "3e8", "-2e+5", "6.022e23",
    "9.81e0", "1.0e-10", "0.0001", "123e",
    "e10", "1.2.3", "++5.6", "--7.8", "3.14e+",
    "-e-5", "5e-", "1e+1.5", "10e10e10"
    ]
    
    for combination in test:
        print(base(combination))
