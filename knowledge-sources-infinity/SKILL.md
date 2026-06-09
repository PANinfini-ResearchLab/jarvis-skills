---
name: knowledge-sources
description: Curated catalog of open, machine-queryable knowledge sources. Use
  whenever the agent needs external factual data and must pick WHERE to get it.
---

# Knowledge Sources — Open Data Catalog

## Rules
1. Prefer keyless sources — no API key = no dependency, no rate-limit surprise
2. Cite source + retrieval date in every response
3. Meaningful User-Agent (project name + contact)
4. Cache locally when possible (pairs with rag-local)
5. Source unavailable → say so ; never substitute memory for a failed call

## Academic

| Source          | Endpoint pattern                                              | Key needed |
|-----------------|---------------------------------------------------------------|------------|
| arXiv           | https://export.arxiv.org/api/query?search_query=...           | No         |
| OpenAlex        | https://api.openalex.org/works?filter=...                     | No         |
| Crossref        | https://api.crossref.org/works?query=...                      | No         |
| Zenodo          | https://zenodo.org/api/records?q=...                          | No (read)  |
| HAL             | https://api.archives-ouvertes.fr/search/?q=...                | No         |
| ORCID (public)  | https://pub.orcid.org/v3.0/<orcid-id>/works                   | No         |
| PubMed          | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi    | No         |
| Semantic Scholar | https://api.semanticscholar.org/graph/v1/paper/search?query= | No         |

## General knowledge

| Source    | Endpoint pattern                                              | Key needed |
|-----------|---------------------------------------------------------------|------------|
| Wikipedia | https://en.wikipedia.org/api/rest_v1/page/summary/<title>    | No         |
| Wikidata  | https://query.wikidata.org/sparql?query=...                   | No         |
| DBpedia   | https://dbpedia.org/sparql?query=...                          | No         |

## Practical / real-world

| Source      | Endpoint pattern                                            | Key needed |
|-------------|-------------------------------------------------------------|------------|
| Open-Meteo  | https://api.open-meteo.com/v1/forecast?...                  | No         |
| Overpass    | https://overpass-api.de/api/interpreter?data=...            | No         |
| Nominatim   | https://nominatim.openstreetmap.org/search?q=...            | No (1 r/s) |
| World Bank  | https://api.worldbank.org/v2/country/.../indicator/...      | No         |
| GitHub API  | https://api.github.com/...                                  | No (60/h)  |

## Rate-limit patterns
- Nominatim : 1 req/s, User-Agent required, no bulk
- Wikidata SPARQL : back-off on 429, prefer small queries + pagination
- arXiv : 3s between requests recommended
- GitHub anonymous : 60 req/h — use token for higher limits
