def sexof_m(n):
    if n == "Femenino":
        a = 2 
        return a
    else:
        a = 1
        return a

def opciones(n):    
    if n == "Normal":
        a = 1
        return a
    elif n =="Por encima de lo normal":
        a = 2
        return a
    else:
        a = 3
        return a
def opciones(n):    
    if n == "Normal":
        a = 1
        return a
    elif n =="Por encima de lo normal":
        a = 2
        return a
    else:
        a = 3
        return a
    
def si_no(r):
    if r == "Si":
        b = 1
        return b
    else:
        b = 0
        return b

def resultados_finales(i):
    if i == 0:
        return "Es probable que **no tenga** riesgo de una enfermedad cardiovascular"
    else:
        return "Es probable que *tenga* riesgo de una enfermedad cardiovascular"