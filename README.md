# Semantic-Web-linking-LCA-Database-to-IFC-Model
This is serving as an example on how the IFC structure can be linked to data in other Databases. It can be used to enrich a BIM Modell with relevant information.
In this case the Databases used are ÖKOBAUDAT, buildingSMART Data Dictionary, FreeClass and DBPedia.

For further details refere to 2024_B4_IsabelleSeifert_WrittenDocumentation.

RDF Turtle File:

	2024_B4_IsabelleSeifert_RDF_Concrete.ttl


RDF Turtle File simplified (for better redability usiing Prefixes. Can´t be queried sufficiently. Use the non simplified file for queries.):

	2024_B4_IsabelleSeifert_RDF_ConcreteSimplified.ttl


Visual Illustration of the Semantic Web:

	2024_B4_IsabelleSeifert_SematicWeb_Illustrated.pdf
To excecute the script the import of rdflib, networkx as nx and ipycytoscape are necessary.


Examplary SparQL queries:

	Material Comparison based on Properties:
	
		2024_B4_IsabelleSeifert_Recycling.py
		2024_B4_IsabelleSeifert_Reinforcement.py


	Specification of Materials based on LCA Data:
	
		2024_B4_IsabelleSeifert_LP1_AverageGWP.py
		2024_B4_IsabelleSeifert_LP3_MaterialConcretisation.py
		2024_B4_IsabelleSeifert_LP4_SelectionSpecificMaterial.py
  
To be able to execute the queries, the download of the rdflib is required.
