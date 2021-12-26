my_file = open("read_my_contents.txt")
print(list(my_file.readlines()))

for line in my_file.readlines():
    print(line)
#    print(line, end='') -- print without new line


#my_other_file = open("moshe.txt", "w")
#my_other_file.write("hey hey\n ffff\n")


def update_file(your_name)
    my_names_file = open("names.txt", "a")
    my_names_file.write(your_name "\n")


update_file(input("pleas enter your name"))



