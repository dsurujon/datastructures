import BioNetworkNode

class BioNetworkEdge(object):
	"edge class"
	def __init__(self, node1, node2, index, direction=False, metadata=None,type="1"):
		self.node1=node1
		self.node2=node2
		self.index=index
		self.direction=direction
		self.metadata=metadata
		#depending on the format of the metadata, 
		#can write a simple parser
		
		#evidence for forming the edge, could be
		# PubMed IDs for example
		self.evidence=[]
		self.weight=self.get_weight()
		
		#allow edges to have multiple types e.g. 
		#protein-protein interaction, transcription 
		#factor, inhibitor etc. 
		self.type=type
		#can decorate the edge even more with 
		#fields such as creator, date created etc.
		
	def get_weight(self):
		#could get much fancier with this metric
		#but a simple example is to give an edge
		#more weight if there's more paper about
		#the interaction.
		return len(self.evidence)
		