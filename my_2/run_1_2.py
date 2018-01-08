"""
    Pycharm can't following this import if installed with debug
"""

print("Entering run")

print("importing lib_1")
from sanglais.lib_1.lib_1 import lib_1_func
print("importing lib_2")
from sanglais.lib_2.lib_2 import lib_2_func

print ("Calling lib_1_func")
lib_1_func()

print ("Calling lib_2_func")
lib_2_func()

print("That's All Folks")