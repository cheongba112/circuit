import time

current = time.localtime()
datedata = time.strftime("%Y-%m-%d", current)
timedata = time.strftime("%H-%M-%S", current)

if __name__ == '__main__':
	print(datedata, timedata)
