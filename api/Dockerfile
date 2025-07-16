FROM python:3.13-slim 

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev && apt-get clean

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

# Expose Streamlit & Flask ports
EXPOSE 8501
EXPOSE 5000

# Run Streamlit and Flask together
CMD ["python", "api.py"]
