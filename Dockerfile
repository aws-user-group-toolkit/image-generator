# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY ./src/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY ./src/ .

# Set the environment variables
ENV TITLE="Default Title" \
    DATE="Default Date" \
    LOCATION="Default Location" \
    FOTO="https://example.com/default.jpg"

# Run the command to start the application
CMD [ "python", "generate.py" ]