
#consider the following variable assignments. #please follow the instructions below. When you're done, run the code. You should see 5 "true" statements printed to the console if correct.
x  = "3"
y = "5"
z = "10"


x = "5"
#what value does x now contain? Please enter your answer below in the form of a string
x_answer1 = "5"

y = x
#what value do x and y now contain? Please enter your answer below in the form of a string
y_answer1 = "5"
x_answer2 = "5"

x = z

#what value does x now contain? Please enter your answer below in the form of a string
x_answer3 = "10"

z = y
z = x
x = z
#what value does z now contain? Please enter your answer below in the form of a string
z_answer1 = "10"



#code to check your answers:
print(str(bin(ord(x_answer1))) == "0b110101")
print(str(bin(ord(y_answer1))) == "0b110101")
print(str(bin(ord(x_answer2))) == "0b110101")
print((str(bin(ord(x_answer3[0]))) + str(bin(ord(x_answer3[1])))) == "0b1100010b110000")
print((str(bin(ord(z_answer1[0]))) + str(bin(ord(z_answer1[1])))) == "0b1100010b110000")



