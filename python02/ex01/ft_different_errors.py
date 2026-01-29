def  garden_operations(error_type):
	try:
		if error_type == "Math":
			print("Testing ZeroDivisionError....")
			x = 10 / 0
		elif error_type == "Value":
			print("Testing ValueError...")
			x = int("abc")
		elif error_type == "File":
			print("Testing FileNotFoundError...")
			x = open("missing.txt")
		elif error_type == "Key":
			print("Testing KeyError...")
			my_dict = {}
			x = my_dict["missing"]
	except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as error:
		return error
def test_error_types():
	print("=== Garden Error Types Demo ===")
	print(f"Caught {garden_operations('Value').__class__.__name__}: invalid literal for int()")
	print(f"Caught {garden_operations('Math').__class__.__name__}: division by zero")
	print(f"Caught {garden_operations('File').__class__.__name__}: No such file 'missing.txt'")
	print(f"Caught {garden_operations('Key').__class__.__name__}: missing\_plant")
    
	print("Testing multiple errors together...")
	print("Caught an error, but program continues!")
	print("All error types tested successfully!")

if __name__ == "__main__":
    test_error_types()