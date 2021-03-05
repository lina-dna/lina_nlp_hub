
FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-runtime

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils vim
RUN buildDeps='gcc libc6-dev make build-essential curl gnupg' \
    && apt-get update && apt-get install -y $buildDeps git wget tar \
    && pip install --upgrade pip 
    
RUN curl -sL https://deb.nodesource.com/setup_12.x  | bash -
RUN apt-get -y install nodejs
RUN npm install

RUN pip install tornado pytorch-lightning pandas scikit-learn streamlit boto3 gensim python-mecab-ko g2pk
RUN pip install jupyterlab
RUN pip install pororo jupyter-tensorboard papermill elyra elyra-pipeline-editor-extension elyra-code-snippet-extension elyra-python-editor-extension
RUN jupyter lab build
RUN jupyter labextension install jupyterlab-system-monitor

#load pre-trained model in pororo
COPY download_all_pororo_models.py ./download_all_pororo_models.py
RUN python download_all_pororo_models.py

EXPOSE 8888 8080 6006

CMD ["sh","-c", "jupyter lab --ip=0.0.0.0 --allow-root --port=8888 --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*'"]
