import sys, math
var = (sys.argv)
if len(var) != 4:
	print("We need exactly 3 arguments (x, y, z)")
else:
	my_list = []
	dis = 0
	flag = True
	for i in var[1:]:
		try:
			my_list.append(int(i))
		except ValueError as error:
			print(f"Wrong input -> {error}")
			flag = False
			

	if flag == True:
		dis = int(math.sqrt((my_list[0]-0)**2 + (my_list[1]-0)**2 + (my_list[2]-0)**2))
		my_tuple = tuple(my_list)
		print(f"Position created: {my_tuple}")
		print(f"Distance between (0, 0, 0) and {my_tuple}: {float(dis)}")
	



