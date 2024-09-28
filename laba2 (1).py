list1 = ["asdasda", 123, 12455, "asdaggfghs", "35gg", 1245]
types = [type(value) for value in list1]
from collections import Counter
type_counter = Counter(types)
most_common_type = type_counter.most_common(1)[0][0]
print(f"Найчастіше зустрічаючийся тип даних: {most_common_type}")
