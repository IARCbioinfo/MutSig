from SigProfilerMatrixGenerator.scripts import CNVMatrixGenerator as scna
from SigProfilerExtractor import sigpro as sig
import sys, getopt
import pandas as pd
#create the matrix needed for cnv data
def create_matrix(caller_cna,prefix):
 file_type = "ASCAT"
 input_file = caller_cna
 output_path=prefix
 project=prefix
 scna.generateCNVMatrix(file_type, input_file, project+"_matrix", "")

#run the signature analysis
def run(result,mfile,ncpu):
	filein="./"+mfile+"/ASCAT.CNV.matrix.tsv"
	sig.sigProfilerExtractor("matrix", result, filein,reference_genome="GRCh38",opportunity_genome="GRCh38", minimum_signatures=1, maximum_signatures=20, nmf_replicates=100,cpu=ncpu)



if __name__ == '__main__':

 cnv_file=''
 prefix=''
 project=''
 cpu=44

 try:
  opts, args = getopt.getopt(sys.argv[1:],"hi:p:t:",["cnvfile=","prefix=","cpu="])
 except getopt.GetoptError:
  print ("run_cnv_signature.py -i <cnv_segments> -p <prefix> -t <ncpu>")
  sys.exit(2)

 for opt, arg in opts:
  if opt in ("-h"):
   print ("run_cnv_signature.py -i<cnv_segments> -p <prefix> -t <ncpu>")
   sys.exit()
  elif opt in ("-i","--cnvfile"):
   cnv_file=arg
  elif opt in ("-p","--prefix"):
   prefix=arg
  elif opt in ("-t","--cpu"):
   cpu=int(arg)
 
 
 #we prepare the matrix
 create_matrix(cnv_file, prefix)
 #we run the CNV analysis
 result=prefix+"_cnvsig"
 mfile=prefix+"_matrix"
 run(result,mfile,cpu)

