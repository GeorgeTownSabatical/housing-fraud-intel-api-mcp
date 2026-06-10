FROM python:3.11-slim

WORKDIR /workspace
COPY pyproject.toml README.md ./
COPY app ./app
COPY docs ./docs
COPY sample_data ./sample_data
COPY scripts ./scripts
RUN pip install --no-cache-dir -e .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
