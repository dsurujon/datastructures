import BioNetworkEdge

class BioNetworkNode(object):
	"Generic node."
	def __init__(self, data, index, category="gene", neighbors=None, metadata=None):
		#allow nodes to have different categories: gene, function, protein complex, metabolite etc.
		self.category=category
		#data could be gene name/locus tag or could have more sub-fields. 
		#It could even be another BioNetwork object. 
		self.data = data
		#each node in a graph should have a unique index 
		self.index = index
		#set of neighbors. could be empty.
		self.neighbors = []
		#the neighbors are just the indices of the neighboring nodes
		#the list of edge indices will point to BioNetworkEdge 
		#objects with much more detailed information
		self.edges=[]
		if neighbors is not None:
			for n in neighbors:
				newedge=self.add_neighbor(n)
				self.edges.append(newedge.index)
				n.edges.append(newedge.index)
		self.metadata=metadata
		#depending on the format of the metadata, 
		#can write a simple parser
		
	def add_neighbor(self, node, edgeindex, direction=False):
		#in an undirected graph, we can define the edge by connecting both nodes to each other
		#also make sure not to count self-to-self connections multiple times
		if direction==False and node.index!=self.index:
			self.neighbors.append(node.index)
			node.neighbors.append(self.index)
			self.edges.append(edgeindex)
			node.edges.append(edgeindex)
		else:
			self.neighbors.append(node.index)
			self.edges.append(edgeindex)
			
		return BioNetworkEdge.BioNetworkEdge(self,node,edgeindex)



