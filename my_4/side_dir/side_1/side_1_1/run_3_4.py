"""
    Pycharm can't following this import if installed with debug
"""

print("Entering run")

try:
    print("importing lib_3")
    from sanglais.lib_3 import lib_3_func
    print("importing lib_4")
    from sanglais.sub_4.sub_1_1.lib_4 import lib_4_func
except ImportError as e:
    import sys
    import imp
    path = ''
    for i in sys.path:
        if 'site-packages' == i[-13:]:
            path = i
    if not path:
        raise e
    _lib_3 = imp.load_source('lib_3',path+'/sanglais/lib_3.py')
    lib_3_func = _lib_3.lib_3_func
    _lib_4 = imp.load_source('lib_4',path+'/sanglais/lib_4.py')
    lib_4_func = _lib_4.lib_4_func

print ("Calling lib_3_func")
lib_3_func()

print ("Calling lib_4_func")
lib_4_func()

print("That's All Folks")