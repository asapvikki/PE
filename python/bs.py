import math
stream = input()
stream = stream.split()
stream = [int(a) for a in stream]
start = 0
end = len(stream) - 1
stream.sort()
element = input("enter an element")
element = int ( element )
flag = 0
while(start <= end):
	##print('asap')
	mid = (start + end)/2
	mid = math.floor(mid)
	
	if element  == stream[mid]:
		flag = 1
		print ( 'element found' )
		break
	elif element > stream[mid]:
		start = mid + 1
	else :
		end = mid - 1 

if flag == 0:
	print ('element not present' )
