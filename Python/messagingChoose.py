import messagingClient as mC
import messagingServer as mS

def Main():
	while True:
		print("\n[1] FOR CLIENT")
		print("[2] FOR SERVER")
		sel = input("\n-> ")
		if sel == 1:
			mC.Main()
		elif sel == 2:
			mS.Main()
		else:
			print("-" * 50 + "\n")
			continue


if __name__ == "__main__":
	Main()