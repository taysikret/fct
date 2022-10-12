# условные конструкции
# if 5 > 5:
#     print("Yes")
#     print("!!!")
# else :
#     print("false")


# isHappy = True
# if isHappy :
#     print("User is happy")

# isHappy = False
# if not isHappy == True:
#     print("User is happy")

# user_data = int(input("Введите число:"))
# if user_data > 5: # != < ==
#     print("Мы на месте")
#     if user_data > 6:
#         print("Число больше, чем 5")


# isHappy = True
# if isHappy == True:
#     print("User is happy")
# else:
#     print("User is unhappy")
#
# isHappy = False
# if isHappy == True:
#     print("User is happy")
# else:
#     print("User is unhappy")



# user_data = int(input("Введите число:"))
# isHappy = False
# if isHappy:
#     print("User is happy")
# if user_data > 5:
#     print("Number is more than 5")
# if user_data < 10:
#     print("Number", user_data, "is less than 10")
# else:  #так как сработал elif, то не срабатывает else
#     print("User is unhappy")




user_data = int(input("Введите число:"))
isHappy = False
if isHappy or user_data <= 100: # оператор and для обозначения обеих условий
    if user_data == 100:
        print("User is happy")
    if user_data > 5:
        print("Number is more than 5")
    if user_data < 10:
        print("Number", user_data, "is less than 10")
else:
    print("User is unhappy")