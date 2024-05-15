'''
Este codigo permite administrar el stock de los productos en una bodega
'''
import os
productos = {'escoba' : 5, 'huevos' : 10, 'leche' : 8}
menup = ['Ver productos', 'Añadir productos', 'Eliminar productos', 'Ajustar productos', 'Salir']
print ('***************************************************')
print ('**************Administracion de stock**************')
print ('***************************************************')
while True:
    for ind in range(len(menup)):
        print(f'{ind + 1}. {menup[ind]}')
    ans = input('¿Que deseas hacer?: \n')
    if ans == '1':
        os.system('cls')
        for a, b in productos.items():
            print(f'{a.center(10, ' ')}: {b}')
    elif ans == '2':
        os.system('cls')
        while True:
            producto = input('¿Que producto desea agregar?: \n')
            if not producto.isalpha():
                print('Solo se pueden ingresar caracteres alfabeticos')
                break
            if producto.lower() in productos:
                print('Este producto ya existe \n')
                continue
            else:
                print(f'El producto {producto} fue agregado')
                break
    elif ans == '3':
        os.system('cls')
        while True:
            eliminar = input('¿Que producto deseas eliminar?: \n')
            if not eliminar in productos:
                print('No puedes eliminar un producto que no existe')
                break
    elif ans == '4':
        pass
    elif ans == '5':
        os.system('cls')
        exit('Hasta pronto')
    else:
        os.system('cls')
        print('Error: Caracter invalido')
