# Use python image as base
FROM python:3.8

# Set working directory
WORKDIR /code
# Copy requirements.txt file
COPY requirements.txt /code/
# Install dependencies
RUN pip install -r requirements.txt
# Copy application code
COPY . /code/
# Set environment variable
ENV DJANGO_SETTINGS_MODULE=todoproject.settings
# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]