
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():
     
	folder = r"C:\Users\FATIMANOOR\Desktop\Animal"
	for count, filename in enumerate(os.listdir(folder)):
		dst = f"{str(count+1)}.jpg"
		src =f"{folder}/{filename}" # foldername/filename, if .py file is outside folder
		dst =f"{folder}/{dst}"
		
		# rename() function will
		# rename all the files
		os.rename(src, dst)

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()
