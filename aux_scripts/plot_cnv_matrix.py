import sigProfilerPlotting as sigPlt
import sys, getopt
import pandas as pd


if __name__ == '__main__':

 matrix_file=''
 output_path=''
 project=''
 #bolean variables
 percentage=False
 aggregate=False

 try:
  opts, args = getopt.getopt(sys.argv[1:],"hm:n:o:p:a:",["matrix=","project=","output_path=","percentaje=","agregate="])
 except getopt.GetoptError:
  print ("run_cnv_matrix.py -m <cnv_matrix> -n <name_project> -o <output_path>")
  sys.exit(2)

 for opt, arg in opts:
  if opt in ("-h"):
    print ("run_cnv_matrix.py -m <cnv_matrix> -n <name_project> -o <output_path>")
    sys.exit()
  elif opt in ("-m","--matrix"):
    matrix_file=arg
  elif opt in ("-n","--project"):
    project=arg
  elif opt in ("-o","--output_path"):
    output_path=arg
  elif opt in ("-p","--percentaje"):
    percentage=True
  elif opt in ("-a","--agregate"):
    aggregate=True

print(matrix_file)
print(output_path)
print(project)
#we call the function for ploting the copy number
sigPlt.plotCNV(matrix_file, output_path, project, "pdf", percentage=percentage, aggregate=aggregate) #plotting of CNV counts
