FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install tensorboardX==2.0 
RUN pip install admet_ai==1.2.0
RUN pip install numpy==1.23.5
RUN pip install protobuf==3.20.3
RUN pip install torch==1.12.0

WORKDIR /repo
COPY . /repo
