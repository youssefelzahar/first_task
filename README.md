
# 🌸 Model Deployment as API | The Iris Dataset

Deploying a Machine Learning Model as a REST API using Flask and Docker.

![Iris](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png "Iris")

---

## 📊 Dataset Overview

This is one of the most well-known datasets in pattern recognition. It includes **3 classes** of 50 instances each (Setosa, Versicolour, Virginica), based on:

1. Sepal length (cm)
2. Sepal width (cm)
3. Petal length (cm)
4. Petal width (cm)
5. Class label

---

## 🔧 Project Structure & Steps

1. Build and train the machine learning model in Jupyter Notebook (`model/Iris_model.ipynb`)
2. Save the model to `api/iris_model.pkl`
3. Create a RESTful API (`api/api.py`) with **POST** and **GET** endpoints
4. Write a Dockerfile to containerize the app
5. Run the app locally or with Docker

---

## 💻 Requirements

* Python 3.6+
* Docker
* Dependencies from `requirements.txt`

---

## 🚀 How to Run

### ▶️ Run Locally (No Docker)

```bash
# Clone the project
git clone https://github.com/AchilleasKn/flask_api_python.git

# Navigate to API folder
cd flask_api_python/api

# Install dependencies
pip3 install -r requirements.txt

# Run the API
python3 api.py
```

---

### 🐳 Run with Docker

#### 🔨 Build from Source

```bash
# Clone the project
git clone https://github.com/AchilleasKn/flask_api_python.git
cd flask_api_python/api

# Build the Docker image
docker build -t iris_api .

# Run the container
docker run -d -p 5000:5000 iris_api
```

#### 🪝 Pull Prebuilt Image (Original Image by Author)

```bash
# Pull and run image
docker pull achilleaskn/flask_api_python:latest
docker run -d -p 5000:5000 achilleaskn/flask_api_python:latest
```

---

## 📬 API Endpoints

### 🔍 `POST /predict`

Make predictions by sending a feature array.

**Request:**

```json
{
  "feature_array": [6.4, 3.2, 4.5, 1.5]
}
```

**Response:**

```json
{
  "prediction": [1]
}
```

### 📄 `GET /`

Simple welcome message or health check.

**Request:**

```bash
curl http://localhost:5000/
```

**Response:**

```json
{
  "message": "Welcome to the Iris Prediction API"
}
```

---

## 🧪 Testing

You can test the API using tools like:

* [Postman](https://www.postman.com/)
* `curl`
* Python `requests` module

---

## 📦 Sample Queries

| Type        | Feature Array          | Prediction |
| ----------- | ---------------------- | ---------- |
| Setosa      | `[4.9, 2.9, 1.2, 0.3]` | `[0]`      |
| Versicolour | `[6.4, 3.2, 4.5, 1.5]` | `[1]`      |
| Virginica   | `[6.2, 3.1, 5.3, 2.4]` | `[2]`      |

---

## 👨‍💻 Author (Forked & Updated by You)

This is a forked and extended version of the original [AchilleasKn/flask\_api\_python](https://github.com/AchilleasKn/flask_api_python) repository.

Feel free to clone, customize, and deploy your own ML APIs.


