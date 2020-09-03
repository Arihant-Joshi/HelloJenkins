import sys

def main():
	name = "Jenkins User"
	count = 1
	if(len(sys.argv) == 3):
		count = int(sys.argv[2])
	if(len(sys.argv) == 2):
		name = sys.argv[1]

	for i in range(count):
		print("Hello~",str(name))

if __name__ == "__main__":
	main()