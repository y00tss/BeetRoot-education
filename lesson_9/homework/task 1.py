def oops():
    raise IndexError()

def fix_oops():
    try:
        oops()
    except IndexError as e:
        print("IndexError was caused...", e)

fix_oops()

"""In case if we will change oops to KeyError next Errors:
Traceback (most recent call last):
  File "link to file", line 10, in <module>
    fix_oops()
  File "link to filey", line 6, in fix_oops
    oops()
  File "link to file", line 2, in oops
    raise KeyError()
KeyError
"""


