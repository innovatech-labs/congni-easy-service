# https://fastapi.tiangolo.com/deployment/docker/

# Start from the official base image of Python 3.11
FROM python:3.11

# Set the current working directory of the container to /code
WORKDIR /code

# Copy the file with the requirements to the /code directory
COPY ./requirements.txt /code/requirements.txt

# Install the package dependencies in the requirements file
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the all files in current directory to the /code directory of the container
COPY . /code

# Set the command to run the uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]