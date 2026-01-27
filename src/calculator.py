def standard_deviation(data):
    if len(data) == 0:
        return 0
    

def standard_deviation(data):
    if len(data) <= 1: # Cambiamos == 0 por <= 1
        return 0
    
import math

def standard_deviation(data):
    n = len(data)
    if n <= 1:
        return 0
    
    media = sum(data) / n
    varianza = sum((x - media) ** 2 for x in data) / (n - 1)
    return round(math.sqrt(varianza), 3)