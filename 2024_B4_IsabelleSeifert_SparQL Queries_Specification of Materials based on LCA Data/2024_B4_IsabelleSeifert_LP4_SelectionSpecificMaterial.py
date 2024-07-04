import rdflib

# Create a graph
g = rdflib.Graph()

# Path to the RDF file
file_path = r"C:\2024_B4_IsabelleSeifert_RDF_Concrete.ttl"

# Parse the RDF data
g.parse(file_path, format="turtle")

# Define the SPARQL query
query = """
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?classLabel ?instanceLabel ?instanceURI
WHERE {
    ?class skos:narrowMatch <https://www.oekobaudat.de/OEKOBAU.DAT/resource/processes/d2ae1721-bb2a-4386-9d9f-abb1c774b0a8?version=20.23.050> ;
           rdfs:label ?classLabel .
    ?instance a ?class ;
              rdfs:label ?instanceLabel ;
              <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?instanceURI .
}
"""

# Execute the query
results = g.query(query)

# Print the results
for row in results:
    print(f"Class: {row.classLabel}, Instance: {row.instanceLabel}, URI: {row.instanceURI}")



