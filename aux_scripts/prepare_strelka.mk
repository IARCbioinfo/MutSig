

files=$(shell ls *.somatic.snvs_PASS.vcf.gz | xargs)

merge_files=$(patsubst %.somatic.snvs_PASS.vcf.gz,%.merge.vcf,$(wildcard *somatic.snvs_PASS.vcf.gz))
#order should be #CHROM	POS	FILTER	REF	ALT
%.merge.vcf:%.somatic.snvs_PASS.vcf.gz
	bcftools concat -a -r "chr1,chr2,chr3,chr4,chr5,chr6,chr7,chr8,chr9,chr10,chr11,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr20,chr21,chr22,chrX" $(subst snvs,indels,$<) $< |\
	egrep "^#CHR|^chr" | cut -f1,2,4,5,7 | awk '{print $$1"\t"$$2"\t"$$NF"\t"$$3"\t"$$4}'> $@

merge_all:$(merge_files)
all: merge_all


