# SKILL : PAN-KNOWLEDGE-BASES
**Bases de données ouvertes — Corpus RAG PAN∞**
**Réf. :** PAN-RL-434D-INF-0626-0003 · v1.0 · CC BY-SA 4.0

## DESCRIPTION
Inventaire des sources de données ouvertes disponibles pour le RAG souverain PAN∞.
Organisé par catégorie. Toutes les URLs sont vérifiées au 09/06/2026.

## STATUT TÉLÉCHARGEMENTS ODIN
- frwiki-latest-pages-articles-multistream.xml.bz2 → /mnt/JARVIS-MODEL/wikidata/ ✅
- latest-truthy.nt.bz2 (Wikidata) → /mnt/JARVIS-MODEL/wikidata/ ⏳ en cours
- short-abstracts_lang=fr.ttl.bz2 (DBpedia) → /mnt/JARVIS-MODEL/wikidata/ ✅

## 1. ENCYCLOPÉDIQUE / FACTUEL

### Wikimedia / Wikipedia FR
- Dump articles : https://dumps.wikimedia.org/frwiki/latest/frwiki-latest-pages-articles-multistream.xml.bz2
- Wiktionnaire : https://dumps.wikimedia.org/frwiktionary/latest/frwiktionary-latest-pages-articles.xml.bz2
- Wikiquote : https://dumps.wikimedia.org/frwikiquote/latest/frwikiquote-latest-pages-articles.xml.bz2
- Wikiversité : https://dumps.wikimedia.org/frwikiversity/latest/frwikiversity-latest-pages-articles.xml.bz2

### Wikidata
- JSON complet : https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.bz2
- RDF truthy : https://dumps.wikimedia.org/wikidatawiki/entities/latest-truthy.nt.bz2

### DBpedia
- Abstracts FR : https://databus.dbpedia.org/dbpedia/text/short-abstracts/2022.12.01/short-abstracts_lang=fr.ttl.bz2
- Latest-core : https://databus.dbpedia.org/dbpedia/collections/latest-core

### Kiwix / ZIM
- Wikipedia FR avec images : https://download.kiwix.org/zim/wikipedia/wikipedia_fr_all_maxi_2026-05.zim
- Wikipedia FR sans images : https://download.kiwix.org/zim/wikipedia/wikipedia_fr_all_nopic_2026-05.zim

### YAGO 4.5
- https://yago-knowledge.org/downloads/yago-4-5

### ConceptNet
- https://github.com/commonsense/conceptnet5/wiki/Downloads

## 2. CODE SOURCE

### Corpus massifs IA
- The Stack v2 : https://huggingface.co/datasets/bigcode/the-stack-v2
- The Stack v1 : https://huggingface.co/datasets/bigcode/the-stack
- StarCoderData : https://huggingface.co/datasets/bigcode/starcoderdata
- GitHub Code (CodeParrot) : https://huggingface.co/datasets/codeparrot/github-code
- Software Heritage : https://archive.softwareheritage.org/

### Benchmarks code IA
- CodeSearchNet : https://github.com/github/CodeSearchNet
  - Python : https://s3.amazonaws.com/code-search-net/CodeSearchNet/v2/python.zip
  - Java : https://s3.amazonaws.com/code-search-net/CodeSearchNet/v2/java.zip
  - Go : https://s3.amazonaws.com/code-search-net/CodeSearchNet/v2/go.zip
  - PHP : https://s3.amazonaws.com/code-search-net/CodeSearchNet/v2/php.zip
  - JavaScript : https://s3.amazonaws.com/code-search-net/CodeSearchNet/v2/javascript.zip
  - Ruby : https://s3.amazonaws.com/code-search-net/CodeSearchNet/v2/ruby.zip
- CodeXGLUE (Microsoft) : https://github.com/microsoft/CodeXGLUE
- Project CodeNet (IBM) : https://github.com/IBM/Project_CodeNet
- APPS : https://people.eecs.berkeley.edu/~hendrycks/APPS.tar.gz
- HumanEval : https://github.com/openai/human-eval

### Archives GitHub
- GH Archive : https://www.gharchive.org/
- Libraries.io : https://zenodo.org/records/3626071

### Registres paquets
- npm : https://replicate.npmjs.com/
- PyPI : https://pypi.org/simple/
- Maven Central : https://repo.maven.apache.org/maven2/
- crates.io : https://crates.io/data-access
- Go Modules : https://index.golang.org/
- Packagist (PHP) : https://packagist.org/packages/list.json
- RubyGems : https://rubygems.org/
- NuGet (.NET) : https://api.nuget.org/v3/index.json

## 3. OS / PROJETS MAJEURS
- Linux Kernel : https://github.com/torvalds/linux
- LLVM/Clang : https://github.com/llvm/llvm-project
- FreeBSD : https://github.com/freebsd/freebsd-src
- Debian sources : https://deb.debian.org/debian/dists/stable/main/source/Sources.xz
- Ubuntu sources : https://archive.ubuntu.com/ubuntu/dists/noble/main/source/Sources.xz
- AOSP : https://android.googlesource.com/
- Chromium : https://chromium.googlesource.com/chromium/src.git
- F-Droid : https://f-droid.org/en/packages/

## PRIORITÉ D'INGESTION PAN∞
1. Wikipedia FR multistream ← en cours
2. Wikidata truthy ← en cours
3. DBpedia abstracts FR ← téléchargé
4. CodeSearchNet Python/JS ← à faire
5. The Stack v1 ← à faire
6. Libraries.io ← à faire

*PAN-KNOWLEDGE-BASES v1.0 — PAN∞ Research Lab — CC BY-SA 4.0*
*Auteur : Cédric MARET — ORCID 0009-0006-6399-9132*
