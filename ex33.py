i = 0
nubmers = []

while i < 6:
	print('At the top i is %d' % i)
	nubmers.append(i)

	i = i + 1
	print('Numbers now: ', nubmers)
	print('At the bottom i is %d' % i)


print('The numbers: ')

for num in nubmers:
	print(num)