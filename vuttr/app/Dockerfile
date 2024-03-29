# Use the official Python base image
FROM python:3.10.14-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the working directory
COPY . .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Expose the port on which the application will run
EXPOSE 8000

# Creata table in database
CMD ["python","app.py"]

# Run the FastAPI application using uvicorn server
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]