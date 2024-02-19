import os
import modulos.menu as menu
import modulos.campers as camp
import modulos.admin as admin
import modulos.trainers as t
import modulos.matriculas as m
campus ={
    'campers':{},
    'rutas':{
        'java':{
            'trainer': 0,
            'fundamentos':0,
            'web':0,
            'lengformal':0,
            'bd':0,
            'backend':0,
            'fecha_inicio':0,
            'fecha_fin': 0
        },
        'nodejs':{
            'trainer': 0,
            'fundamentos':0,
            'web':0,
            'lengformal':0,
            'bd':0,
            'backend':0,
            'fecha_inicio':0,
            'fecha_fin': 0
        },
        'netcore':{
            'trainer':0,
            'fundamentos':0,
            'web':0,
            'lengformal':0,
            'bd':0,
            'backend':0,
            'fecha_inicio':0,
            'fecha_fin': 0
        }
    },
    'areas':{
        'apolo':{
            'nombre': 'apolo',
            'capacidad': {}, #33
            'ruta': {},
            'noestudiante':0
        },
        'artemis':{
            'nombre': 'artemis',
            'capacidad': {}, #33
            'ruta': {},
            'noestudiante':0
        },
        'sputnik':{
            'nombre': 'sputnik',
            'capacidad': {}, #33
            'ruta': {},
            'noestudiante': 0
        }
    },
    'trainners':{},
    'matriculas':{},
}
isActive = True
while isActive:
    os.system('cls')
    opciones = menu.menu()
    if (opciones == 1):
        camp.Addcamper(campus.get('campers'))
    elif (opciones == 2):
        admin.menuadmin(campus)
    elif (opciones == 3):
        t.zonatrainers(campus)
    elif (opciones == 4):
        m.gestormatriculas(campus)
    elif (opciones ==5): 
        pass
    elif (opciones == 6):
        isActive = False
        print('Muchas gracias por hacer uso del software')