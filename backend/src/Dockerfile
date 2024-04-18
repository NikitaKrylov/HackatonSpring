FROM python:3.11-alpine

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apk update && apk add curl

WORKDIR /src

COPY ./requirements ./requirements
RUN python -m pip install --upgrade pip \
    pip install -r requirements/dev.txt

RUN mkdir -p ./logs

COPY . .

CMD ["python", "-m", "app.main"]
