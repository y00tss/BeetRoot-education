import random

user_input = input()

for i in range(5):                                                                                        # count of actions depend from string
   user_list = list(user_input)                                                                                         # to list for shuffling
   random.shuffle(user_list)
   shuffled_string = "".join(user_list)                                                                                 # and back

   print(shuffled_string, end=" ")                                                                              # printing in line by "end=" ""
