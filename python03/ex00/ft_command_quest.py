import sys
var = sys.argv
le = len(var)
print("=== Command Quest ===")
if le == 1:
	print("No arguments provided!")
	print(f"Program name: {var[0]}")
else:
	print(f"Arguments received: {le - 1}")
	for i in range(1, le):
		print(f"Argument {i}: {var[i]}")

print(f"Total arguments: {le}")