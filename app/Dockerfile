FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file and Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the default command to run the application
CMD ["streamlit", "run", "main.py"]