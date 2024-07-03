FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt /app/

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["/app/Main.py"]

