#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: ZhangChunsheng
import fnmatch;
import os;
import sys;

#function used to get all specific files
#return a generator
def getFileList(initDir = ".", formats = "*"):
    for dirpath, dirnames, fname in os.walk(initDir):
        for fn in fnmatch.filter(fname, formats):
            yield os.path.join(dirpath, fn).replace("\\", "/");


#change file encoding,be sure to make a backup
def changeFileEncoding(folder, fromEncoding = 'gbk', toEncoding = 'utf-8', formats = "*"):
    for i in getFileList(folder, formats):
        print("processing " + i);
        with open(i, 'r', encoding = fromEncoding) as f:
            tmpcon = f.read();
            #print(tmpcon);
            f.close();
        with open(i, 'w', encoding = toEncoding) as f:
            f.write(tmpcon);
            f.close();

def convert(filename, in_enc = "GBK", out_enc = "UTF-8"):
	# read the file
	fp = open(filename);
	content = fp.read();
	fp.close();
	# convert the concent
	try:
		new_content = content.decode(in_enc).encode(out_enc);
		#write to file
		fp = open(filename, 'w');
		fp.write(new_content);
		fp.close();
	except:
		print " error... ";

def explore(dir, formats):
	for root, dirs, files in os.walk(dir):
		for file in fnmatch.filter(files, formats):
			path = os.path.join(root, file);
			print "convert " + path,
			convert(path, "gbk", "utf-8");
			print " done";

def main():
	if(len(sys.argv) > 1):
		path = sys.argv[1];
	else:
		changeFileEncoding('./chinese', 'gb2312', 'utf-8', '*.html');#python3.*
		
	if(os.path.isfile(path)):
		convert(path);
	elif(os.path.isdir(path)):
		explore(path, "*.html");

if __name__ == "__main__":
	main();