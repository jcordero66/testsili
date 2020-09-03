largest = 0
smallest = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if smallest == 0 or num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Maximum is", largest)
print("Minimum is", smallest)
