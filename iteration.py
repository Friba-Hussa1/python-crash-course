
# first example
# where=input("Where do you want to go? right or left? ")
# while where == "right":
#     where=input("you are in the lost forest. go left or right?")
# print("Yoou got out")



# second example
# n= int(input("enter  a number:"))

# while n>0:
#     print('x')
#     n=n-1
    

# third example
# n=6
# while n>0:
#     print('x'*n)
#     n-=1


# fourth example
#  n is a counter variable so that we can keep track of our loop iterations
# n=0
# where = input("Where do you want to go? right or left? ")
# while where == "right":
#     n+= 1
#     if n>2:
#         print("You are lost in the forest. You have to go back.")
#     where = input("you are in the lost forest. go left or right? ")
# print("You got out of the forest.")

# fifth example
# x=4
# i=1
# factorial=1

# while i<=x:
#     factorial= factorial*i
#     i+=1
# print(f"tha factorial of {x} is {factorial}")

# for loop
# for i in range(5):
#     print(i)

# for n in range(1,4,1):
#     print(n)

# for me in range(4,0,-1):
#     print(me)

# for j in range(1,4,2):
#     print(j*2)

# mysum=0
# for i in range(10):
#     mysum+=i
# print(mysum)

mysum=0
start=3
end=5

for i in range(start,end+1):
    mysum+=i
print(mysum)

