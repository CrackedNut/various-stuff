import subprocess

class getinputs():
	def __init__(self):
		self.version = 1.0

	def getxinputs(self):
		results = subprocess.run(["xinput", "--list"], stdout = subprocess.PIPE)
		results = results.stdout.decode("utf-8").split("\n")
		for result in results:
			print(result)

def Main():
	gti = getinputs()
	gti.getxinputs()