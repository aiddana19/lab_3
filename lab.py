import os
import os.path

def Function():
	print('Press 1 to work with directories')
	print('Press 2 to work with files')
	print('Press 0 to exit')
def Directory():
	os.chdir('C://')
	curDirect=os.getcwd()
	print('Press 1 to rename directory')
	print('Press 2 to see the number of files in it')
	print('Press 3 to see the number of directories in it')
	print('Press 4 to list the content of directory')
	print('Press 5 to add file to the directory')
	print('Press 6 to add new directory to this directory')
	print('Press 0 to exit')
	a=int(input())
	if a==0:
		print("")
	elif a==1:
		print('Current directory is:',curDirect)
		v=str(input())
		os.chdir(v)
		curDirect=os.getcwd()
		print('New directory is:',curDirect)
	elif a==2:
		entries = os.listdir(curDirect)
		num=int(0)
		for entry in entries:
			if os.path.isfile(entry):
				num+=1
		print("Directory has", num, "files")
	elif a==3:
		print('Current directory is:',curDirect)
		entries=os.listdir(curDir)ect
		num=int(0)
		for entry in entries:
			if os.path.isdir(entry):
				num += 1
		print("Directory has", num, "directories")
	elif a==4:
		print('Current directory is:',curDirect)
		print("Directory has:", end='')
		for root, dirs, files in os.walk(curDirect):
			print(files)
	elif a==5:
		print('Current directory is:',curDirect)
		print("Enter the name of file:")
		v=str(input())
		g=open(v+'.txt','w')
		g.close()
		print("File created")
	elif a==6:
		print('Current directory is:',curDir)ect
		print("Enter the name of directory:")
		v=str(input())
		os.mkdir(v)
		print("Directory created")

def Files():
    print('Press 1 to rename file ')
    print('Press 2 to add content to the file')
    print('Press 3 to rewrite content of the file')
    print('Press 4 to delete file')
    print('Press 5 to return to the parent directory')
    print('Press 0 to exit')
    a=int(input())
    if a==0:
    	Function()
    elif a==1:
    	print("Enter the file name:")  
    	st=str(input()+'.txt')
    	st1=str(input()+'.txt')
    	if os.path.exists(st):
    		os.rename(st,st1)
    		print("File name was changed")
    	else:
    		print("There is no file with the same name in directory")
    elif a==2:
    	print("Enter the file name:")
    	st=str(input()+'.txt')
    	print("Enter the content:")
    	f=open(st,'a')
    	st1=input()
    	f.write(st1)
    	f.close()
    	print("Content was added")
    elif a==3:
    	print("Enter the file name:")
    	st=str(input()+'.txt')
    	if os.path.exists(st):
    		os.remove(st)
    		print("Enter the content:")  
    		f=open(st,'a')
    		st1=input()
    		f.write(st1)
    		f.close()
    		print("Content was added")
    	else:
    		print("There is no such file")
    elif a==4:
    	print("Enter the file name:")
    	st=str(input()+'.txt')
    	if os.path.exists(st):
    		os.remove(st)
    		print("File succesfuly deleted")
    	else:
    		print("There is no such file")
    elif a==5:
        os.chdir('C://')

start=True
while start:
    Function()
    a=int(input())
    if a==0:
        start=False 
    elif a==1:
        Directory()
    elif a==2:
    	Files()


