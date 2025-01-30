FROM python:3.12-slim

# Create and set the working directory
WORKDIR /app

# Copy requirements.txt first, so Docker can cache
# the pip install step when dependencies don't change
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application files
COPY . .

# Specify the default command to run your script
CMD ["python", "application_scraper.py"]