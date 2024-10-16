x = {2,45,3,53,"asda"}
c = [type(value) for value in x]
int_list = []
str_list = []
float_list = []
bool_list = []
for z in x:
    if type(z) == int:
        int_list.append(z)
    elif type(z) == str:
        str_list.append(z)
    elif type(z) == float:
        float_list.append(z)
    elif type(z) == bool:
        bool_list.append(z)
d = { "int": len(int_list),"str": len(str_list),"float": len(float_list),"bool": len(bool_list)}
v =max(d, key = d.get)
print(f"Найбільше елементів у списку з типом даних: {v}")
