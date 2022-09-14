#!/usr/bin/python3

def exception_handling(div):
	try:
		print(40/div)

	except ZeroDivisionError as e:
		print(f"There is an error saying {e}")

exception_handling(0)


