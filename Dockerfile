# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app

# Expose the Flask port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
