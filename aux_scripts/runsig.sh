#!/bin/bash
#SBATCH --job-name=SSIG     # Job name
#SBATCH --mem-per-cpu=1000mb
#SBATCH --cpus-per-task=44

~/miniconda3/bin/python run_strelka_signatures.py 
