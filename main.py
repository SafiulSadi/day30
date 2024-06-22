
# # KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existant_key"]

# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit_list[3]

# # TypeError
# a = "abc"
# print(a + 5)

# FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["snadf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"that key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
print("error")
# the problem that needs to be solved are iftar problem and perfect permutation.
# need to look more into the buet exam for the chance to study there and mainly getting the hall facilities.


