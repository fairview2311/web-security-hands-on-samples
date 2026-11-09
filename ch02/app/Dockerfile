FROM python:3.13-slim
RUN apt-get update && apt-get install -y --no-install-recommends iputils-ping && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN mkdir -p /opt/flags && echo "FLAG{os-command-injection}" > /opt/flags/ch13.txt
