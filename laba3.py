dict1 = {1:"Python",
         2:"C++",
         3:{3.1: "Pascal", 3.2: "Assembler",3.3: "C#",3.4: "Java", 3.5: "Visual Basic"},
         4: "SQL"}
print(dict1)

dict_types = {}
for key in dict1:
    val = dict1[key]
    if type(val) == dict:
        for sub_key in val:
            sub_val = type(val[sub_key])
            dict_types[sub_key] = type[sub_val]
    else:
        dict_types[key] = type(val)
print(dict_types)
