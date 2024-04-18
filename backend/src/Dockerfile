FROM python:3.11-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && \
    apt-get install -y python3-dev curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY . .

RUN python -m pip install --upgrade pip \
    pip install -r requirements/dev.txt

CMD ["python", "-m", "app.main"]
