import os
import modulos.menu as menu
def Addcamper (campers : dict):
    os.system('cls')
    try:
        print(menu.titulo)
        print('Bienvenido al registro camper, por favor ingrese sus datos')
        print('Digite su T.I o numero de id')
        id = int (input(':)_ '))
        print('Digite su nombre')
        nombre = str (input(':)_ '))
        print('Digite sus o su apellido')
        apellido = str (input(':)_ '))
        print('Digite su direccion')
        direccion = (input(':)_ '))
        print('Inserte su numero de telefono')
        tel = int (input(':)_ '))
        camper = {
            'id' : id,
            'nombre' : nombre,
            'apellido': apellido,
            'direccion' : direccion,
            'telefono' : tel,
            'estado' : {
                'teorico1': 0, 
                'practico1':0,
                'promedio1':0,
                'status':0
            }, 
            'notas' :{ 
                'modulofundamentos':{
                    'practico':0,
                    'teorico': 0,
                    'notaclase': 0,
                    'definitiva': 0,
                    'situacion': 0
                },
                'moduloweb':{
                    'practico':0,
                    'teorico': 0,
                    'notaclase': 0,
                    'definitiva':0,
                    'situacion':0
                },
                'moduloformal':{
                    'practico':0,
                    'teorico': 0,
                    'notaclase':0,
                    'definitiva':0,
                    'situacion':0
                },
                'modulobd':{
                    'practico':0,
                    'teorico': 0,
                    'notaclase':0,
                    'definitiva': 0,
                    'situacion': 0
                },
                'modulobackend':{
                    'practico':0,
                    'teorico':0,
                    'notalcase':0,
                    'definitiva': 0,
                    'situacion': 0
                }
            }
        }
        print('Cuantos acudientes desea registrar?')
        a = int (input(':)_ '))
        camper['acudiente(s)'] = {}
        for i in range (1, a+1):
            print('Ingrese el nombre de su acudiente')
            nombre1 = str (input(':)_ ')).upper()
            print(f'Ingrese el telefono del acuidente {nombre1}')
            telacu =  int (input(':)_ '))
            camper['acudiente(s)'][nombre1] ={
                'nombre' : nombre1,
                'telefonoa': telacu   
            }
        campers.update({id:camper})
    except ValueError:
        print('Dato no valido')
        os.system('pause')
        return
    else:
        print('camper registrado correctamente')
        print('Desea agregar otro camper?')
        dec = input(':)_ ').upper()
        if (dec == 'SI'):
            Addcamper(campers)
        else: 
          os.system('pause')