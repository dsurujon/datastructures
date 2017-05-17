import BioNetworkNode
import BioNetworkEdge

class BioNetwork(object):
	def __init__(self, nodes=[], edges=[]):
		self.nodes=nodes
		self.edges=edges
		self.node_number=len(nodes)
		self.edge_number=len(edges)
		
	def add_node(self, data):
		#construct the node and put it on the nodes list
		newnode=BioNetworkNode.BioNetworkNode(data, index=self.node_number)
		self.nodes.append(newnode)
		self.node_number+=1
	
	#construct an edge between two nodes.
	def add_edge(self,node1_ix,node2_ix,direction=False):
		#construct the edge and put it on the edges list
		node1=self.nodes[node1_ix]
		node2=self.nodes[node2_ix]
		newedge=node1.add_neighbor(node2, self.edge_number)
		self.edges.append(newedge)
		self.edge_number+=1
		
	def print_network(self,format="sif"):
	#print out nodes and edges n a cytoscape-readable
	#format
		if format=="sif":
			#node1  relationship node2
			for node in self.nodes:
				if node.edges==[]:
					print(node.index)
				else:
					for i in range(0,len(node.edges)):
						edge_ix=node.edges[i]
						edge=self.edges[edge_ix]
						print(node.index,edge.type,node.neighbors[i])

		elif format=="nnf":
		#make a nested network formatted version
		#or other acceptable formats
			pass