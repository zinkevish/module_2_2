print ( "Введите три числа")
first =  input ()
second = input ()
third =  input ()
if first == second == third:
    print (3)
elif first == second != third :
    print(2)
elif first != second == third :
    print(2)
elif first == third != second :
    print (2)
else:
    print(0)
