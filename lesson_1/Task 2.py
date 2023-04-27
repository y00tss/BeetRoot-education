
# 1
print("Hello world")
# """"""
print("""
Hello                         hello                         hello
     hello               hello     hello               hello
          hello     hello               hello     hello
               hello                         hello""")

# var variables and concatenation
s = "Bobre " # using space to avoid *no space word
d = "Cześć"

print(s + d)

# or
print(s, d)

# using end sep \n \t
s = "Bobre" # no space to avoid double space in print func
print(s, d, sep="maly ") # also with space
print("--------------------------------------------------------------------------------------------")
print("\tWord", 2, 3, "additional word", s, d, "\n")  # \t - indent , \n new string