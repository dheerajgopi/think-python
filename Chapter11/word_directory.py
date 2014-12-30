def word_directory():

	fin = open('/home/dheeraj/think-python/words.txt')
	word_dir=dict()
	i = 0

	for line in fin:

		word=line.strip()
		i+=1
		word_dir[word]=i
	print word_dir
