# MutSig
Mutational signature analysis of WGS data. 
This repo constains simple scripts to perform mutational signatures analysis using [SigProfilerExtractor](https://github.com/AlexandrovLab/SigProfilerExtractor)

# Signature workflow (Point Mutations)

## 1. Prepare reference genome
the script "add_ref_signatures.py" stored in aux_script directory provide examples to donwload the reference genome (def:GRCh38)

## 2. Prepare WGS data
The makefile stored in aux_scripts directory provide examples for mutect and strelka callers.

## 3. Run Signature analysis
The python and bash scripts provide examples for both Point mutations callers.

# Signature workflow (Copy Number Alterations)
The python script ***run_cnv_signature.py*** and the bash script runsig_both.sh stored in the aux_script directory provide examples
for discovering CNV signatures from Purple or Facets callers. 
 
# Docker container
To avoid install the needed software a Docker container is available at [hub.docker:iarcbioinfo/mutsig](https://hub.docker.com/repository/docker/iarcbioinfo/mutsig) and include the GRCh38 reference.

