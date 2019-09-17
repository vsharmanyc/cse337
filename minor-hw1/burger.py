# Vasu Sharma
# 110493783
# vvsharma
#
# CSE 337 (Fall 2019)
# Minor Homework 1, Problem 1

def burger(order):
    if type(order) == type("") and order != "":
    	protiens = 0
    	toppings = 0
    	condiments = 0
    	for x in order:
    		if x in "BTV":
    			protiens += 1
    		elif x in "ltopjcbsmf":
    			toppings += 1
    		elif x in "kuyaq":
    			condiments += 1
    		else:
    			return "unrecognized order code"
    	if protiens == 1 and 0 <= toppings <= 5 and 0 <= condiments <=2:
    		if "B" in order:
    			return 0.5 * toppings + 2.0
    		elif "T" in order:
    			return 0.5 * toppings + 2.5
    		else:
    			return 0.5 * toppings + 2.25
    	else:
    		return "invalid order"
    else:
    	return "unrecognized order code"


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print('burger("Bck"):', burger("Bck")) # simple cheeseburger
    print()
    print('burger("Tpmlmy"):', burger("Tpmlmy")) # turkey burger w/ stuff
    print()
    print('burger("altop"):', burger("altop")) # error: no protein
    print()
    print('burger("VtojsT"):', burger("VtojsT")) # error: too many protein choices
    print()
    print('burger("lsucjV"):', burger("lsucjV")) # okay; protein at end
    print()
    print('burger("Bqcbksmfy"):', burger("Bqcbksmfy")) # error: too many condiments
    print()
    print('burger("Toxpk"):', burger("Toxpk")) # error: invalid character (x)
    print()
    print('burger("Vqltopjm"):', burger("Vqltopjm")) # error: too many toppings
    print()

