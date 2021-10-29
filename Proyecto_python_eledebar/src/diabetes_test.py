  # -*- coding: utf-8 -*-
from diabetes import lee_fichero


def test_lee_fichero(fichero):
    print ("test_lee_fichero" + "="*25)
    lista_tuplas = lee_fichero(fichero)
    print('Leídos', len(lista_tuplas), 'registros.')
    print('Los tres primeros registros son:', lista_tuplas[:3])
    print('Los tres últimos registros son:', lista_tuplas[-3:])

    
def main():
    
    test_lee_fichero('../data/dataset_diabetes.csv')

    
if __name__ == '__main__':
    main()
