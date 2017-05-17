import BioNetwork

#little demo for the network object
mynetwork=BioNetwork.BioNetwork()

#sample nodes
newnodes=["A","B","C","D","E"]
for i in newnodes:
	mynetwork.add_node(i)
print("added 5 nodes")
mynetwork.print_network()


mynetwork.add_edge(3,2)
mynetwork.add_edge(4,1)
mynetwork.add_edge(2,2)

print("added 3 edges")
mynetwork.print_network()
