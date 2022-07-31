
# Question 1
for i in range(0,1000):
    if i ** 3 <= 1000:
        print(i ** 3)

# Question 2

# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break

start = 1
end = 100

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# Question 3

name = input("What is your name? ")
age = input("How old are you? ")

age = int(age)

if age < 18:
    print(name + ", you are a kid.")
elif age <= 64 and age >= 18:
    print(name + ", you are an adult.")
else:
    print(name + ", you are a senior.")

