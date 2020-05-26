# Print out each element of the following array on a separate line:
# ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code.
# Run through the UPER problem solving framework while going through your thought process.

class Test:
    
    def __str__(self):
        return "test"

arr = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', Test(), 'void *', '42', 'float', 'pointers', 5006]

# for item in arr:
#     print(item + "\n")

for item in arr:
    print(str(item) + "\n")