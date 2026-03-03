# Builder stage
FROM python:3.12-slim as builder

WORKDIR /app

COPY main.py .

# Install any dependencies if needed
RUN pip install --no-cache-dir --user -r requirements.txt 2>/dev/null || echo "No requirements.txt"

# Release stage
FROM python:3.12-slim

WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder /app/main.py .
COPY --from=builder /root/.local /root/.local

# Set environment variables
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]