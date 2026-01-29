# Concept 1: Names, Objects, Immutability
# Demonstrating how Python passes things through references, not values

# Setting a to basic base seq and setting b equal to a
a = "ACTG"
b = a

# a and b now share the same id (address)
print(id(a))
print(id(b))

# Adding a "G" to b
b = b + "G"

# Printing the values for a and b as well as the id of b
print(a)
print(b)
print(id(b))

# Learnings: b was changed, a was not even though they shared an id. the + operator
#            created a new object for b, making a new id as well.



# Concept 2: Lists vs Strings (Mutability Contrast)
# Checking the difference in mutability between lists and strings using append

# Creating a list named x
x = [1, 2, 3]

# Copying list into y
y = x

# Checking IDs of lists
print(id(x))
print(id(y))

# Adding 4 to the end of y
y.append(4)

# Checking the changes in both lists
print(x)
print(y)

# Creating stringx
stringx = "Hello"

# Copying stringx into stringy
stringy = stringx

# Changing stringy
stringy = "Bye"

# Checking the changes
print(stringx)
print(stringy)

# Learnings: When creating and mutating lists (mutate means to change the original
#            without completely resassigning), if you copy a list into a new variable
#            and change said variable, the original list will also change. Morever, 
#            strings are immuatable, meaning you MUST make a new variable if you want to
#            mutate a string


# Concept 3: Functions as first-class objects
# Understanding how functions can be used as objects

# Creating a function to count how many times G and C occur in a seq
def count_gc(seq):

    # Return the sum of: 1 for every time G and C occur
    return sum(1 for b in seq if b in ("G", "C"))

# Creating a "variable" (really just an object) that represents the function
# allowing you to create short versions of the function
f = count_gc

# Printing the result of applying f (count_gc) to the given sequence
print(f("ATGCGC"))

# Learnings: Python is particularly powerful when it comes to objects and functions
#            as you can essentially turn a function into an object that can be applied
#            to given data
