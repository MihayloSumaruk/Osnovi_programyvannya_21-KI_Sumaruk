dict1 = {1:"Python",
         2:"C++",
         3:{3.1: "Pascal", 3.2: "Assembler",3.3: "C#",3.4: "Java", 3.5: "Visual Basic"},
         4: "SQL"}
print(dict1)
dict2 = {1: type(dict1[1]), 2: type(dict1[2]), 3: type(dict1[3]), 4: type(dict1[4])}
print(dict2)