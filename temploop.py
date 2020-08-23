# __author__ = 'chaotic braindead'
from os import system, name
from time import sleep
def clear():
	# lines 8-10 are commented as this script is meant for the Raspbian Operating System.
	# stole this from some unnamed user on geeksforgeeks: https://www.geeksforgeeks.org/clear-screen-python/
	"""
	if name == 'nt':
		_ = system('cls')
	else:
	"""
	_ = system('clear')
print("To terminate the script, press Ctrl+C.\nThis message will disappear in 5 seconds.")
sleep(5)
while 3 > 2:
	clear()
	_ = system('vcgencmd measure_temp') # displays the temperature
	sleep(1)
#end
