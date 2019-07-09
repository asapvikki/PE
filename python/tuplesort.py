lst = []
print ("enter the no of tuples to be entered")
k = int(input())
i = 0
while (i<k):
    print ("enter the tuple")
    x = input()
    x = x.split()
    x = tuple(x)
    lst.append(x)
    i = i + 1
output = sorted(lst, key=lambda x:x[-1])
print(output)

