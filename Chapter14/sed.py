import os

def sed(pattern,replace,file1,file2):

	fin = open(file1,'r')
	fout = open(file2,'w')

	for i in fin:

		line = i.replace(pattern,replace)
		fout.write(line)

	fout.close()
	fin.close()


sed('%s','Dheeraj','/home/dheeraj/repos/think-python/f3.txt','/home/dheeraj/repos/think-python/f2.txt')
