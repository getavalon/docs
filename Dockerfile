FROM mottosso/maya:2016sp1

MAINTAINER Marcus Ottosson <konstruktion@gmail.com>

COPY requirements.txt .

RUN wget https://bootstrap.pypa.io/get-pip.py && \
	mayapy get-pip.py && \
	mayapy -m pip install -r requirements.txt

# Avoid creation of auxilliary files
ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONPATH=$PYTHONPATH:/pythonpath
WORKDIR /workspace

EXPOSE 8000

ENTRYPOINT mayapy -u _serve.py
