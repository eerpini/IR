"""Formats the given file and removes all non alphanumeric characters, the output is written
to output.txt"""
import string
alphanum = [ i for i in string.printable if i.isalnum()]
#print alphanum
def remove_non_printable(file_name,output_file_name="output.txt"):
	in_file = file(file_name)
	filtered_file = file(output_file_name,"w")
	for line in in_file:
		for ch in line:
			if ch in alphanum or ch==' ':
				filtered_file.write(ch)	
