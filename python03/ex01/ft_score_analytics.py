import sys
print("=== Player Score Analytics ===")
var = sys.argv
if len(var) == 1:
	print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
	my_list = []
	total_score = 0
	max_score = 0
	for x in var[1:]:
		try:
			my_list.append(int(x))
		except ValueError:
			print(f"oops wrong input: {x}")
	l = len(my_list)
	if my_list != []:	
		print(f"Scores processed: {my_list}")
		print(f"Total players: {l}")
		print(f"Total score: {sum(my_list)}")
		print(f"Average score: {sum(my_list) / l}")
		print(f"max score: {max(my_list)}")
		print(f"Low score: {min(my_list)}")
		print(f"Score range: {max(my_list) - min(my_list)}")