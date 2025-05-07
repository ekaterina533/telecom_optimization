FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /section_1

COPY section_1/requirements.txt .
COPY section_1/HTTP_requests.py .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "HTTP_requests.py"]