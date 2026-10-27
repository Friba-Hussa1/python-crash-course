# even_nums=0
# for i in range(5):
#     if i%2==0:
#         even_nums+=1
#         print(f"{i} is even")
# print(even_nums)


# s="demo loops - fruit loops"
# for index in range(len(s)):
#     if s[index]=='i' or s[index]=='u':
#         print(f"{s[index]} found at index {index}")

# w="abcdefghijjjklmnopqrsss"
# seen=''
# count=0
# for char in w:
#     if char not in seen:
#         seen+=char
#     else:
#         count=count+1
#         print(f"{char} is repeated {count} times")
    
# guess=0
# x=int(input("Guess a number between 1 and 10: "))
# while guess**2<x:
#     guess+=1
# if guess**2==x:
#     print(f"{guess} is the square root of {x}")
# else:
#     print(f"{x} is not a perfect square")


# secret=4
# user_guess=int(input("Guess a number between 1 and 10: "))
# while user_guess!=secret:
#     if user_guess<secret:
#         print("Too low")
#     else:
#         print("Too high")
#     user_guess=int(input("Guess again: "))

found=False
secret=80
for i in range(1,11):
    if i == secret:
        print("found")
        found=True
if not found:
    print("not found")