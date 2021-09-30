from sys import path ##Right now we are in the modules folder
path.append("folder1") #We add folder 1, so we can see the content of folder1

import module1

def say_hello2():
    print(f"{__name__} says hello.")

module1.say_hello1()