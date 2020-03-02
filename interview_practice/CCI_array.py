


#1.1 Is Unique
# Implement an algorithm to determine if a string has all unique characters.
# what if you cannot use additional data structures?

# create a set/ or hash table from string and see if length v original string is diff

"""
def isUnique(string):
    set_string = set()

assert isUnique('cat') ==True, "True"
assert isUnique('cata') ==False, "False"
assert isUnique('aa') ==False, "False"
assert isUnique('a')==True,"True"
"""


# 1.2 CHeck permutations
# Given two strings, write a method to decide if one is a permutation of the other.
#

# check both same length
# sort both, then compare
# complexity is O(n log n)


#1.3 skipped

#1.4 Palindrome Permutation
# palindrome check

def checkPalindrome(s1,s2):
    s1= s1.replace(" ","")
    s2=s2.replace(" ","")


    if len(s1) == len(s2):
        # hash table/dict for each character map
        s1_alphabet = {}
        s2_alphabet = {}
        for i in range(0,len(s1)):
            if s1[i] in s1_alphabet:
                s1_alphabet[s1[i]] += 1
            else:
                s1_alphabet[s1[i]] = 1

            if s2[i] in s2_alphabet:
                s2_alphabet[s2[i]] += 1
            else:
                s2_alphabet[s2[i]] = 1
        if s1_alphabet == s2_alphabet:
            return True

        else:
            return False

    else:
        return False

print(checkPalindrome("taco cat","cat taco"))
print(checkPalindrome("taco moo","cat taco"))


#1.5 One Away
# insert, replace, or remove a char -
"""
def oneAway(s1,s2):
    # check replace
    if len(s1) == len(s2):
       #call helper that goes thru both at the same time and just tracks that their is ONLY ONE diff

    #check remove/insert -- no difference
    elif len(s1) -len(s2)==-1:
        #call helper that uses a pointer to go thru both the pointer can only be adjusted for the diff of char once
    elif len(s1) -len(s2)==1:
        # call inverse of helper above
    else:
        return False

"""


#1.6 String Compression


#1.7 Rotate Matrix
# rotate NxN matrix by 90 degrees
