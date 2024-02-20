import os
import modulos.menu as menu
def menureport(campus: dict):
    isActive =  True
    opciones = ('1.Campers que se encuentren en estado de inscrito\n2.Campers que aprobaron el examen inicial.\n3.Entrenadores trabajando con campuslands.\n4.Estudiantes que cuentan con bajo rendimiento.\n5.Campers y entrenador asociados a una ruta de entrenamiento\n6.Campers aprobados y reprobados\n7.Salir')
    while isActive:
        try:
            os.system('cls')
            print(menu.titulo)
            print(opciones)
            op = int(input(':)_ '))
            if (op == 1):
                inscrito(campus)
            elif (op == 2):
                pruebaacces(campus)
            elif (op == 3):
                listtriners(campus)
            elif (op == 4):
                lowrendimiento(campus)
            elif (op == 5):
                salones(campus)
            elif (op == 6):
                aprbo(campus)
            elif (op == 7):
                isActive = False
                return
            else:
                print('Numero no encontrado')
                os.system('pause')
                menureport(campus)
        except ValueError:
            print('Error de escritura')
            os.system('pause')
            menureport(campus)

def inscrito(campus : dict):
    os.system('cls')
    print(menu.titulo)
    for item in campus['campers']:
        print(f'El camper {item} esta inscrito ')
    print('Estos son los estudiantes inscritos')
    os.system('pause')
    return

def pruebaacces(campus:dict):
    os.system('cls')
    for item in campus['campers']:
        for i in campus['campers']['estado']:
            if campus['campers']['estado']['status'] == 'Aprobado':
                print(f'El estudiante {item} aprobó la prueba de acceso')
        print('Estos son los estudiantes que aprobaron y reprobaron la prueba de accesl')
        os.system('pause')
        return

def listtriners(campus:dict):
    os.system('çls')
    print(menu.titulo)
    listrain = list(campus['trainners']['nomtrains'])
    print('Los trainers trabajando con campuslands son')
    print(listrain)
    os.system('pause')
    return

def lowrendimiento(campus:dict):
    print(menu.titulo)
    print('Bienvenido al buscador de estudiantes en zona de riesgo')
    print('Seleccione el modulo en el cual quiere buscar los campers con riesgo')
    try:
        for item in campus['campers']:
            lstmodul = list(campus['campers'][item]['notas'].keys()) 
            print(lstmodul) #el id es variable
            select = str(input(':)_ '))
            for info in campus['campers'][item]['notas'][select].items():
                if campus['campers'][item]['notas'][select]['situacion'] == 'reprobado':
                    print(f'El camper {item} en el modulo {select} esta en bajo rendimiento')
                    os.system('pause')
                    return
    except ValueError:
        print('Dato ingresado no es valido')
        os.system('pause')
        return
    else:
        print('Estos son los campers en riesgo')

def salones(campus:dict):
    os.system('cls')
    print('Bienvenido al reporte de los salones de campus')
    print('Porfavor seleccione el salon el cual desea ver su ruta y el trainer encargado')
    try:
        listsalon = list(campus['areas'])
        print(listsalon)
        salon = str(input(':)_ '))
        if salon in listsalon:
            info = campus['areas'][salon]
            print(info)
            print(f'Esta es la informacion del salon {salon} matricualdo')
            os.system('pause')
        else:
            print('nombre de salon no encontrado')
            os.system('pause')
            salones(campus)
    except ValueError:
        print('Error de digitacion')
        os.system('pause')
        return

def aprbo(campus:dict):
    print(menu.titulo)
    print('Bienvenido al buscador de estudiantes aprobados y reprobados')
    print('Seleccione el modulo en el cual quiere buscar los campers aprobados o desaprobado')
    try:
        for item in campus['campers']:
            lstmodul = list(campus['campers'][item]['notas'].keys()) 
            print(lstmodul) 
            select = str(input(':)_ '))
            for info in campus['campers'][item]['notas'][select].items():
                if campus['campers'][item]['notas'][select]['situacion'] == 'reprobado':
                    print(f'El camper {item} en el modulo {select} fue reprobado')
                elif campus['campers'][item]['notas'][select]['situacion'] == 'aprobado':
                    print(f'El camper {item} en el modulo {select} fue aprobado')
                else:
                    print('El estudiante no ha cursado el modulo o no han registrado notas')
    except ValueError:
        print('Dato ingresado no es valido')
        os.system('pause')
        return
    else:
        print(f'Este ha sido el reporte de los estudiantes aprobados y desaprobados en el modulo {select}')
        os.system('pause')
        return