FROM python:3.12-slim
WORKDIR /app
COPY scripts/ /app/scripts/
ENTRYPOINT ["python", "/app/scripts/health_check.py"]
