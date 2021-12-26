print("hello world")

what_to_print = "hello world\n"

print(what_to_print * 4)

print(list(range(9, 2, -1)))

amount_of_print = 4

for i in range(amount_of_print):
    print(what_to_print)
    print("I is", i)

list_of_names = ["hen", "noam", "lior", "amichai"]
amount_of_print = 4

for i in range(1, amount_of_print):
    print(str(i) + ") " + what_to_print)

for i in range(len(list_of_names)):
    print(list_of_names[i])


for name in list_of_names:
    print(name)
    print(list_of_names.index(name))

a = 0
while a < 10:
    print(a)
    a = a+1

for name in list_of_names:
    if name == "hen":
        continue
    print(name)

