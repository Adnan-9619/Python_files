"""try:
    f = open("world.txt", "a")
    print(f.write("fgghsdfbdfb"))
except:
    print("its a file")
else:
    print("my name is khan")
finally:
    print("mhbjgfjydhvmhfgtrdrt")"""


with (open("world.txt", "a")) as file:
    print(file.write("adnan"))


