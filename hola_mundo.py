# 1. TAREA: imprime "Hola, mundo"

print("Hola, mundo")

# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Noelle"
print("Hola, Noelle")	# con una coma
print( "hola, " + name)	# con un +

# 3. imprimir "Hola 42!" con el número en una variable
name = 42
print("Hola,",str(name),"!")	# con una coma
print("Hola, " + str (name) + "!" )	# con una +	-- este debería arrojar un error! 
"""Arroja error: TypeError porque no se puede sumar un string con un numero"""

# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Amo comer {} y {}" .format (fave_food1, fave_food2)) # con .format()
print(f"Amo comer {fave_food1} y {fave_food2}" ) # con una cadena f

#--------------------------------------PRACTICE-----------------------------------------

print("hola, mundo!") #1

my_name = "Pablo"
print("hola,", my_name, "!") #2a
print("hola," + my_name + "!") #2b

num = 10
print("hola,",str (num)) #3a
print("hola, " + str(num))


#--------------------------BONUS NINJA---------------------------------

eat_1 = "fideos"
eat_2 = "completos"
print("Amo comer {} y {}" .format(eat_1 , eat_2)) #4a
print(f"Amo comer {eat_1} y {eat_2}") #4b