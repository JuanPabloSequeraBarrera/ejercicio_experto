import os 
import modulos.menu as menu
def menuadmin(campus : dict):
    os.system('cls')
    opciones = ('1.Registro de prueba inicial campers\n2.Rutas de entrenamiento y salones\n3.Asignacion de campers\n4.Notas de campers\n5. Estudiantes en riesgo\n6.Volver a menu inicial')
    isActive = True
    while isActive:
        os.system('cls')
        print(menu.titulo)
        print('Bienvenido al menu administrativo de Campuslands')
        print(opciones)
        try:
            op = int(input(':)_ '))
            if (op == 1):
                registprueba1(campus)
            elif (op == 2):
                rutatrain(campus) 
                assigclass(campus)
            elif (op == 3):
                assigcamper(campus)
            elif (op == 4):
                notascampers(campus)
            elif (op == 5):
                estudiantesriesgo(campus)
            elif (op == 6):
                isActive = False
                return
            else:
                print('Numero no valido')
                os.system('pause')
                menuadmin(campus)
        except ValueError:
            print('Dato invalido')
            os.system('pause')
            menuadmin(campus)

def registprueba1(campus : dict):
    os.system('cls')
    print(menu.titulo)
    print('Bienvenido usuario administrativo')
    print('Seleccione el ID del camper al cual quiere registrar sus notas de examen inical')
    listcamp = list(campus['campers'].keys())
    print(listcamp)
    try:
        select = int(input(':)_ '))
        if (select in listcamp):
            print('Ingrese la nota del examen teorico')
            teoric = int(input(':)_ '))
            print('Ingrese la nota del examen practico')
            practic = int(input(':)_ '))
            campus['campers'][select]['estado']['teorico1'] = teoric
            campus['campers'][select]['estado']['practico1'] = practic
            prom = ((teoric+practic)/2)
            campus['campers'][select]['estado']['promedio1'] = prom
            if (prom >= 60):
                campus['campers'][select]['estado']['status'] = 'Aprobado'
                print(f'El estudiante con id {select} ha sido aprobado con un promedio de notas de {prom}')
                os.system('pause')
            else:
                campus['campers'][select]['estado']['status'] = 'Reprobado'
                print(f'El estudiante con id {select} ha sido reprobado con un promedio de notas de {prom}')
                os.system('pause')
        else:
            print(f'El camper con id {select} no ha sido aun inscrito')
            os.system('pause')
            return
    except ValueError:
        print('Dato ingresado no es valido')
        os.system('pause')
        registprueba1(campus)
    else: 
        print('El estado del camper ha sido correctamente modificado')
        os.system('pause')
        return
def rutatrain(campus : dict):
    os.system('cls')
    print(menu.titulo)
    print('Bienvenido usuario administrativo')
    print('Seleccione la ruta de entrenamiento la cual quiere actualizar')
    listtrain = list(campus['rutas'].keys())
    print(listtrain)
    try: 
        select = str(input(':)_ ')).lower()
        if (select in listtrain):
            print(f'Ingrese los stacks tecnologicos de fundamentos que se veran en {select} ')
            fun = str(input(':)_ '))
            print(f'Ingrese los stacks tecnologicos webs que se veran en {select}')
            web = str(input(':)_ '))
            print(f'Ingrese los stacks teconologicos formales que se veran en {select}')
            formal = str(input(':)_ '))
            print(f'Ingrese los stacks teconologicos de bd que se veran en {select}')
            bd = str(input(':)_ '))
            print(f'Ingrese los stacks teconologicos de backend que se veran en {select}')
            backend = str(input(':)_ '))
            campus['rutas'][select]['fundamentos'] = fun
            campus['rutas'][select]['web'] = web            
            campus['rutas'][select]['lengformal'] = formal
            campus['rutas'][select]['bd'] = bd
            campus['rutas'][select]['backend'] = backend
        else:
            print('Ruta no registrada')
            os.system('pause')
            return
    except ValueError:
        print('Dato invalido')
        os.system('pause')
        return
    else:
        print(f'La ruta de entreanmiento de {select} ha sido actualizada con exito')
        print('Desea registrar actualizar otra ruta de entrenamiento? Si(SI), No(NO)')
        dec = str(input(':)_ ')).upper()
        if (dec == 'NO'):
            return
        else:
            rutatrain(campus)
        
