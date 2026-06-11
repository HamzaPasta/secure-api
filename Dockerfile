# Stage 1 - Build dependencies
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

#Stage 2 - Minimal final runtime footprint
FROM python:3.12-slim AS runtime

#Create non-root user for container security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

#Copy installed packages and binary from builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

COPY app/ ./app/

#Switch to non-root execution
USER appuser
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]