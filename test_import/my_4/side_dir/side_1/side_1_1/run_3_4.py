"""
    Pycharm can't following this import if installed with debug
"""

print("Entering run")

print("importing lib_3")
from sanglais.lib_3 import lib_3_func
print("importing lib_4")
from sanglais.sub_4.sub_1_1.lib_4 import lib_4_func

print ("Calling lib_3_func")
lib_3_func()

print ("Calling lib_4_func")
lib_4_func()

print("That's All Folks")