# Gunakan image python sebagai base
FROM python:3-slim

# Set working directory
WORKDIR /code

# Salin file requirements.txt
COPY requirements.txt /code/

# Install dependencies
RUN pip install -r requirements.txt

# Salin kode aplikasi
COPY . /code/

# Set environment variable
ENV DJANGO_SETTINGS_MODULE=todoproject.settings

# Jalankan server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
