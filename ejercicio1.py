# Sergio Lemus Serrano Mayo-2022

#ACTIVIDAD 6

from ast import Or


a = int(input('a -> '));

print (a,' + ',a,' = ', a + a);

a *= a;
print(a,' x ',a,' = ',a);

print(a != a  or a == a)

print(a > a if a else a)