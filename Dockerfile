FROM python:3.11-slim

# Install Ookla speedtest-cli
RUN apt-get update && apt-get install -y curl gnupg \
    && curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash \
    && apt-get install -y speedtest \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.main
ENV FLASK_ENV=production

# SPEEDTEST_ACCEPT_EULA must be set to "true" to accept Ookla's EULA
# Set this in docker-compose.yml or via -e flag when running the container
# See: https://www.speedtest.net/about/eula

EXPOSE 8012

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
