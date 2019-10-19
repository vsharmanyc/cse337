import re

def printMatches(regex, strings):
	for str in strings:
		if(re.search(regex, str)):
			print(str)


"""1. (5 points) For each of the strings below, does the pattern [^O]*o+ match the string? If so,
list which part of the string will be matched. If not, then state "no match".
"""

strings = ["balloons", "FOODY", "bookstore", "Look", "PoolRoOM"]
print("matched strings:")
printMatches("[^O]*o+", strings)

"""
balloons
bookstore
Look
PoolRoOM
"""

"""
2. (5 points) Define a regular expression that will correctly (and exactly) match a valid
Gregorian calendar date of the form MM/DD/YYYY (with leading zeroes for single-digit
months and days) (and ONLY dates in this format).
• Months 1, 3, 5, 7, 8, 10, and 12 have 1–31 days
• Months 4, 6, 9, and 11 have 1–30 days
• Month 2 (February) has 1–28 days (ignore leap years)
• Assume that the year falls into the range 1900–2099
"""
dateStrings = ["01/31/1900", "02/28/2019", "04/20/2069"]
badDateStrings = ["02/29/1999", "difjdslfj", "04/31/2019", "4/2/2000", "06/00/1999"]
regex = "^(((0[13578]|1[02])\/(((0[1-9])|([1-2]\d))|3[0-1]))|((0[469]|11)\/(((0[1-9])|([1-2]\d))|30))|((02)\/((0[1-9])|(1\d)|(2[0-8]))))(\/(((19)|(20))\d\d))$"

#^(((0[13578]|1[02])\/(((0[1-9])|([1-2]\d))|3[0-1]))|((0[469]|11)\/(((0[1-9])|([1-2]\d))|30))|((02)\/((0[1-9])|(1\d)|(2[0-8]))))(\/(((19)|(20))\d\d))$  <-- regex for problem 2

print("\ndateStrings matches output:")
printMatches(regex, dateStrings)

print("\nbadDateStrings matches output:")
printMatches(regex, badDateStrings)

#only the valid date strings got printed and not the bad ones


"""
(5 points) You have been assigned to validate user identification numbers for a new
computer system. A valid user identification number consists of an even number (as
defined below), followed by a single dash, followed by three digits, followed by another
single dash, followed by an odd number (as defined below).
An even number is a sequence of one or more digits where the final (rightmost) digit is 0, 2,
4, 6, or 8 (other digits can be anything between 0 and 9). For example, 4 and 316 are both
even numbers.
An odd number is a sequence of one or more digits where the final (rightmost) digit is 1, 3,
5, 7, or 9 (other digits can be anything between 0 and 9). For example, 7 and 41629 are
both odd numbers.
Two examples of valid user identification numbers are 2130-405-3649 and 8-112-4637281.
By contrast, 445-917-307 is invalid because the first part (445) is not an even number as
defined above.
Define a regular expression that will match this particular pattern and ONLY this pattern.
"""
idStrings = ["0000000000-000-000000000000003", "1032-857-6846841165", "2130-405-3649", "8-112-4637281"]
badIdStrings = ["420-2-69", "666-420-100", "445-917-307"]
regex = "^(\d*[02468])-\d\d\d-(\d*[13579])$"

print("\nidStrings matches output:")
printMatches(regex, idStrings)
print("\nbadIdStrings matches output:")
printMatches(regex, badIdStrings)

#only the valid ids got printed and not the bad ones