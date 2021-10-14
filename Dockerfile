################## BASE IMAGE ######################
FROM python:3.7.3

################## METADATA ######################

LABEL base_image="python"
LABEL version="1.0"
LABEL software="MutSig-nf"
LABEL software.version="1.0"
LABEL about.summary="Container image containing all requirements for **mutational signatures analysis**"
LABEL about.home="https://github.com/IARCbioinfo/MutSig"
LABEL about.documentation="http://github.com/IARCbioinfo/MutSig/README.md"
LABEL about.license_file="http://github.com/IARCbioinfo/MutSig/LICENSE.txt"
LABEL about.license="MIT"

################## MAINTAINER ######################
MAINTAINER **digenovaa** <**digenovaa@fellows.iarc.fr**>

################## INSTALLATION ######################
RUN pip install --upgrade pip
RUN pip install SigProfilerExtractor SigProfilerMatrixGenerator SigProfilerPlotting
ADD ./aux_scripts/add_ref_signatures.py /opt
RUN python /opt/add_ref_signatures.py
