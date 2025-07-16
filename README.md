
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
4. Create a RESTful API (`api/data_api.py`) with **POST** and **GET** endpoints
5. Write a Dockerfile to containerize the frontend and backend
6. decompose docker files 
7. Run the app locally or with Docker

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
git clone git clone https://github.com/youssefelzahar/first_task.git


# Navigate to API folder
cd first_task/api

# Install dependencies
pip3 install -r requirements.txt

# Run the API
python3 api.py
python3 data_api.py
```

---

### 🐳 Run with Docker

#### 🔨 Build from Source

```bash
# Clone the project
git clone https://github.com/youssefelzahar/first_task.git
cd first_task/api

# Build the Docker image
docker-compose up --build
# Run the container
docker-compose up
```



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

```
✅ Get All Data
GET /data
Returns all Iris dataset records.

http://127.0.0.1:5000/data

✅ Add New Record
POST /data
Add a new record to the dataset.
Request Body:
{
  "sepal length (cm)": 6.4,
  "sepal width (cm)": 3.2,
  "petal length (cm)": 4.5,
  "petal width (cm)": 1.5,
  "target": 1
}




---

## 🧪 Testing

You can test the API using tools like:

* [Postman](https://www.postman.com/)

---

## 📦 Sample Queries

| Type        | Feature Array          | Prediction |
| ----------- | ---------------------- | ---------- |
| Setosa      | `[4.9, 2.9, 1.2, 0.3]` | `[0]`      |
| Versicolour | `[6.4, 3.2, 4.5, 1.5]` | `[1]`      |
| Virginica   | `[6.2, 3.1, 5.3, 2.4]` | `[2]`      |

---

## 👨‍💻 Author (Forked & Updated by youssefelzahar)

This is a forked and extended version of the original [AchilleasKn/flask\_api\_python](https://github.com/AchilleasKn/flask_api_python) repository.

Feel free to clone, customize, and deploy your own ML APIs.


