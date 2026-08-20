print("string + string → ?")
word_1 = "hola"
word_2 = "como estas?"
message_1 = word_1 + word_2
print(message_1)

print("______________")
print("string + int → ?")
word_3 = "cuantos años tienes ?"
whole_number = 33
message_2 = word_3 + whole_number
print(message_2) 

print("______________")
print("int + string → ?")
age = 33
word_4 = "cuantos años tienes ?"
message_3 = age + word_4 
print(message_3)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("______________")
print("list + list → ?")
list_1 = [1,2,3]
list_2 = [4,5,6]
whole_list = list_1 + list_2
print(f"La suma de {list_1} + {list_2} es igual a: {whole_list}")

print("______________")
print("string + list → ?")
word_3 = "7,6,5"
list_3 = [10,9,8]
print(word_3 + list_3)
# TypeError: can only concatenate str (not "list") to str   


print("______________")
print("float + int → ?")
float_var = 3.14
int_var = 3
message_4 = float_var + int_var
print(message_4)

print("______________")
print("bool + bool → ?")

estudia = True
practicar_ejercicios = True
suma_booleanos = estudia + practicar_ejercicios
print ("la suma de boleanos es: ", suma_booleanos)

