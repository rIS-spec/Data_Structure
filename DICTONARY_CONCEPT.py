# marks = {
#      "amex": 100,
#      "hdfc": 81,
#      "axis": 76,
#      "sbi": 75,
#      "yes": 75,
#      "icici": 81,
# }
                                      # dictonary are mutable
# print(marks,type(marks))

# print(marks["hdfc"])

# print(marks["amex"])

# print(marks["icici"]) 
                               

# marks["amex"] = "pnb"
# print(marks)                                     



# words = {
#     "sahajjo": "help",
#     "anando": "happy",
#     "ghoum": "sleep",
# }
# word = input("Enter the word you want to meaning: ")
# print(words[word])


# student = {
#     "num1":"arish mahammad",  
#     "subject1" : {
#         "phy":67,
#         "che":81,
#         "math":85,
#     }
# }
# print(student.items())

# print(list(student.items()))

# new = {"coms":"70"}
# student.update(new)

# print(student)



square_num={x:x**2 for x in range(6)}
print(square_num)
square_num.clear()
print(square_num)