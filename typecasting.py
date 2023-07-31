#Implicit Type Conversion (Coercion):

#Implicit type conversion is done automatically by the programming language when it is safe and logical to do so. It occurs when a value of one data type is assigned to a variable of another data type that can represent the value without loss of data or precision. For example, converting an integer to a floating-point number.



num_int = 10
num_float = 5.5

result = num_int + num_float  # The integer is implicitly converted to float before addition
print(result)  # Output: 15.5

#Explicit Type Conversion (Type Casting):
#Explicit type conversion is done explicitly by the programmer using language-specific conversion functions or syntax. This method is used when there is a possibility of data loss or when the programmer wants to ensure a specific data type is used for an operation



num_str = "100"
num_int = int(num_str)  # Explicitly converting the string to an integer
print(num_int)  # Output: 100

num_float = float(num_int)  # Explicitly converting the integer to a float
print(num_float)  # Output: 100.0


