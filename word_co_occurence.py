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


if (len(sys.argv)<2):
	print "Expect the input file as an argument"
	sys.exit(1)
if(len(sys.argv) >= 3):
	temp_file = sys.argv[2]
else:
	temp_file = "temp_file.txt"
if(len(sys.argv) >= 4):
	output_file = sys.argv[3]
else:
	output_file = "output_file.txt"
if(len(sys.argv) >= 5):
	n = string.atoi(sys.argv[4])
else:
	n = 1
filter_text.remove_non_printable(sys.argv[1],temp_file)
word_relevance.calculate_correlation(temp_file, n)

