# 3/5/23

# the three addresses given in the assignment directions
addr1 = 19986
addr2 = 347892
addr3 = 5978

# the function take in as a parameter the address and outputs to the terminal
# and to an output file the page number and the offset for a system with 
# a 32-bit virtual memory address with 4-KB page size. 
def output_page(address):
	
	# 4 KB = 4096 Bytes 
	page = address // 4096 # rounded division to return an integer value 
	offset = address % 4096 # modulo to find the offset 
	
	# create the strings output 
	str1 = "The address " + str(address) + " is in:\n"
	str2 = "  Page number = " + str(page) + "\n"
	str3 = "  Offset = " + str(offset) + "\n\n"
	
	#output to terminal
	print(str1 + str2 + str3)
	
	#output to file 
	f.write(str1)
	f.write(str2)
	f.write(str3)

# main function of program 
if __name__ == "__main__":
	
	# create the output file
	f = open("output.txt", "w")
	
	# create output file introductory string
	intro = "Assignment 4\nMarch 5, 2023\n\n"
	
	# output introductory string to terminal 
	print(intro)
	
	# output introductory string to file 
	f.write(intro)
	
	# call the function and pass the three addresses 
	output_page(addr1)
	output_page(addr2)
	output_page(addr3)
	
	# close the output file 
	f.close() 
