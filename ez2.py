import time
#string = "Shibashish!"
string=input(("Enter a string:"))
print_string = ""
for i in range(0, len(string)):
   print_string = print_string + string[i]
   print(print_string)
   time.sleep(2)
