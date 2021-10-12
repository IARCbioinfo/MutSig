from SigProfilerExtractor import sigpro as sig
import sys
import pandas as pd

def run():
	sig.sigProfilerExtractor("vcf", "results_sigs_strelka", "/home/digenovaa/scratch/lungNENomics/MutSig/Mutect2/mutect_vcfs",reference_genome="GRCh38", minimum_signatures=1, maximum_signatures=10, nmf_replicates=100,cpu=44)


if __name__ == '__main__':
    run()

