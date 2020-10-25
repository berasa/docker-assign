import os,socket

#Define variables
sum_count = 0
curr_max_file_len = 0
curr_max_file = 'Something'
max_len_filename = 'Something'


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

f = open("/home/output/result.txt", "a")

f.write('IP Address: ' + ip_address + '\n')	
f.write('List of file names in directory: ' '\n')		


#print('IP Address: ', ip_address)

for root, dirs, files in os.walk("."):
	for filename in files:
		f.write(filename +'\n')
		
		#print(filename)
		#print('Number of words in file ' ,filename,':', len(words))
		#print(sum_count)

for root, dirs, files in os.walk("."):
	for filename in files:
		file = open(filename,"rt")
		data = file.read()
		words =data.split()

		prev_file_word_count = len(words)
		sum_count = sum_count + len(words)
		f.write('Number of words in file ' +filename +': ' + str(len(words)) + '\n')

		if curr_max_file_len <= len(words):
			curr_max_file_len = len(words)
			curr_max_file = filename


f.write('Sum of All words in Files: ' + str(sum_count) +'\n')		
f.write('File having max words: ' + curr_max_file +'\n')		

f.close()

#open and read the file after the appending:
f = open("/home/output/result.txt", "r")
print(f.read())

