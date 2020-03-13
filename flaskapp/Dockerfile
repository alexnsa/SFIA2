FROM python:3.5.3
WORKDIR /app
COPY . .
EXPOSE 5000
RUN  pip3 install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/python", "app.py"]
