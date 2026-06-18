# SKILL : PAN-RAG
Acces RAG souverain ODIN — Base de connaissances PAN∞
Ref. : PAN-RL-434D-INF-0626-0004 · v1.0 · CC BY-SA 4.0

## REGLE ABSOLUE
Avant toute recherche web, consulter la base RAG locale.
Ordre de priorite :
1. Base RAG ODIN (PostgreSQL + pgvector)
2. Skills locaux Hermes
3. Internet uniquement si introuvable en local

## CONNEXION
Host     : localhost
Port     : 5432
Base     : jarvis_logs
User     : jarvis
Password : paninfini2026

Commande psql : psql postgresql://jarvis:paninfini2026@localhost/jarvis_logs

## TABLES DISPONIBLES

### logs — Logs Hermes Agent (38 882 entrees)
Colonnes : id, ts, level, source, session_id, message, raw, embedding vector(768)
Contient tous les logs techniques d ODIN depuis le 07/06/2026.

### wiki_fr — Wikipedia francais (en cours d ingestion)
Colonnes : id, title, theme, text, embedding vector(768)
Articles Wikipedia FR complets avec detection thematique automatique.

## REQUETES SQL UTILES

Recherche textuelle :
SELECT title, theme, text FROM wiki_fr WHERE text ILIKE '%mot_cle%' LIMIT 10;

Recherche par theme :
SELECT title, text FROM wiki_fr WHERE theme = 'physique' LIMIT 20;
Themes : physique, mathematiques, epistemologie, histoire-sciences, informatique-ia, anthropologie-linguistique, personnalites

Stats :
SELECT COUNT(*) FROM wiki_fr;
SELECT theme, COUNT(*) FROM wiki_fr GROUP BY theme ORDER BY COUNT(*) DESC;

Logs recents ODIN :
SELECT ts, level, source, message FROM logs WHERE level IN ('WARNING','ERROR') ORDER BY ts DESC LIMIT 20;

Recherche semantique RAG :
1. Generer embedding : curl -s http://localhost:11434/api/embeddings -d '{"model":"nomic-embed-text","prompt":"question"}' | python3 -c "import sys,json; print(json.load(sys.stdin)['embedding'])"
2. Requete : SELECT title, theme, text FROM wiki_fr ORDER BY embedding <=> '[VECTEUR]'::vector LIMIT 10;

## DONNEES EN COURS D INGESTION
- Wikipedia FR multistream (2.5M articles) → wiki_fr
- Wikidata truthy RDF (~39 Go) → table a creer
- DBpedia abstracts FR → table a creer
- CodeSearchNet + The Stack → table a creer

## MODELE EMBEDDING
nomic-embed-text via Ollama local port 11434
Dimension : 768 vecteurs
Index : HNSW cosine

*PAN-RAG v1.0 — PAN∞ Research Lab — CC BY-SA 4.0*
*Auteur : Cedric MARET — ORCID 0009-0006-6399-9132*
