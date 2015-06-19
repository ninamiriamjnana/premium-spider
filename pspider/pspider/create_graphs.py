
from peeweemodels import *
import networkx as nx
import ipdb
import collections

import matplotlib.pyplot as plt



def create_u_dict():
	myquery=(User.select(User.id, User.name,Topic.id.alias('topic_id')).join(Post).join(Topic).naive().order_by(User.id))
	start=myquery[0]
	start_id=start.id
	udict={}
	user_list=[]

	uname_dict={}

	helper=0

	counter=myquery.count()

	for x in myquery:
		#ipdb.set_trace()
		uname_dict[x.id]=x.name
		helper+=1
		
		if(x.id==start_id):

						
			user_list.append(x.topic_id)
			alte_id=x.id	
			first=0

		elif x.id!=start_id and first==1: # in this case we have to save the user_list to dict
			udict[start_id]=user_list
			user_list=[]
			user_list.append(x.topic_id)
			start_id=x.id
			first=1
			
		elif x.id!=start_id and first==0: 
			#ipdb.set_trace()			
			udict[alte_id]=user_list
			user_list=[]
			user_list.append(x.topic_id)
			start_id=x.id
			first=1
	if(x.id==start_id):
		user_list.append(x.topic_id)
		udict[x.id]=user_list
	#ipdb.set_trace()
	dictcollection=collections.namedtuple('dictcollection', ['udict','uname_dict'])
	dc=dictcollection(udict, uname_dict)
	return dc





def compare (G, udict, such_user, such_topic):
	for k, v in udict.iteritems():
		for vergleich_topic in v:
			if vergleich_topic==such_topic and such_user != k:
				#ipdb.set_trace()
				if G.has_edge(such_user,k):
					G[such_user][k]['weight']+=1
				else:
					G.add_edge(such_user, k, weight=1)
	return G
	

def create_u_graph():
	dc=create_u_dict()
	
	udict=dc[0]
	unamedict=dc[1]
	
	G=nx.Graph()
	
	for k, v in udict.iteritems():
		G.add_node(k)
		name=unamedict[k]
		G.node[k]['name']=name
		# wie krieg ich jetzt den namen dazu?
		for topic in v:
			G=compare(G,udict,k, topic)

	return G


def draw_u_graph(G, unamedict):
	elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight']>50]
	esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight']<=50]

	pos=nx.spring_layout(G)

	nx.draw_networkx_nodes(G, pos, node_size=700, with_labels=False)
	#ipdb.set_trace()
	nx.draw_networkx_labels(G,pos, unamedict)
	
	nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
	nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, style='dashed')

	plt.axis('off')
	plt.show()

	
	
	
	