def assigclass(campus: dict):
    os.system('cls')
    print(menu.titulo)
    print('Bienvenido usuario Administrativo a la asignacion de clases')
    print('Seleccione la ruta que quiere asignar a alguno de los salones')
    listrut = list(campus['rutas'].keys())
    print(listrut)
    try:
        rut = input(':)_ ').lower()
        if (rut in listrut):
            print(f'Seleccione el salon al cual quiere asignar la ruta {rut}')
            listclass = list(campus['areas'].keys())
            print(listclass)
            salon = input(':)_ ')
            if (salon in listclass):
                campus['areas'][salon]['ruta'] = campus['rutas'][rut]
            else:
                print('Salon no encontrado')
                os.system('pause')
                assigclass(campus)
        else:
            print('Ruta escrita no encontrada')
            os.system('pause')
            assigclass(campus)
    except ValueError:
        print('Valor ingresado no valido')
        os.system('pause')
        return
    else:
        print('La asignacion de ruta en la clase ha sido realizada con exito')
        os.system('pause')
        return

def assigcamper(campus: dict):
    os.system('cls')
    print(menu.titulo)
    print('Bienvendio usuario Administrativo a la asignacion de campus a las clases')
    print('Seleccione el salon al que quiere agregar el estudiante')
    try:
        listclass = list(campus['areas'].keys())
        print(listclass)
        salon = str(input(':)_ ')).lower()
        print('Seleccione el estudiante que quiera ingresar')
        listcampers = list(campus['campers'].keys())
        print(listcampers)
        estudiante = int(input(':)_ '))
        if not (estudiante in campus['areas'][salon]['capacidad']):
            if campus['areas'][salon]['noestudiante'] <= 33:
                if (campus['campers'][estudiante]['estado']['status'] == 'Aprobado'):
                    campus['areas'][salon]['capacidad'] = campus['campers'][estudiante]
                    campus['areas'][salon]['noestudiante'] =+ 1
                else:
                    print('el estudiante fue reprobado en la prueba de acceso')
                    os.system('pause')
                    return
            else:
                print('El salon ya esta lleno de estudiantes')
                os.system('pause')
                assigcamper(campus)
        else:
            print('El estudiante ya fue agregado en un salon de clases')
            os.system('pause')
            return
    except ValueError:
        print('Valor ingresado invalido')
        os.system('pause')
        return
    else: 
        print(f'El estudiante {estudiante} fue agregado al salon {salon}')
        os.system('pause')
        return
def notascampers(campus: dict):
    os.system('cls')
    print(menu.titulo)
    try:
        print('Bienvenido al gestor de notas de los campers')
        print('Ingrese el camper al cual quiere registrar una nota')
        listcamp = list(campus['campers'].keys())
        print(listcamp)
        camp = int(input(':)_ '))
        if (camp in listcamp):
            print(f'Seleccione el modulo al cual quiere asignar las notas de {camp} ')
            listmodul = list(campus['campers'][camp]['notas'].keys())
            print(listmodul)
            asignar = str(input(':)_ ')).lower()
            if (asignar in listmodul):
                print(f'Que nota quiere asignar al examen practico de {camp}')
                practico = int(input(':)_ '))
                print(f'Que nota quiere asignar al examen teorico de {camp}')
                teorico = int(input(':)_ '))
                print(f'Que nota quiere asignar a las notas de clase de {camp}')
                notcalse = int(input(':)_ '))
                campus['campers'][camp]['notas'][asignar]['practico'] = practico
                campus['campers'][camp]['notas'][asignar]['teorico'] = teorico
                campus['campers'][camp]['notas'][asignar]['notaclase'] = notcalse
                definitivo = (practico*0.6) + (teorico*0.3) + (notcalse*0.1)
                campus['campers'][camp]['notas'][asignar]['definitiva'] = definitivo
                if definitivo > 60:
                    campus['campers'][camp]['notas'][asignar]['situacion'] = 'aprobado'
                    print('El estudiante pasó satisfactoriamente el modulo')
                else:
                    campus['campers'][camp]['notas'][asignar]['situacion'] = 'reprobado'
                    print('El estudiante no pasó el modulo satisfactoriamente')
            else:
                print('modulo no encontrado')
                os.system('pause')
                notascampers(campus)
        else:
            print('Camper no registrado aun')
            os.system('pause')
            return
    except ValueError:
        print('Error en el dato digitado')
        os.system('pause')
        return
    else:
        print(f'Las notas del camper {camp} han sido actualizadas')
        os.system('pause')

def estudiantesriesgo (campus : dict):
    print(menu.titulo)
    print('Bienvenido al buscador de estudiantes en zona de riesgo')
    print('Seleccione el modulo en el cual quiere buscar los campers con riesgo')
    lstmodul = list(campus['campers']['id']['notas'].keys()) #necesito que me imprima todas las llaves de los modulos, pero como son todos los campers
    print(lstmodul) #el id es variable
    select = str(input(':)_ '))
    for camper, info in campus['campers'].items():
        if 'situacion' in info['notas'][select] and info['notas'][select]['situacion'] == 'reprobado':
            print(f'camper:{campus["campers"]}')