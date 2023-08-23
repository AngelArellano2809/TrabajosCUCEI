#Arellano Granados Angel Mariano
#Algoritmo usa todos los operadores aritméticos 
#en dos números en diferentes funciones

def main ():
    num1 =int(input('Dame un número entero: '))
    num2 =int(input('Dame otro número entero: '))
    sum_ (num1, num2)
    res (num1, num2)
    mul (num1, num2)
    div (num1, num2)
    int_div (num1, num2)
    resi (num1, num2)
    pot (num1, num2)

def sum_ (num1, num2):
    suma = num1 + num2
    print(num1,'+', num2,'=', suma)
	
def res (num1, num2):
    resta = num1 - num2
    print (num1,'-', num2,'=', resta)
    
def mul (num1, num2):
    multiplicación = num1 * num2
    print(num1,'*', num2,'=', multiplicación)
    
def div (num1, num2):
    división = num1 / num2
    print(num1,'/', num2,'=', división)
    
def int_div (num1, num2):
    Integer_division = num1 // num2
    print (num1, '//', num2, '=', Integer_division)
    
def resi (num1, num2):
    residuo = num1 % num2
    print(num1, '%', num2,'=', residuo)
    
def pot (num1, num2):
    potencia = num1 ** num2
    print(num1, '**', num2, '=', potencia)

main()
