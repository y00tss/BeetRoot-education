import sys

print(sys.path)

"""http://dl3.joxi.net/drive/2023/05/16/0045/0626/2949746/46/f1e2798738.jpg"""

# adding directory
sys.path.append("C://Users//Mykhailo//Desktop//Python//BeetRoot-education//lesson_8//homework//task_2")

# check again
print(sys.path)

"""http://dl4.joxi.net/drive/2023/05/16/0045/0626/2949746/46/eeb4d32c96.jpg"""


try:
    import my_module
    print("Was imported")
except ImportError:
    print("Import Error")

# deleting of directory
sys.path.remove("C://Users//Mykhailo//Desktop//Python//BeetRoot-education//lesson_8//homework//task_2")

# and again check
print(sys.path)
"""http://dl4.joxi.net/drive/2023/05/16/0045/0626/2949746/46/deb66be002.jpg"""

"""YES, modifying of sys.path may affect on module imports"""



