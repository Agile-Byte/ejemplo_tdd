# -*- coding: utf-8 -*-
"""Funciones"""
import pandas as pd


def hello_world():
    return "hello world"

def super():
    return "super "

def super_hello_world():
    first = super()
    second = hello_world()
    return first + second

def super_super_hello_world():
    first = super()
    second = super()
    third = hello_world()
    return first+second+third

def super_super_whatever():
    first = super()
    second = super()
    third = whatever()
    return first+second+third

def whatever():
    query = 'select * from tabla_parametrizacion'

    #resultado = haz_consulta(query)

    df = pd.read_excel(io=r'/home/gondaviza/Escritorio/agilebyte/ejemplo_tdd/src/extras/ejemplo_TDD.xlsx')
    resultado = df.valor[0]
    return resultado
    #return 'fail'


res = super_super_whatever()