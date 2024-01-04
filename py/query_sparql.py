from rdflib import Graph
import json

url = "https://raw.githubusercontent.com/Irenko85/pokemon-rdf-data/dev/dataset/ttl/pokemon.ttl"
g = Graph()
g.parse(url, format="turtle")


PREFIXES = """
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX pkmn: <http://www.ex.org/#>
"""


sparql_query = PREFIXES + """
SELECT ?pokemonName ?uniqueAbility
WHERE {
  ?pokemon rdf:type pkmn:Pokemon ;
           pkmn:hasName ?pokemonName ;
           pkmn:hasAbility ?ability .

  OPTIONAL {
    ?otherPokemon rdf:type pkmn:Pokemon ;
                  pkmn:hasAbility ?ability .
    FILTER (?otherPokemon != ?pokemon)
  }

  FILTER (!bound(?otherPokemon))
  FILTER (lang(?pokemonName) = 'en')

  BIND (?ability AS ?uniqueAbility)
}
"""


results = g.query(sparql_query)

for row in results:
    # Aqui hay que printear los resultados dependiendo de la query
    print(row['pokemonName'], row['uniqueAbility'])
    pass
