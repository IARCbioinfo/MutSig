#!/bin/bash
#SBATCH --job-name=MSIG     # Job name
#SBATCH --mem-per-cpu=1000mb
#SBATCH --cpus-per-task=44

#replicate 1
~/miniconda3/bin/python run_cnv_signature.py -i lung_internal_public.purple.tsv -p purple_cnv_lung_r1 -t 44
~/miniconda3/bin/python run_cnv_signature.py -i lung_internal_public.facets.tsv -p facets_cnv_lung_r1 -t 44
#replicate 2
~/miniconda3/bin/python run_cnv_signature.py -i lung_internal_public.purple.tsv -p purple_cnv_lung_r2 -t 44
~/miniconda3/bin/python run_cnv_signature.py -i lung_internal_public.facets.tsv -p facets_cnv_lung_r2 -t 44
