"""Program for calculating the word co occurrence in a given input file
	arguments : 
		input file 
		temporary file with non alphanumeric characters removed (set to temp_file.txt)
		output file which contains the world relevancy matrix (set to word_relevance.txt)
		the value of n (the n-gram size for relevancy computations, set to 1 by default)"""
import filter_text
import word_relevance
import sys
import string


if (len(sys.argv)!=2):
	print "Expect the input files as an argument"
	sys.exit(1)

filter_text.remove_non_printable(sys.argv[1],"new_output.txt")
