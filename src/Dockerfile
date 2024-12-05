FROM python:3.11-alpine
WORKDIR /usr/src
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && \
    apt-get install -y gcc libpq-dev musl-dev
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 80
RUN chmod +x start.sh
ENTRYPOINT ["bash", "start.sh"]
