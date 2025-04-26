FROM python:3.11.12-slim-bookworm

WORKDIR /usr/src/app
COPY app.py ./
RUN pip install --upgrade pip
RUN pip install flask
EXPOSE 5000

CMD ["python", "app.py"]
