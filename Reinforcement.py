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

# Load the RDF data
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

# Path to the RDF file
file_path = r"RDF_Concrete.ttl"
g.parse(file_path, format="turtle")

# Define the SPARQL query with addition of the result
query = prepareQuery("""
    PREFIX bSDD: <https://identifier.buildingsmart.org/> 
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 
    PREFIX owl: <http://www.w3.org/2002/07/owl#> 
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
    PREFIX dbp: <https://dbpedia.org/page/> 
    PREFIX dbpp: <https://dbpedia.org/property/> 
    PREFIX fcl: <https://www.freeclass.de/> 
    PREFIX obd: <https://www.oekobaudat.de/OEKOBAU.DAT/resource/processes/> 

    SELECT ?finalGWP ?gwpTotal WHERE {
        BIND(2400 * 0.025 AS ?densityWithReinforcement)
        BIND(?densityWithReinforcement * 0.763693331 AS ?intermediateResult)
        
        <https://www.oekobaudat.de/OEKOBAU.DAT/resource/processes/6739667a-49d1-4a9c-a4b2-eb542167710c?version=20.23.050> 
            <https://identifier.buildingsmart.org/uri/LCA/LCA/3.0/prop/GWP_total> ?gwpTotal .

        BIND(?intermediateResult + ?gwpTotal AS ?finalGWP)
    }
""")

# Execute the SPARQL query
result = g.query(query)

# Print the final result of the query
for row in result:
    print("Total GWP:", row.gwpTotal)
    print("Total GWP with reinforcement:", row.finalGWP)

