istrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"

if a > 0 and a <= 4:
    print("ok")

if a >= 2 and strOne == "One" or not strThree == "two":
    print("a is greater then 2")
elif b == 2.5:
    print("something")
elif strOne == "3":
    print("bla")
else:
    print("a is lower then 2")


my_list = ["hen", "lior", "shay", "ariel"]
my_other_list = ["roni"]
if my_list[0]  == "hen" or my_list[1] == "hen" or my_list[2] == "hen" or my_list[3] == "hen":
    print("Hen is in the list")

if "hen" in my_list:
    print("we have found hen")

    if my_other_list:
        print("hello")

if len(my_list) > 0:
    print("hey")

print(len(my_other_list))

if len(my_other_list) == 1:
    print("hey other list")

    c = "aaa"
    d = "aaa"
if c is d:
    print("c is d")

c = ["aaa", "1"]
d = ["aaa", "1"]
e = 9
if c is d:
    print("c is d")

if type(e) is int:
        print("e is an integer")



