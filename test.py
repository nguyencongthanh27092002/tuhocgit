print("Hello, world!")
firstName = "Nguyen Cong"
lastName = "Thanh"
print(firstName + " " + lastName)

def sum(arr):
    sum = 0
    for n in arr:
        sum += n
    return sum

arr = [1,2,3,4,5,6,7,8,9,10]
res = sum(arr)
print("Result of arr: ", res)

print("Hi")
