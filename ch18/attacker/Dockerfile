FROM python:3.13-slim
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir httpx==0.28.1 pyjwt==2.15.1 pytest==8.4.2 pip-audit==2.9.0
