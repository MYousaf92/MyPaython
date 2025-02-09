
'''
if expression:
    print ('')
    print ('')
elif expression: 
    print ('')
else:
    print ('')
'''
' yes i forgot the python code , becasus almost from two weeks , ihave not seen again python code.

'''
val = float (input ("Enter float value: "))
print ('Float value = ' + str(val))
print ('Float value = ', val)
print (f'Float value = {val}')
print ("Enter ahmad's address: ")
'''

 
'''
a = 10
b = 16
c = 15

if a > b and a > c: 
    print (a)
elif b > a and b > c:
    print ('B')
    print (b)
else: 
    print (c)
'''

'''choice = int (input ("Enter number: "))
match choice: 
    case 1: 
        print ('Option 1')
    case 2: 
        print ('Option 2')
    case 3: 
        print ('Option 3')
    case _: 
        print ("Unknown")'''
        

# for i in range(0, 10): # for (int i=0; i<10; i++)
#     print ('Hello World')
    
    
# for k in range(0, 10, 3): # for (int k=0; k<10; k+=3)
#     print ('HAHAHA!!!')

# items = ['A', True, False, 1.1, 'B', 'C', 'D', 'E', 'F', 'G']
# for i in items:
#     if (i == 'B' or i == 'C' or i == 'D'):
#         continue
#     print (i)
    
    
    
# arr = []
# x = -1
# while x != 0:
#     x = int (input ('Enter any integer (or 0 to exit the loop): ')) 
#     if (x == 0):
#         continue
#     arr.append(x)


# for index in arr: 
#     print (index, end=" ")


x = int (input ('Enter your table no='))
for i in range(1,11):
 print(f'{x} x {i} = {x*i}')   
