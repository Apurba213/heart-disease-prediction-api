# Heart Disease Prediction API

A Machine Learning API that predicts the likelihood of heart disease using patient health information. Built with Python, Scikit-learn, FastAPI, and Docker, and deployed on Render.

## Live Demo

- **API:** https://heart-disease-prediction-api-fcq0.onrender.com/
- **Swagger Documentation:** https://heart-disease-prediction-api-fcq0.onrender.com/docs
- **Health Check:** https://heart-disease-prediction-api-fcq0.onrender.com/health

## Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- FastAPI
- Pydantic
- Joblib
- Docker
- Docker Compose
- Git and GitHub
- Render

## Project Structure

```text
heart-disease-prediction-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── model/
│   └── heart_model.joblib
│
├── data/
├── train_model.py
├── inspect_data.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## Machine Learning Model

- Algorithm: Logistic Regression
- Preprocessing: StandardScaler
- Implementation: Scikit-learn Pipeline
- Task: Binary Classification
- Output: Heart disease prediction (0 or 1)

The trained model is saved using Joblib and loaded by the FastAPI application.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API homepage |
| GET | `/health` | Health check |
| GET | `/info` | Model information |
| POST | `/predict` | Make a prediction |

## Example Prediction Request

**POST /predict**

```json
{
  "age": 55,
  "sex": 1,
  "cp": 0,
  "trestbps": 140,
  "chol": 250,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.5,
  "slope": 1,
  "ca": 0,
  "thal": 2
}
```

Example response:

```json
{
  "heart_disease": false
}
```

## Run Locally

Clone the repository:

```bash
git clone https://github.com/Apurba213/heart-disease-prediction-api.git
cd heart-disease-prediction-api
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Run with Docker

Build and start:

```bash
docker compose up --build
```

Open:

```text
http://127.0.0.1:8000/docs
```

Stop the containers:

```bash
docker compose down
```

## Deployment

The application is containerized using Docker and deployed as a Render Web Service.

## Disclaimer

This project is developed for educational and machine-learning practice purposes only. Its predictions are not medical diagnoses and should not be used as a substitute for professional medical advice.

## Author

**Apurba Barua**

- GitHub: https://github.com/Apurba213
- LinkedIn: https://www.linkedin.com/in/apurba-barua-a1b79a188/