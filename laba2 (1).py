a = "Михайло"
b = "Сумарук"
c = "Сумарук"
list1=[a, b, c]
print(list1)
list2=[type(a), type(b), type(c)]
print(list2)
if type(a) == type(b) and type(b) == type(c) and type(a) == type(c):
    print("Тип str, повторюється найчастіше")
else:
    print("Тип даних незбігаються")
    
