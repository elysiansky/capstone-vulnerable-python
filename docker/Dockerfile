FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint script
COPY /docker/entrypoint.sh /entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# Expose the port
EXPOSE 5000

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]