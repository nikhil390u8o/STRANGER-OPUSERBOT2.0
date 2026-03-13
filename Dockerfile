FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl ffmpeg aria2 git && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

COPY . /app/

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "SHUKLA"]
