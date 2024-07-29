FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requeriments.txt
RUN pip install katara/
RUN chmod +x wait-for entrypoints.sh

CMD ["./entrypoints.sh"]
