m = int(input("m = "))

# розв’язувати рівняння виду  a mod m = x
print("Рівняння виду a mod m = x")
a = int(input("a = "))
x = a % m 
print("x =", x)


# розв’язувати рівняння виду a^b mod m = x
def aModM(a, m):
    number = 0
 
    for i in range(len(str(a))):
        number = (number * 10 + int(str(a)[i]))
        number = number % m
 
    return number

def aPowbModM(a, b, m):
  
    ans = aModM(a, m)
    mul = ans
 
    for i in range(1, b):
        ans = (ans * mul) % m
         
    return ans

print("Рівняння виду a^b mod m = x")
a = int(input("a = "))
b = int(input("b = "))

print("x =", aPowbModM(a, b, m))


#генерувати просте число у діапазоні від A до B.
print("Генерація простого числа в діапазоні [A, B]")
a = int(input("A = "))
b = int(input("B = "))
lst = [2]
for i in range(3, b + 1, 2):
	if (i > 10) and (i % 10 == 5):
		continue
	for j in lst:
		if j * j - 1 > i:
			lst.append(i)
			break
		if (i % j == 0):
			break
	else:
		lst.append(i)
new_lst = []
for i in lst:
    if i >= a:
        new_lst.append(i)
print(new_lst)
