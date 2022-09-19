FROM python:3.8.13-alpine3.15
WORKDIR /app
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip3 install --upgrade pip

COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./ ./
EXPOSE 8000
CMD ["python", "./manage.py", "migrate"]