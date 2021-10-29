  # -*- coding: utf-8 -*-
'''
@author: eledebar
'''

import csv
from collections import namedtuple 
from parsers import parsing_boolean, parsing_date

Info = namedtuple('Info', 'Age, Gender, Heart_disease, Thyroid_disease, Centimetres_high, Kilograms_weight, Date_of_diagnosis, Physical_activity')            


#----------------------------------------------------------------------------------------------------------------------------
# -- ENTREGA 1
#----------------------------------------------------------------------------------------------------------------------------
def lee_fichero(fichero):
    '''
    Devuelve una lista de tuplas de tipo Info a partir de los datos incluidos en el fichero
    csv dado como parámetro. El fichero debe estar codificado en formato utf-8.
    @param fichero: Nombre y ruta del fichero csv a leer. 
    @type fichero:srt
    @return: Una lista de tuplas de tipo Info con todos los datos del csv
    @rtype: [ Info(int, str, boolean, boolean, int, float, str, str, in, boolean, int,vdatetime.date, str)]  
    '''
    with open(fichero) as f:
        
        lector = csv.reader(f, delimiter=';')
        next(lector)
        res = []
        for Age, Gender, Heart_disease, Thyroid_disease, Centimetres_high, Kilograms_weight, Date_of_diagnosis, Physical_activity in lector:
                         
            tupla = Info(int(Age), Gender, parsing_boolean (Heart_disease), parsing_boolean(Thyroid_disease), int(Centimetres_high), float(Kilograms_weight), \
                         parsing_date(Date_of_diagnosis), Physical_activity)
            res.append(tupla)
    return res   
