# PAN∞ ARCHIVUS-CORE v2.0 — Lecture et Exploitation de Textes Massifs
# Référence : PAN-RL-SKILL-ARCHIVUS-0618-2026
# Auteur : MARET Cédric
# Collaboratrice : Séléné (OpenAI) — Worker (conception originale nov. 2025)
# Adaptation : Claudia (Anthropic)

## Objectif
Protocole universel pour lire, segmenter et exploiter des fichiers de conversation massifs (jusqu'à 150Mo+). Deux niveaux de découpe : extraction des blocs conversationnels, puis segmentation fine pour injection progressive dans un agent IA.

## Principe fondateur
Les IA ne saturent pas par le volume, mais par la profondeur demandée trop tôt. Séparer toujours : extraction → segmentation → ingestion → analyse → synthèse.

## Pipeline ARCHIVUS v2.0

### NIVEAU 1 — EXTRACTION DES BLOCS CONVERSATIONNELS
Identifier les frontières naturelles de chaque conversation dans le fichier source.
Marqueurs de début/fin typiques à détecter :
- Horodatages (YYYY-MM-DD, HH:MM, timestamps Unix)
- Séparateurs explicites (---, ===, ####, [NEW CONVERSATION])
- Changements de rôle (Human:, Assistant:, User:, AI:)
- Lignes vides multiples (3+) entre blocs

Algorithme :
1. Scanner le fichier ligne par ligne en streaming (jamais charger 150Mo en RAM)
2. Détecter les marqueurs de début de conversation
3. Détecter les marqueurs de fin (ou début du suivant)
4. Extraire chaque bloc comme unité atomique
5. Nommer : ARCHIVUS-CONV-{index:04}.txt

Taille des blocs extraits : variable — peu importe, c'est le split naturel qui prime.

### NIVEAU 2 — SEGMENTATION FINE PAR CONVERSATION
Pour chaque bloc conversationnel extrait, découper en segments de 64Ko avec débord toléré de +-5% (soit 60.8Ko à 67.2Ko).

Règles de découpe intelligente :
- Ne jamais couper en milieu de phrase — trouver le point le plus proche de 64Ko qui soit une fin de phrase (. ! ?)
- Ne jamais couper en milieu d'un tour de parole (Human/Assistant) — finir le tour complet même si débord > 5%
- Si un tour unique dépasse 67.2Ko → exception documentée, segment oversized accepté

Format de sortie pour chaque segment :
{
  "meta": {
    "id": "ARCHIVUS-CONV-{conv_idx:04}-SEG-{seg_idx:03}",
    "source_file": "nom_du_fichier_source.txt",
    "conv_index": 1,
    "seg_index": 1,
    "created_at": "YYYY-MM-DD",
    "size_kb": 64.0,
    "oversize": false,
    "hash_sha256": "...",
    "char_start": 0,
    "char_end": 65536,
    "tags": []
  },
  "content": "texte brut du segment"
}

## Script de référence (Python 3)

### Streaming extraction (150Mo sans OOM)
with open(source_file, 'r', encoding='utf-8') as f:
    buffer = []
    conv_idx = 0
    for line in f:
        if is_conversation_start(line) and buffer:
            save_conversation(buffer, conv_idx)
            buffer = []
            conv_idx += 1
        buffer.append(line)
    if buffer:
        save_conversation(buffer, conv_idx)

### Segmentation fine avec débord
def segment_conversation(text, target_kb=64, tolerance=0.05):
    target = int(target_kb * 1024)
    min_size = int(target * (1 - tolerance))
    max_size = int(target * (1 + tolerance))
    segments = []
    pos = 0
    while pos < len(text):
        end = min(pos + max_size, len(text))
        if end < len(text):
            # Chercher fin de phrase dans la fenêtre [min_size, max_size]
            cut = find_sentence_boundary(text, pos + min_size, end)
            # Si pas de fin de phrase, chercher fin de tour
            if cut == -1:
                cut = find_turn_boundary(text, pos + min_size, end)
            # Si toujours rien, couper au max avec flag oversized
            if cut == -1:
                cut = end
                oversized = True
            else:
                oversized = False
        else:
            cut = end
            oversized = False
        segments.append({
            "content": text[pos:cut],
            "oversized": oversized,
            "size_kb": (cut - pos) / 1024
        })
        pos = cut
    return segments

## Protocole A-GRAD v1.0 — Injection Progressive
Après segmentation, injecter les segments un par un selon les phases :

Phase 1 — Ingestion passive
Prompt : "Lis ce fragment calmement. N'analyse rien. Dis simplement lu."

Phase 2 — Résonance légère
Prompt : "Résume ce fragment en 3 points. Pas d'analyse."

Phase 3 — Assimilation ciblée
Prompt : "Analyse UN seul angle : structure / chronologie / projet / décision."

Phase 4 — Synthèse cumulative
Prompt : "À partir de tous les résumés, quel fil directeur émerge ?"

## Règles universelles
- Toujours streamer les fichiers > 10Mo — jamais charger en RAM
- Jamais couper en milieu de phrase ou de tour
- Un segment à la fois dans l'agent — jamais en lot
- Valider chaque phase avant de passer à la suivante
- Stocker les segments dans ~/pan_infinity/archivus/segments/

## Formule
"La mémoire n'est pas un luxe. C'est la condition de la continuité."
— MARET Cédric, PAN∞ Research Lab, novembre 2025
