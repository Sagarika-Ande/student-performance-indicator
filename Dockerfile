FROM python:3.12-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements_docker.txt .

# Install only necessary packages and clean up
RUN pip install --no-cache-dir -r requirements_docker.txt && \
    rm -rf /root/.cache/pip

# Copy ONLY prediction-related files
COPY app.py .

# Copy trained model and preprocessor
COPY artifacts/model.pkl ./artifacts/
COPY artifacts/preprocessor.pkl ./artifacts/

# Copy only required src files
COPY src/__init__.py ./src/
COPY src/exception.py ./src/
COPY src/logger.py ./src/
COPY src/utils.py ./src/
COPY src/pipeline/__init__.py ./src/pipeline/
COPY src/pipeline/predict_pipeline.py ./src/pipeline/

# Copy templates for Flask
COPY templates/ ./templates/

# Expose Flask port
EXPOSE 5000

# Set environment variable for production
ENV FLASK_ENV=production

# Run with Gunicorn (production-ready)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120", "app:app"]