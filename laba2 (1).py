a  = "Михайло"
b = "Сумарук"
c = 16
list1=[a, b, c]
print(list1)
list2=[type(a), type(b), type(c)]
print(list2)
if type(a) == type(b) and type(b) == type(c) and type(a) == type(c):
    print("Тип:", type(a), "повторюється найчастіше")
else:
    print("Типи даних незбігаються")
