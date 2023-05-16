# # tub sonlar jadvali
# number_1 = int(input("enter the first number:"))
# number_2 = int(input("enter the second number:"))
# k = 0
#
# if number_1 == 0 and number_2 > 0 or number_2 == 0 and number_1 > 0:
#     for i in range(1, number_1 + number_2 + 1):
#         for j in range(1, number_1 + number_2 + 1):
#             if i % j == 0:
#                 k += 1
#         if k == 2:
#             print(i)
#         k = 0
# elif number_1 > number_2:
#     for i in range(number_2, number_1 + 1):
#         for j in range(1, number_1 + 1):
#             if i % j == 0:
#                 k += 1
#         if k == 2:
#             print(i)
#         k = 0
# elif number_2 > number_1:
#     for i in range(number_1, number_2 + 1):
#         for j in range(1, number_2 + 1):
#             if i % j == 0:
#                 k += 1
#         if k == 2:
#             print(i)
#         k = 0
# else:
#     print("eng kichik tub son 2 siz kiritgan sonlar ikkidan kichik yoki birxil son kiritgansiz qaytadan urunib ko'ring!")


# # fibonacci numbers
#
# # 1 1 2 3 5 8 13 21 34 55 89
#
# fibNumber = int(input("enter the fibonacci number: "))
# fib_number_1 = 1
# fib_number_2 = 1
# for i in range(1, fibNumber + 1):
#     fib_number_n = fib_number_2 + fib_number_1
#     print(fib_number_1)
#     fib_number_1 = fib_number_2
#     fib_number_2 = fib_number_n
# numLists = list(range(1, 102))
# numList = []
# numListAll = []
# for number in numLists:
#     numList.append(number)
#     if len(numList) == 3:
#         numListAll.append(numList)
#         numList = []
# numListAll.append(numList)
# print(numListAll)

