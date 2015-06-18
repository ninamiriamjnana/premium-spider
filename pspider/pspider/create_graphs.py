
from peeweemodels import *
import networkx as nx



def create_u_dict():
	myquery=(User.select(User.id,Topic.id.alias('topic_id')).join(Post).join(Topic).naive().order_by(User.id))
	start=myquery[0]
	start_id=start.id
	udict={}
	user_list=[]
	
	for x in myquery:
		if(x.id==start_id):
			user_list.append(x.topic_id)
			alte_id=x.id
		else:
			udict['alte_id']=user_list
			user_list=[]
			user_list.append(x.topic_id)
			start_id=x.id
	return udict


def compare (G, udict, such_user, such_topic):
	for k, v in udict.iteritems():
		for vergleich_topic in v:
			if vergleich_topic==such_topic and such_user != k:
				if nx.path.bidirectional.djikstra(G, such_user, k):
					G['such_user']['k']['weight']+=1
				else:
					G.add_edge(such_user, k, weight=1)
	return G
	

def create_u_graph(udict):

	G=nx.Graph()
	
	for k, v in udict.iteritems():
		G.add_node(k)
		for topic in v:
			G=vergleich(G,udict,k, topic)
	
