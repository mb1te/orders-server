FROM python:3
ENV PYTHONBUFFERED=1

WORKDIR /app
COPY . .

RUN pip install -U pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev