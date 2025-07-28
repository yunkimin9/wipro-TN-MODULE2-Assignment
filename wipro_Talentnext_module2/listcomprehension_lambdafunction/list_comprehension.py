# write a program to create an output dictionary which contains only the odd numbers that are present in the  input list=[1,2,3,4,5,6,7] aS keys and their cubes as value

input_list = [1, 2, 3, 4, 5, 6, 7]
output_dict = {x: x**3 for x in input_list if x % 2 != 0}
print(output_dict)

# make a dictionary of the 26 english alphabets mapping each with the corresponding integer
import string

alphabet_dict = {letter: idx for idx, letter in enumerate(string.ascii_lowercase, start=1)}
print(alphabet_dict)

