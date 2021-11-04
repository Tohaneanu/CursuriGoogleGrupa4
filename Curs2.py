my_var = 5
msg = "nu sunt respectate conditiile"
if my_var > 6:
    msg = "Set instructini 1"
elif my_var < 10:
    msg = "Set instructini 2"

print(msg)

a = 1
b = 2
x = 1 if a > b else -1
print(x)
for i in range(10):
    print(f"set de instructiuni {i}")

variabila = "Ana are mere"
# lista = []
# for i in variabila:
#     lista.append(i)
lista = [i for i in variabila]
print(lista)

for item, value in enumerate(variabila):
    print(f"{item} => {value}")

dictionar = {"key1": "value1", "key2": "value2"}
for item in dictionar.items():
    # print(item)
    item0, item1 = item
    print(item0, item1)
variabila = (1,)
print(type(variabila))
