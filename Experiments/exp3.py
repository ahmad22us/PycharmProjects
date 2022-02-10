# def my_function(c, b=2, a=1):
#     d=1
#     print(a, b, c)
#     return a+b+c
#
# print(my_function(5))
#
# my_dict={1:1, 1:2, 1:4, 2:5}
# print(my_dict)
##########################################
# def my_function(*args):
#     print(type(args))
#     add_value = 0
#     for i in args:
#         add_value += i
#     return add_value
#
#
# print(my_function(1, 2, 3, 4, 6))
#########################################
# def to_camel_case(text):
#     if text == "":
#         return "An empty string was provided but not returned"
#     else:
#         split_text = text.split("-","_")
#         f_text = []
#         for i in range(0, len(split_text)):
#             if split_text[0][0] != split_text[0][0].upper() and i == 0:
#                 f_text.append(split_text[i])
#             else:
#                 f_text.append(split_text[i].title())
#         join_text = ''.join(f_text)
#         return join_text
#
#
# print(to_camel_case(""))
########################################
operations = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication",
    "/": "division"
}

Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
print("Select operation to perform: ")
for i in operations:
    print(i)
symbol = input("Enter your choice of operation: ")
print(operations[symbol])
