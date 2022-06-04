# Sergio Lemus Serrano Mayo-2022

#ACTIVIDAD 6    


from ast import If


def IMC(a,b,c):
    if (a >= 18 ):
     peso = b /(c**2);
     if (peso < 18.5):
         print ('Usted es mayor de edad y tiene bajo peso');
     elif (peso >= 18.5 and peso < 25):
         print ('Usted es mayor de edad y tiene un peso normal');
     elif (peso >= 25 and peso < 30):
         print ('Usted es mayor de edad y tiene un sobre peso');
     elif (peso >= 30):
         print ('Usted es mayor de edad y tiene obesidad');  
    elif (a < 18 ):
     peso = b /(c**2);
     if (peso < 18.5):
         print ('Usted es menor de edad y tiene bajo peso');
     elif (peso >= 18.5 and peso < 25):
         print ('Usted es menor de edad y tiene un peso normal');
     elif (peso >= 25 and peso < 30):
         print ('Usted es menor de edad y tiene un sobre peso');
     elif (peso >= 30):
         print ('Usted es menor de edad y tiene obesidad');     

def figuras(figur):
    circulo = "circulo";
    for c in figur:
     if( figur == circulo ):
        figur = float(input('Radio -> '));
        respuesta = (figur**2)* 3.1416;
        return print('El radio es de ', respuesta);
        break;
    
    triangulo = "triangulo";
    for c in figur:
        if(figur == triangulo):
            altura = float(input('Altura -> '));
            base = float(input('Base -> '));
            respuest = (base*altura)/2;
            return print('El area del triangulo es ', respuest)
            break;
    cuadrado = "cuadrado";
    for c in figur:
        if(figur == cuadrado):
            lado = float(input('Lado -> '));
            answer = lado * 4;
            return print('El perimetro del cuadrado es ',answer)
            break;  

def operadorAritmetrica(valor1,operador,valor2):


    suma = "+"
    for c in suma:
        if (operador == "+"):
            opera = valor1 + valor2;
            return print(valor1,' + ',valor2,' = ',opera);
            break;
    resta = "-"
    for c in resta:
        if (operador == "-"):
            oper = valor1 - valor2;
            return print(valor1,' - ',valor2,' = ',oper);
            break;
    multiplicacion = "*"
    for c in multiplicacion:
        if (operador == "*"):
            ope = valor1 * valor2;
            return print(valor1,' x ',valor2,' = ',ope);
            break;
    divisi = "/"
    for c in divisi:
        if (operador == "/"):
            op = valor1 / valor2;
            return print(valor1,' / ',valor2,' = ',op);
            break;
