"""Given the list of simbols and its desire lenghts return is prefix code"""
import random as rnd

s = [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h'], ['i'], ['j'], ['k'], ['l'], ['m'], ['n'], ['o'], ['p'], ['q'], ['r'], ['s'], ['t'], ['u'], ['v'], ['w'], ['x'], ['y'], ['z']]

for i in range(len(s)):
	s[i].append(rnd.randint(1,len(s)))

size = lambda leng: leng[1]
s.sort(key=size)

s[0].append(0)
for i in range(1, len(s)):
	code = (s[i-1][2] + 1) * (2**(s[i][1] - s[i-1][1]))
	s[i].append(code)

for l in s:
	print(l)
