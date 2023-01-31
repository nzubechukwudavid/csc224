#! python

# Write a python script that takes two numbers as input and calculate their sum in
# two's complement

print("""
This program converts two negative numbers to their twos complement form
and adds (subtracts) them. within the range of 8-bits""")

"""
how to convert to twos complement:
take the binary form,
invert the zeros and ones,
add one to the result
if there's a "carry", drop it.
"""


def convert_to_binary(number):
    bin_digit = bin(number)[2:]

    # what I want to do here is to add leading zeroes to make 2 bit groups always. 
    return bin_digit.rjust(8, "0")


def to_twos_complement(binary_string):
    data = binary_string
    inverted = "".join("10"[int(x)] for x in data)
    results = []
    carry = 1
    for bit in inverted[::-1]:
        new_bit = int(bit) ^ carry
        carry = int(bit) & carry
        results.append(new_bit)
    return "".join(str(i) for i in results[::-1])


# returns the integer form
def to_int(twos_complement_form):
    return int(to_twos_complement(twos_complement_form), 2)


a = int(input("Enter a negative number without the sign: "))
b = int(input("Enter another negative number without the sign: "))
input_a = a
input_b = b

a = to_twos_complement(convert_to_binary(a))
b = to_twos_complement(convert_to_binary(b))

result = bin(int(a, 2) + int(b, 2))[3:]
print(f"-{input_a}-{input_b} = -{to_int(result)}\n")

print(f"""
In Twos complement form:
  {input_a}   {a}
+ {input_b}   {b}
________________________
= -{to_int(result)}   {result}
""")
