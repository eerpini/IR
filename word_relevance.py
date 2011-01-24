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
			if word == "Phil":
				print word + "<<<>>>" + prev_word
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
	draw_graph(rel_count, threshold)

def draw_graph(rel_count, threshold):
	import networkx as nx
	import matplotlib
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
	print g.nodes()
	#lets separate the edges here
	edges_above_threshold = [(u,v) for (u,v,d) in g.edges(data = True) if d['weight']>=threshold]
	edges_below_threshold = [(u,v) for (u,v,d) in g.edges(data = True) if d['weight']<threshold]
	plt.figure(figsize=(100,100))
	plt.axis('off')
	#colors=range(g.number_of_edges())
	pos = nx.spring_layout(g)
	nx.draw(g, pos,  node_size = 2000, node_color = '#A0CBE2', node_shape='o', alpha = 0.7, width = 4.0, edgelist= edges_above_threshold, edge_color = 'blue', edge_cmap = plt.cm.Blues,  with_labels = True)
	nx.draw_networkx_edges(g, pos, edgelist = edges_below_threshold, width = 2.0, alpha = 0.4, edge_color = 'red', style = 'solid')
	plt.savefig('graph_out.png')
	#plt.show()
