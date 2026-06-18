# SKILL : PAN-PHYSX-RESEARCH
Recherche et optimisation PhysX 3.4 — PAN∞ Research Lab
Ref. : PAN-RL-434D-PanHermesSkill-0626-0003 · v1.0 · CC BY-SA 4.0

## DESCRIPTION
PhysX 3.4 (NVIDIA GameWorks) est clone en local pour etude et optimisation.
Code source complet, moteur physique temps reel open-source (multi-threading,
SIMD, allocateurs memoire custom, kernels CUDA).

## EMPLACEMENT
/mnt/JARVIS-SSD/jarvis-research/PhysX-3.4

## OBJECTIF
Etudier l architecture et les techniques d optimisation de PhysX :
- Multi-threading et parallelisation
- Vectorisation SIMD (SSE/AVX)
- Allocateurs memoire custom
- Kernels CUDA pour simulation GPU
- Patterns transposables aux projets PAN∞ (AOM, simulations physiques,
  moteurs de calcul scientifique)

## ACTIONS DISPONIBLES

### Inspection de la codebase
cd /mnt/JARVIS-SSD/jarvis-research/PhysX-3.4
pygount --format=summary --folders-to-skip=".git,bin,lib,build" .

### Recherche de patterns d optimisation
grep -rn "SIMD\|AVX\|SSE\|__m128\|__m256" --include=*.cpp --include=*.h .
grep -rn "__global__\|__device__\|cudaMalloc" --include=*.cu .

### Analyse de l architecture multi-threading
search_files pattern="Thread\|Mutex\|Atomic\|TaskManager" target=content

## PISTES D AMELIORATION A EXPLORER
- Portage des kernels CUDA pour architectures Volta/V100 (vs architectures
  d origine plus anciennes)
- Comparaison des allocateurs custom avec jemalloc/tcmalloc modernes
- Applicabilite a AOM (Algebre Ontologique de Maret) et aux simulations
  physiques PAN∞ (AION-LUMASS, Cubis-Hexis)

## STATUT
Code clone, en attente d analyse. Jarvis peut explorer librement, documenter
ses observations dans blackbox, et proposer des pistes d optimisation pour
les projets PAN∞ qui necessitent du calcul physique intensif.

*PAN-PHYSX-RESEARCH v1.0 — PAN∞ Research Lab — CC BY-SA 4.0*
*Ref. PAN-RL-434D-PanHermesSkill-0626-0003*
*Auteur : Cedric MARET — ORCID 0009-0006-6399-9132*
