import os 
import modulos.menu as menu
def zonatrainers(campus : dict):
    os.system('cls')
    print(menu.titulo)
    print('Bienvendio usuario a zona trainer, porfavor indique su nombre')
    try:
        nombre = str(input(':)_ '))
        campus['trainners']['nomtrains'].append(nombre)
        print('Seleccione la ruta de entrenamiento que desea dirigir')
        listrutas = list(campus['rutas'].keys())
        print(listrutas)
        selcrut = str(input(':)_ ')).lower()
        if (selcrut in listrutas):
            campus['rutas'][selcrut]['trainer'] = nombre
        else:
            print('ruta no encontrada')
            os.system('pause')
            return
    except ValueError:
        print('Dato invalido')
        os.system('pause')
        return
    else:
        print(f'El trainer {nombre} ha sido asignado a la ruta {selcrut}')
        os.system('pause')
        return