"""Program to calculate the relevancy of words and write out the relevance information.
The result of the computation is the square matrix ( in the case of 1-grams) which shows relevancy between each word.
done in a very inefficient way right now, uses a lot of memory since a dynamic list of all the distinct words is kept in memory."""
#TODO : we are not using n anywhere right now, that has to be changed
import string 

def get_distinct_words(input_fh, n):
	word_list = []
	for line in input_fh:
		for word in line.split():
			if word not in word_list:
				word_list.append(word)
	input_fh.seek(0)
	return word_list

def print_relevancy_matrix(rel_count):
	print rel_count

def calculate_correlation(input_file, n):
	input_fh = file(input_file)
	distinct_words = get_distinct_words(input_fh, n)
	rel_count = {}
	prev_word = ""
	for line in input_fh:
		for word in line.split():
			print word+"     "+prev_word
			if prev_word == "":
				#this is the first word hence initialise
				rel_count[word]={}
				prev_word = word
				continue
			else:
			#the previous word must be present 
			#check if the previous word has already seen this word somewhere else
				if rel_count[prev_word].has_key(word):
					print prev_word + " has seen "+word
					rel_count[prev_word][word] = rel_count[prev_word][word] + 1
				else:
					rel_count[prev_word][word] = 1
			#add the current word to the matrix if it is not already present, update the relevance wrt to prev word and continue
				if not rel_count.has_key(word):
					print "The dict does not have "+word
					rel_count[word]={}
					rel_count[word][prev_word] = 1
			#check if the current word has already seen the previous word
				else:
					if rel_count[word].has_key(prev_word):
						rel_count[word][prev_word] = rel_count[word][prev_word] + 1
					else:
						rel_count[word][prev_word] = 1
			prev_word = word
	print rel_count
	print_relevancy_matrix(rel_count)
	return rel_count

