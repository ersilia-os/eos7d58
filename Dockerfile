FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install tensorboardX==2.0 admet_ai==1.2.0
RUN conda install -c conda-forge xorg-libxrender xorg-libxtst

WORKDIR /repo
COPY . /repo
