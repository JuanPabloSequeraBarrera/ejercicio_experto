import os
lstopciones = [1,2,3,4,5,6]
titulo = """
    ++++++++++++++++++++++++++++
    +Base de datos campus lands+
    ++++++++++++++++++++++++++++
"""
opciones = ('1.Registro de campers\n2.Menu administrativo\n3.Zona trainers\n4.Gestor de matriculas\n5.Reportes\n6.Salir')
def menu():
    os.system('cls')
    print(titulo)
    print(opciones)
    try:
       op = int(input(':)_ '))
       if not (op in lstopciones):
            print('Valor ingresado no valido')
            os.system('pause')
            menu()
    except ValueError:
        print('error de digitacion')
        os.system('pause')
        menu()
    else:
        return op