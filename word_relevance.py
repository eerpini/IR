"""Program to calculate the relevancy of words and write out the relevance information.
The result of the computation is the square matrix ( in the case of 1-grams) which shows relevancy between each word.
done in a very inefficient way right now, uses a lot of memory since a dynamic list of all the distinct words is kept in memory."""
#TODO : we are not using n anywhere right now, that has to be changed
#TODO : we are not yet writing the output to a file
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
	#		print word+"     "+prev_word
			if prev_word == "":
				#this is the first word hence initialise
				rel_count[word]={}
				prev_word = word
				continue
			else:
			#the previous word must be present 
			#check if the previous word has already seen this word somewhere else
				if rel_count[prev_word].has_key(word):
	#				print prev_word + " has seen "+word
					rel_count[prev_word][word] = rel_count[prev_word][word] + 1
				else:
					rel_count[prev_word][word] = 1
			#add the current word to the matrix if it is not already present, update the relevance wrt to prev word and continue
				if not rel_count.has_key(word):
	#				print "The dict does not have "+word
					rel_count[word]={}
					rel_count[word][prev_word] = 1
			#check if the current word has already seen the previous word
				else:
					if rel_count[word].has_key(prev_word):
						rel_count[word][prev_word] = rel_count[word][prev_word] + 1
					else:
						rel_count[word][prev_word] = 1
			prev_word = word
	print_relevancy_matrix(rel_count)
	return rel_count

def print_relevant_words(rel_count, threshold):
	"""right now we just print all those groups of words which might have high correlation. The words in the groups might be repeated. we are not printing words which are not relevant to any other word"""
	for key in rel_count.keys():
		count = False
		for word in rel_count[key].keys():
			if rel_count[key][word] >= threshold:
				print word+" ",
				count = True
		if count : print key+" " 
	draw_graph(rel_count)

def draw_graph(rel_count):
	import networkx as nx
	import matplotlib.pyplot as plt
	g = nx.Graph()
	for key in rel_count:
		if not g.has_node(key):
			g.add_node(key)
			for word in rel_count[key]:
				if not g.has_node(key):
					g.add_node(word)
					g.add_edge(word,key, weight=rel_count[key][word])
				else:
					if not g.has_edge(word,key):
						g.add_edge(word,key, weight=rel_count[key][word])
	nx.draw_spring(g, node_size = 10, node_shape='s', alpha = 0.7, width = 1.3, with_labels = False )
	#plt.show()
	plt.savefig('graph_out.png')
