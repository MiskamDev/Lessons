# Explicit
name = "Bro"
age = 21
gpa = 1.9
student = True

print(type(name)) # Str
print(type(age))  # Int
print(type(gpa))  # Float
print(type(student)) # Boolean


age = float(age)  # Integer to Float

print(age)
print(type(age))


student = str(student)

print(student)
print(type(student))



# Implicit
x = 2      # Integer
y = 2.0    # Float

x = x / y  # Implicit type casting

print(x)  # Float