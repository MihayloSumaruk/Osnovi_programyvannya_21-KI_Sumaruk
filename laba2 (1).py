a = 'Сумарук' 
b = 'Михайло' 
c = 16 
g = type(a) 
k = type(b) 
h = type(c) 
list1 = [a, b, c] 
list2 = [g, k, h ] 
list_string = [] 
list_int = [] 
 
if g == str: 
    list_string.append(g) 
elif g == int: 
    list_int.append(g) 
 
if k == str: 
    list_string.append(k) 
elif k == int: 
    list_int.append(k)   
 
if h == str: 
    list_string.append(h) 
elif h == int: 
    list_int.append(h) 
 
if len(list_string) > len(list_int): 
    print('Тип даних str переважає') 
elif len(list_int) > len(list_string): 
    print('Тип даних int переважає')
