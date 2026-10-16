num = int(input("Enter a number: "))
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

if lower <= num <= upper:
    print("Number is in the given range")
else:
    print("Number is not in the given range")