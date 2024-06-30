# Semantic-Web-linking-LCA-Database-to-IFC-Model
This is serving as an example on how the IFC structure can be linked to data in other Databases. It can be used to enrich a BIM Modell with relevant information.
In this case the Databases used are ÖKOBAUDAT, buildingSMART Data Dictionary, FreeClass and DBPedia.


RDF Turtle File:

	RDF_Concrete.ttl


RDF Turtle File simplified (for better redability usiing Prefixes. Can´t be queried sufficiently. Use the non simplified file for queries.):

	RDF_ConcreteSimplified.ttl


Visual Illustration of the Semantic Web:

	SematicWeb_Illustrated.pdf


Examplary SparQL queries:

	Material Comparison based on Properties:
	
		Recycling.py
		Reinforcement.py


	Specification of Materials based on LCA Data:
	
		LP1_AverageGWP.py
		LP3_MaterialConcretisation.py
		LP4_SelectionSpecificMaterial.py

