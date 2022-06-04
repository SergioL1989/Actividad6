# Sergio Lemus Serrano Mayo-2022

#ACTIVIDAD 6

import funciones

tipoDeDocumento = str(input('¿Tipo de documento? '));
Id = int(input('Ingrese su numero de identificación '));
Nombre = str(input('Ingrese su nombre '));
Edad = int(input('Ingrese su edad '));
sexo = str(input('¿Tipo de sexo? '))
peso = float(input('Ingrese su peso en Kg '))
altura = float(input('Ingrese su altura en metros '))

funciones.IMC(Edad,peso,altura);