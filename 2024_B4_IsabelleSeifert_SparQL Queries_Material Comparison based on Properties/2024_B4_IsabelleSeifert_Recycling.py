import rdflib
from rdflib.namespace import RDFS
from rdflib.plugins.sparql import prepareQuery

# Namespaces
SKOS = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
RDFS = rdflib.namespace.RDFS
XSD = rdflib.namespace.XSD
OWL = rdflib.namespace.OWL
DBP = rdflib.Namespace("https://dbpedia.org/page/")
DBPP = rdflib.Namespace("https://dbpedia.org/property/")
BSDD = rdflib.Namespace("https://identifier.buildingsmart.org/")
FCL = rdflib.Namespace("https://www.freeclass.de/")
OBD = rdflib.Namespace("https://www.oekobaudat.de/OEKOBAU.DAT/resource/processes/")

# Load RDF data
g = rdflib.Graph()
g.bind("skos", SKOS)
g.bind("rdfs", RDFS)
g.bind("xsd", XSD)
g.bind("owl", OWL)
g.bind("dbp", DBP)
g.bind("dbpp", DBPP)
g.bind("bsdd", BSDD)
g.bind("fcl", FCL)
g.bind("obd", OBD)

# Path to RDF file
file_path = r"C:\2024_B4_IsabelleSeifert_RDF_Concrete.ttl"
g.parse(file_path, format="turtle")

# Define the SPARQL query
query_str = """
    PREFIX bsdd: <https://identifier.buildingsmart.org/> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    PREFIX dbp: <https://dbpedia.org/page/> 
    PREFIX dbpp: <https://dbpedia.org/property/> 
    PREFIX fcl: <https://www.freeclass.de/> 
    PREFIX obd: <https://www.oekobaudat.de/OEKOBAU.DAT/resource/processes/> 

    SELECT ?label ?gwpTotal ?recycledStatus
    WHERE {
        {
            ?instance 
                <https://identifier.buildingsmart.org/uri/Al-Qazzaz/Circularity/0.0.1/prop/Recycled> "yes" ;
                <https://identifier.buildingsmart.org/uri/buildingsmart/ifc/4.3/class/Pset_ConcreteElementGeneral/prop/Pset_ConcreteElementGeneral/StrengthClass> "C25/30" ;
                <https://identifier.buildingsmart.org/uri/LCA/LCA/3.0/prop/GWP_total> ?gwpTotal ;
                rdfs:label ?label .
            BIND("yes" AS ?recycledStatus)
        }
        UNION
        {
            ?instance 
                <https://identifier.buildingsmart.org/uri/buildingsmart/ifc/4.3/class/Pset_ConcreteElementGeneral/prop/Pset_ConcreteElementGeneral/StrengthClass> "C25/30" ;
                rdfs:label ?label .
            OPTIONAL {
                ?instance <https://identifier.buildingsmart.org/uri/Al-Qazzaz/Circularity/0.0.1/prop/Recycled> ?recycled .
            }
            FILTER (!bound(?recycled))
            OPTIONAL {
                ?instance <https://identifier.buildingsmart.org/uri/LCA/LCA/3.0/prop/GWP_total> ?gwpTotal .
            }
            BIND("no" AS ?recycledStatus)
        }
    }
"""

# Prepare the query
query = prepareQuery(query_str)

# Execute the SPARQL query
result = g.query(query)

# Print the results
for row in result:
    print(f"{row.label}, GWP Total: {row.gwpTotal if row.gwpTotal else 'Not available'}, Recycled: {row.recycledStatus}")
