# car_creator.py
import pandas as pd

def make_car(fabricante, modelo, **info):
    result = {'fabricante': fabricante, 'modelo': modelo}
    for key, value in info.items():
        result[key] = value
    return result
