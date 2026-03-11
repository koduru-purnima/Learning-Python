num  = int(input(" enter number of rows: "))
print(' ---------first Pattern :--------')
for i in range(1,num+1):
    print('* ' * i)
print("----------Reverse Pattern ---------------")

for i in range(num,0,-1):
    print('* ' * i)
print("------------TRIANGLE-------------")
for i in range(1,num+1):
    print(" "*(num-i)+'* '*i)
print("------------Reverse TRIANGLE-------------")
for i in range(num,0,-1):
    print(' '*(num-i)+'* '*i)


    print("------------daimond-------------")
for i in range(1,num+1):
    print(" "*(num-i)+'* '*i)

for i in range(num,0,-1):
    print(' '*(num-i)+'* '*i)