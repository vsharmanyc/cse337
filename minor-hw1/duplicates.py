# Vasu Sharma
# 110493783
# vvsharma
#
# CSE 337 (Fall 2019)
# Minor Homework 1, Problem 2

def duplicates(installed):
	repeats = []
	from re import search
	for i in range (0, len(installed)):
		name = installed[i][installed[i].rfind("/")+1:]
		if name not in repeats and any(search("/"+name+"$",x) for x in installed[i+1:]):
			repeats.append(name)
	return repeats


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print('Testing duplicates(["/bin/less", "/opt/local/bin/nice", "/usr/local/bin/host", "/usr/local/bin/apropos", "/usr/local/bin/touch"]):')
    print()
    print(duplicates(["/bin/less", "/opt/local/bin/nice", "/usr/local/bin/host", "/usr/local/bin/apropos", "/usr/local/bin/touch"]))
    print('\n')
    print('Testing duplicates(["/opt/local/bin/cp", "/usr/local/bin/ls", "/usr/bin/touch", "/usr/bin/head", "/bin/ls"]):')
    print()
    print(duplicates(["/opt/local/bin/cp", "/usr/local/bin/ls", "/usr/bin/touch", "/usr/bin/head", "/bin/ls"]))
    print('\n')
    print('Testing duplicates(["/opt/local/bin/su", "/usr/bin/yacc", "/bin/strings", "/usr/bin/nice", "/usr/bin/su", "/usr/bin/rm", "/usr/bin/awk", "/opt/local/bin/uptime", "/bin/ed", "/usr/bin/talk", "/usr/bin/less", "/opt/local/bin/cd", "/usr/local/bin/cd", "/usr/local/bin/sed", "/opt/local/bin/sudo", "/usr/bin/uptime", "/usr/bin/gzip", "/usr/bin/uniq", "/usr/local/bin/man", "/usr/local/bin/top"]):')
    print()
    print(duplicates(["/opt/local/bin/su", "/usr/bin/yacc", "/bin/strings", "/usr/bin/nice", "/usr/bin/su", "/usr/bin/rm", "/usr/bin/awk", "/opt/local/bin/uptime", "/bin/ed", "/usr/bin/talk", "/usr/bin/less", "/opt/local/bin/cd", "/usr/local/bin/cd", "/usr/local/bin/sed", "/opt/local/bin/sudo", "/usr/bin/uptime", "/usr/bin/gzip", "/usr/bin/uniq", "/usr/local/bin/man", "/usr/local/bin/top"]))
    print('\n')
    print('Testing duplicates(["/usr/bin/echo", "/bin/screen", "/usr/bin/rm", "/opt/local/bin/grep", "/usr/local/bin/talk", "/opt/local/bin/echo", "/bin/awk", "/bin/vi", "/usr/bin/vi", "/usr/bin/touch", "/bin/make", "/bin/su", "/usr/bin/less", "/opt/local/bin/quota", "/usr/local/bin/grep", "/opt/local/bin/w", "/usr/local/bin/vi", "/bin/sed", "/usr/local/bin/touch", "/bin/emacs"]):')
    print()
    print(duplicates(["/usr/bin/echo", "/bin/screen", "/usr/bin/rm", "/opt/local/bin/grep", "/usr/local/bin/talk", "/opt/local/bin/echo", "/bin/awk", "/bin/vi", "/usr/bin/vi", "/usr/bin/touch", "/bin/make", "/bin/su", "/usr/bin/less", "/opt/local/bin/quota", "/usr/local/bin/grep", "/opt/local/bin/w", "/usr/local/bin/vi", "/bin/sed", "/usr/local/bin/touch", "/bin/emacs"]))
    print()

