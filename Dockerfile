# 1. Start with a lightweight Python image
FROM python:3.9-slim

# 2. Set the working folder inside the container
WORKDIR /app

# 3. Copy the dependencies file
COPY requirements.txt .

# 4. Install Flask inside the container
RUN pip install -r requirements.txt

# 5. Copy the rest of our code
COPY . .

# 6. Run the app
CMD ["python", "app.py"]