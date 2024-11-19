# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /B22

# Copy the application code
COPY . /B22
RUN pip install --no-cache-dir --upgrade pip
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (optional, for local testing)
EXPOSE 8000

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
