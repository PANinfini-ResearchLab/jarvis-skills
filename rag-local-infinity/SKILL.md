---
name: rag-local
description: Sovereign local RAG over PostgreSQL + pgvector with local embeddings
  (no cloud API). Use whenever the user wants to index documents or search their
  own corpus semantically.
---

# RAG Local — Sovereign Retrieval

## Configuration
| RAG_PG_DSN      | postgresql://localhost:5432/rag | PostgreSQL connection  |
| RAG_TABLE       | documents                       | Table name             |
| RAG_EMBED_URL   | http://localhost:11434          | Ollama endpoint        |
| RAG_EMBED_MODEL | nomic-embed-text                | Embedding model        |
| RAG_CHUNK_SIZE  | 800                             | Chars per chunk        |
| RAG_CHUNK_OVERLAP | 120                           | Overlap between chunks |
| RAG_TOP_K       | 5                               | Results to retrieve    |

## Schema
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE documents (
    id BIGSERIAL PRIMARY KEY,
    source TEXT,
    chunk_index INT,
    content TEXT,
    embedding vector(768),
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops);

WARNING : vector(768) = nomic-embed-text dimension.
Changing model → change dimension AND re-index everything.

## Ingest
1. Split source into chunks of RAG_CHUNK_SIZE with RAG_CHUNK_OVERLAP
2. POST $RAG_EMBED_URL/api/embeddings for each chunk
3. INSERT into $RAG_TABLE
Idempotence : DELETE rows for the source before re-ingestion.

## Query
1. Embed the question with the SAME model
2. SELECT source, content, 1 - (embedding <=> $1) AS score
   FROM documents ORDER BY embedding <=> $1 LIMIT $RAG_TOP_K;
3. Use chunks as LLM context — always cite the source.

## Rules
- No corpus-based answer without real retrieval — cite or say corpus has nothing (cf. honesty).
- Mixing two embedding models in one table silently breaks search.
- Always verify pgvector extension is installed : SELECT * FROM pg_extension WHERE extname='vector';
