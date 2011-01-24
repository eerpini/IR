"""Formats the given file and removes all non alphanumeric characters, the output is written
to output.txt"""
import string
alphanum = [ i for i in string.printable if i.isalnum()]
#print alphanum
def remove_non_printable(input_file,output_file="output.txt"):
	input_fh = file(input_file)
	output_fh = file(output_file,"w")
	prev_ch = ''
	for line in input_fh:
		for ch in line:
			if ch in ['!','$','%','&','~','.',',',';',':','\"','?','/','(',')']:
				if prev_ch != ' ':
					output_fh.write(' ')
					prev_ch = ' '
			else:
				if ch in alphanum:
					output_fh.write(string.lower(ch))
					prev_ch = ch
				if ch == ' ':
					if prev_ch != ' ':
						output_fh.write(string.lower(ch))
						prev_ch = ' '
