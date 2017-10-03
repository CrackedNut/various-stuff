#! /usr/bin/env python

""" Find the real bit architecture
"""

with open("/proc/cpuinfo") as f:
	for line in f:
		if line.strip():
			if line.rstrip("\n").startswith("flags") or line.rstrip("\n").startswith("Features"):
				if "lm" in line.rstrip("\n").split():
					print("64-bit")
				else:
					print("32-bit")
