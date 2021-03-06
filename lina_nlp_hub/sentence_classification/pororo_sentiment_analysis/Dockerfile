FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-runtime

USER root

COPY requirements.txt req.txt
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN buildDeps='gcc libc6-dev make' \
	&& apt-get update && apt-get install -y $buildDeps git git-lfs wget tar build-essential gnupg \
	&& pip install --upgrade pip \
	&& pip install -r req.txt \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /workspace/
COPY inferencer.py /workspace/inferencer.py

#load pre-trained model in pororo
RUN python -c "from pororo import Pororo; sa = Pororo(task='sentiment', model='brainbert.base.ko.shopping', lang='ko');"

EXPOSE 8000 8001
CMD ["uvicorn", "inferencer:app", "--reload", "--host=0.0.0.0", "--port=8000"]
