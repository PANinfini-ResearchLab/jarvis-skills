# SKILL : PAN-LOGS-RAG
**Interface RAG PostgreSQL/pgvector — Logs Hermès — PAN∞ Research Lab**
**Réf. :** PAN-RL-434D-INF-0626-0002 · v1.0 · CC BY-SA 4.0

## DESCRIPTION
Ce skill donne accès à la base de logs vectorielle de ODIN.
Base : PostgreSQL + pgvector sur localhost.
Contient : logs Hermès Agent (agent.log, gateway.log, errors.log) avec embeddings nomic-embed-text.

## CONNEXION
Host     : localhost
Port     : 5432
Base     : jarvis_logs
User     : jarvis
Password : paninfini2026
Connexion: postgresql://jarvis:paninfini2026@localhost/jarvis_logs

## SCHÉMA
Table : logs
id         SERIAL PRIMARY KEY
ts         TIMESTAMPTZ        — horodatage de l'événement
level      VARCHAR(10)        — INFO / WARNING / ERROR / DEBUG
source     VARCHAR(100)       — module source (ex: agent.tool_executor)
session_id VARCHAR(50)        — identifiant de session Hermès
message    TEXT               — message du log
raw        TEXT               — ligne brute originale
embedding  vector(768)        — embedding nomic-embed-text

Index disponibles :
idx_logs_ts        — recherche par date
idx_logs_source    — recherche par module
idx_logs_session   — recherche par session
idx_logs_embedding — recherche vectorielle HNSW cosine

## REQUÊTES SQL UTILES

### Derniers événements
SELECT ts, level, source, message FROM logs ORDER BY ts DESC LIMIT 50;

### Erreurs et warnings récents
SELECT ts, level, source, message FROM logs WHERE level IN ('WARNING','ERROR') ORDER BY ts DESC LIMIT 50;

### Par session
SELECT ts, level, source, message FROM logs WHERE session_id = '20260608_194820_a16030' ORDER BY ts;

### Tool calls exécutés
SELECT ts, source, message FROM logs WHERE message LIKE '%tool%completed%' ORDER BY ts DESC LIMIT 50;

### Tool calls en erreur
SELECT ts, source, message FROM logs WHERE message LIKE '%tool%error%' OR message LIKE '%returned error%' ORDER BY ts DESC LIMIT 50;

### Latences API
SELECT ts, message FROM logs WHERE message LIKE '%latency%' ORDER BY ts DESC LIMIT 20;

### Activité par session
SELECT session_id, COUNT(*) as events, MIN(ts) as debut, MAX(ts) as fin FROM logs GROUP BY session_id ORDER BY debut DESC;

## RECHERCHE VECTORIELLE (RAG)
Nécessite un embedding de la requête via nomic-embed-text.
Exemple Python :
```python
import requests, psycopg2
def search(query, limit=10):
    r = requests.post("http://localhost:11434/api/embeddings", json={"model":"nomic-embed-text","prompt":query})
    vec = r.json()["embedding"]
    conn = psycopg2.connect("postgresql://jarvis:paninfini2026@localhost/jarvis_logs")
    cur = conn.cursor()
    cur.execute("SELECT ts, level, source, message FROM logs ORDER BY embedding <=> %s::vector LIMIT %s", (str(vec), limit))
    return cur.fetchall()
```

## INGESTION DES LOGS
Script : /mnt/JARVIS-SSD/jarvis-rag/ingest_logs.py
Venv   : /mnt/JARVIS-SSD/jarvis-rag/.venv
Lancer :
source /mnt/JARVIS-SSD/jarvis-rag/.venv/bin/activate
python3 /mnt/JARVIS-SSD/jarvis-rag/ingest_logs.py

Sources ingérées :
~/.hermes/logs/agent.log
~/.hermes/logs/gateway.log
~/.hermes/logs/errors.log

## COMMANDES PSQL RAPIDES
# Connexion directe
psql postgresql://jarvis:paninfini2026@localhost/jarvis_logs

# Compter les entrées
SELECT COUNT(*) FROM logs;

# Vérifier les dernières ingestions
SELECT MAX(ts), COUNT(*) FROM logs;

## NOTES
- Modèle embedding : nomic-embed-text (274 MB, installé sur Ollama)
- Dimension vecteur : 768
- Index vectoriel : HNSW cosine (optimal pour recherche sémantique)
- Relancer ingest_logs.py après chaque session pour maintenir la base à jour

*PAN-LOGS-RAG v1.0 — PAN∞ Research Lab — CC BY-SA 4.0*
*Auteur : Cédric MARET — ORCID 0009-0006-6399-9132*
