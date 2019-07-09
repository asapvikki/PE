


string_input = input()
input_list = string_input.split()
input_list = [str(a) for a in input_list]

print ( input_list )

string2 = input()

sort_list = string2.split()
sort_list = [str(a) for a in sort_list]

print ( sort_list )
lst = []
for word in input_list:
	size = len(word)
	num = 0
	for x in word:
		size = size - 1
		count = 1
		for y in sort_list:
			if y == x:
				num = num + count*(pow(10,size))
			else:
				count = count + 1
	tup = (num,word)
	lst.append(tup)	
	
for x in sorted(lst):
	print(x[1])
