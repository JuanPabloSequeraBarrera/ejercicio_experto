import os 
import modulos.menu as menu
def gestormatriculas (campus : dict):
    os.system('cls')
    print(menu.titulo)
    print('Bienvenido al gestor de matriculas de campus')
    print('Porfavor seleccione la ruta a la cual quiere registrar las fechas de inicio y terminacion')
    try:
        listrut = list(campus['rutas'].keys())
        print(listrut)
        rutaselect = str(input(':)_ '))
        if (rutaselect in listrut):
            print('Escirba la fecha de inicio en formato DD/MM/YYY')
            inicio = (input(':)_ '))
            print('Escirba la fecha de finalizacion en formato DD/MM/YYY')
            fin = (input(':)_ '))
            campus['rutas'][rutaselect]['fecha_inicio'] = inicio
            campus['rutas'][rutaselect]['fecha_fin'] = fin
        else:
            print('ruta seleccionada no encontrada')
            os.system('pause')
            return
    except ValueError:
        print('error en la validacion de datos')
        os.system('pause')
        return
    else:
        print('Se han ingresado con exito las fechas del curso')
        os.system('pause')
        return