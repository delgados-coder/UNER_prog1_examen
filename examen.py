import os
###--------------------|realice funciones auxiliares|--------------------------###
def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def generar_menu(opciones):
    limpiar_consola()
    while True:
        limpiar_consola()
        print("----------------------Menu:------------------------")
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        print(f"{len(opciones) + 1}. Salir")
        
        seleccion = input("Selecciona una opcin: ")

        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(opciones):
                limpiar_consola()
                opcion_seleccionada = list(opciones.keys())[seleccion - 1]
                opciones[opcion_seleccionada]()
            elif seleccion == len(opciones) + 1:
                limpiar_consola()
                print("/--------------------------ADIOS--------------------------------/")
                break
            else:
                print("Porfavor, seleccina un nu,mero vlido.")
        else:
            print("Entrada no valida. x favor, introduce un numero.")
            
def convertir_a_enteros(lista):
    enteros = []
    for num_str in lista:
        enteros.append(int(num_str))
    return enteros
###--------------------|FIN funciones auxiliares|--------------------------###
   

         
#----|ingresar todas las calificaciones hasta la palabra fin
def pedir_calificaciones():
    limpiar_consola()
    calificaciones=[]
    calificacion=0
    contador=0
    while True:
        limpiar_consola()
        print("---------------|Ingrese las Calificaciones / 'FIN' para terminar|----------------")
        contador+=1
        print("Calificacion N°",contador)
        calificacion = input("-->")
        if calificacion.upper() == "FIN":
            return calificaciones
            break
        calificaciones.append(calificacion)


###-----Acciones del menu-------#
#----|Imprimir las calificaciones ordenadas de menor a mayor
def func_imprimir_menor_a_mayo():
    print("Lista de calificaciones(desordenada):")
    print(calificaciones_int)
    print("")
    print("Lista de calificaciones(ordenada):")
    print(sorted(calificaciones_int))
    input("presionar Tecla para continuar...")

#-----|Calcular y mostrar el promedio por pantalla.
def func_calc_y_mostrar_prom():
    
    suma=0
    contador=0
    for valor in calificaciones_int:
        suma += valor
        contador+=1
        
    print("Lista de calificaciones(desordenada):")
    print(calificaciones_int)
    print("")    
    print("El valor promedio de calificaciones:")
    print("-->",suma/contador)
    input("presionar Tecla para continuar...")

#-----|Contar el número de calificaciones ingresadas
def func_cont_num_calif_ingresadas():
    print("Lista de calificaciones(desordenada):")
    print(calificaciones_int)
    print("")  
    print("Se ingresaron un total de calificaciones igual a:")
    print(len(calificaciones_int))
    input("presionar Tecla para continuar...")

#-----| Convertir todas las calificaciones a strings y unirlas en una sola cadena(string) separada por comas.
def func_conv_todas_calif_y_cadena():
    print("Lista de calificaciones(desordenada):")
    print(calificaciones_int)
    print("")  
    print("Lista de calificaciones(separadas por (,)):")
    for valor in calificaciones_str:
        string=', '.join(calificaciones_str)
    print(string)  
    
    input("presionar Tecla para continuar...")
    pass

#-----|Contar cuántos alumnos han aprobado la materia (sacaron una nota mayor o igual a 6)
def func_num_alumnos_aprobados():
    cant_aprobados=0
    for valor in calificaciones_int:
        if valor >= 6:
            cant_aprobados+=1
    
    print("Lista de calificaciones(desordenada):")
    print(calificaciones_int)
    print("")  
    print("La cantidad de alumnos aprobados es:")
    print("-->",cant_aprobados)
    input("presionar Tecla para continuar...")
    pass

#----|Calcular la calificación más baja y la más alta e Imprimir por pantalla un mensaje con el
#----|siguiente formato: “La calificación más baja fue XX y la más alta XX.”
def func_calif_extremos():
    print("Lista de calificaciones(desordenada):")
    print(calificaciones_int)
    print("")
    print("Lista de calificaciones(ordenada):")
    print(sorted(calificaciones_int))  
    print("")
    print("La calificacion mas baja es:",sorted(calificaciones_int)[0])
    print("La calificacion mas alta es:",sorted(calificaciones_int)[-1])
    
    input("presionar Tecla para continuar...")
    
#----| Vaciar la lista
def func_vaciar_lista_de_calif():
    calificaciones_str.clear()
    calificaciones_int.clear()
    print("Lista de Calificaciones Vaciada")
    input("presionar Tecla para continuar...")


###-----Fin de Acciones del menu-----###


##///////////INICIO/////////////##


#----opciones y acciones del menu----#
menu_op={
"Imprimir de menor a mayor":func_imprimir_menor_a_mayo,
"Mostrar el promedio de calificaciones":func_calc_y_mostrar_prom,
"Numero de calificaciones ingresadas":func_cont_num_calif_ingresadas,
"Cadena de calificaciones separadas con (',')":func_conv_todas_calif_y_cadena,
"Mostrar Cantidad de Alumnos Aprobados":func_num_alumnos_aprobados,
"Mostrar la mayor y menor calificacion":func_calif_extremos,
"Vaciar lista de Calificaciones":func_vaciar_lista_de_calif,
}


#1.--------------------Utilizar una lista para almacenar las calificaciones.
calificaciones_str=pedir_calificaciones()
calificaciones_int= convertir_a_enteros(calificaciones_str)

generar_menu(menu_op)


##///////////FIN/////////////##