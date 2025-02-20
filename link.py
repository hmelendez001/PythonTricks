"""
Shout out to user Shiva Vinodkumar on the LinkedIn Java Community for their original post on this
Shout out to user Maksim Maksimov for their update to the Palindrome question
"""

# Check if list contains int x
find = 111
lst = [3, 3, 4, 5, 2, 111, 5]
print(f"Is {find} in {lst}: {find in lst}")

# Find duplicate number in int list
elements = [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8, 8]
duplicates, seen = set(), set()
for element in elements:
    if element in seen:
        duplicates.add(element)
    seen.add(element)
print(f"Duplicates in {elements}: {duplicates}")

# Check if two strings are anagrams
astr="flow"
bstr="wolf"
print(f"Are '{astr}' and '{bstr}' anagrams? {sorted(astr) == sorted(bstr)}")

# Remove all duplicates from a list
lst=list(set(elements))
print(f"Remove duplicates from {elements}: {lst}")

# Find pairs of ints in list such that their sum is equal to int x
x=7
s = set()
pairs = []
for num in elements:
    complement = x - num
    if complement in s and (num, complement) not in pairs:
        pairs.append((num, complement))
    s.add(num)
if len(pairs) > 0:
    print(f"Pairs {pairs} sum to {x} in {elements}")
else:
    print(f"No pairs sum to {x} in {elements}")

# Check if a string including sentences with punctuation is a palindrome
def is_palindrome(s: str) -> bool:
    for letter in s:
        if letter.isalnum() is not True:
        # if not letter.isalnum(): same expression
            s = s.replace(letter,'')
        if s.lower() == s[::-1].lower():
            return True
    return False

str = "abc xyz"
print(f"String '{str}' is palindrome? {is_palindrome(str)}")
str = "racecar"
print(f"String '{str}' is palindrome? {is_palindrome(str)}")
str = "A dog! A panic in a pagoda!"
print(f"String '{str}' is palindrome? {is_palindrome(str)}")

# Use list as stack, array, queue
# list as stack
stack = [3, 4]
stack += [5, 6]
print(f"List as stack: {stack}")
lst = stack
lst.append(10)
lst2 = list.copy(lst)
lst2.pop()
print(f"List before pop {lst} and after pop {lst2}")
lst.insert(0, 5)
lst.pop()
print(f"List with insert and pop {lst}")

# Get missing number in [1...100]
lst = list(range(1, 100))
lst.remove(23)
print (f"Missing number in 1...100: {set(range(lst[0], lst[-1])) - set(lst)}")

# Compute the intersection of two lists
def intersect(lst1 : list, lst2 : list) -> list:
    res, lst2_copy = [], lst2[:]
    for el in lst1:
        if el in lst2_copy:
            res.append(el)
            lst2_copy.remove(el)
    return res

lst1 = list(range(1, 5))
lst2 = list(range(3, 9))
print (f"Intersection of {lst1} and {lst2} is: {intersect(lst1, lst2)}")

# Find max and min in unsorted list
lst1 = [4, 3, 6, 3, 4, 888, 1, -11, 22, 3]
print (f"Max = {max(lst1)} of list {lst1}")
print (f"Min = {min(lst1)} of list {lst1}")

# Reverse string using recursion
def reverse(string: str) -> str:
    if len(string) <= 1:
        return string
    return reverse(string[1:]) + string[0]

str1 = "Alamo"
print(f"Reverse of {str1} is {reverse(str1)}")

# Compute the first n Fibonacci numbers
a,b = 0, 1 # initialize the first two
n = 10
print(f"First {n} Fibonacci numbers:", end = " ")
for i in range(n):
    print(a, end = " ")
    a,b = b, a+b
print("")

# Sort list with Quicksort algorithm
def qsort(lst : list) -> list:
    if lst == []:
        return []
    return qsort([x for x in lst[1:] if x < lst[0]]) + lst[0:1] + qsort([x for x in lst[1:] if x >= lst[0]])

lst = [44, 33, 22, 5, 77, 55, 999]
print(f"Qsort {lst} = {qsort(lst)}")
# Find all permutations on s of string
def get_permutations(w: str):
    if len(w) <= 1:
        return w
    smaller = get_permutations(w[1:])
    perms = set()
    for x in smaller:
        for pos in range(0, len(x) + 1):
            perm = x[:pos] + w[0] + x[pos:]
            perms.add(perm)
    return perms

str1 = "python"
str1 = "nane"
str1 = "naxe"
print(f"Permutations of the word '{str1}': {get_permutations(str1)}")

