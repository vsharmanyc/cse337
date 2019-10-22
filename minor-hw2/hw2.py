import re

def printMatches(regex, strings):
	for str in strings:
		if(re.search(regex, str)):
			print(str)


"""1. (5 points) For each of the strings below, does the pattern [^O]*o+ match the string? If so,
list which part of the string will be matched. If not, then state "no match".
"""

strings = ["balloons", "FOODY", "bookstore", "\"Look\"", "PoolRoOM"]
print("matched strings:")
printMatches("[^O]*o+", strings)

"""
balloons     --- balloo
bookstore    --- booksto
Look         --- "Loo
PoolRoOM     --- PoolRo
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
3. (5 points) You have been assigned to validate user identification numbers for a new
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
regex = "^(\d*[02468])-\d{3}-(\d*[13579])$"

print("\nidStrings matches output:")
printMatches(regex, idStrings)
print("\nbadIdStrings matches output:")
printMatches(regex, badIdStrings)

#only the valid ids got printed and not the bad ones


"""
4. (10 points) An IPv4 (Internet Protocol version 4) address consists of exactly four integer
values (each in the range 0–255), separated by periods (this is called dotted-quad
representation). Leading zeros are not permitted. For example, 128.151.220.14 and
127.0.0.1 are valid IPv4 addresses, but 209.337.14.1 and 230.145.09.11 are not (337 is too
large, and "09" has a leading zero).
Define a regular expression that will match valid IPv4 dotted-quad addresses and ONLY
those addresses. BE CAREFUL when creating the part of your pattern that matches a
number in the range 0–255; you may need to define several patterns (for different ranges of
numbers) and combine them using alternation.
"""

addresses = ["128.151.220.14","127.0.0.1","249.209.255.0","0.0.0.0"]
badAddresses = ["209.337.14.1","230.145.09.11"]
regex = "^((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]).){3}(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$"

print("\naddresses matches output:")
printMatches(regex, addresses)
print("\nbadAddresses matches output:")
printMatches(regex, badAddresses)

#only the valid addresses got printed and not the bad ones


"""
5. (15 points) For each of the following Perl regular expressions, give a complete and precise
description of the function of the regular expression, plus a related example string:
(a) /"([^"]*)"/
	
	any or no sequence of characters, except for a double quote, between two doubles quotes

	ex: "kjhkjh"

(b) /[-+]?\d+(\.\d*)?F\b/

	Zero or one occurrances of either + or -,
	followed by a digit between 0-9 inclusive,
	followed by a dot,
	followed by any number of digits,
	followed by a F,
	followed by either nothing or a space which is then followed by any or no sequence of characters

	ex: -4.015F
	

(c) /(\D{2,}).*\[\1\]/

	2 or more occurances of any non digit character (lets calls this sequence of characters as group 1),
	followed by any number of characters except for a newline,
	followed by [,
	followed by the characters used in group 1,
	followed by ]

(d) /((.*?)\d)\s\2/

 any number of characters except for a newline (lets call this sequence of characters group 2), 
 followed by a digit between 0-9 inclusive,
 followed by a white space character,
 followed by the characters used in group 2

(e) /^[0-9]+\/\d+([+\-*\/]\=|([+]{2}|[-]{2}));$/ 
 
  starts one or more instances of a number between 0-9 inclusive, 
  followed by a forward slash, 
  followed by one or more instances of a number between 0-9 inclusive,
  followed by one of the following 3 groups of characters
  group 1: +, or -, or *, or / then followed by a =
  group 2: ++
  group 3: --
  ends with a semicolon
"""  