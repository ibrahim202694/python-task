sum = 0.0
count = 0

print("Enter a numbers or (enter -1 to stop): clear")

while True:
    number = float(input("Enter a number: "))

    if number == -1:
        print("Program stopped.")
        break

    sum += number
    count += 1

    average = sum / count
    print("Current running average: ", average)
