## Student Performance Indicator

This project predicts students' math scores based on features such as gender, race/ethnicity, writing and reading scores, parental education level, lunch type, and test preparation course completion.

🔗 Live App: [Student Performance Indicator](https://student-performance-indicator-3j4u.onrender.com/predictdata)

💻 GitHub Repo: [Sahilnegi4444/student-performance-indicator](https://github.com/Sahilnegi4444/student-performance-indicator)

```
STUDENT PERFORMANCE
│
├── artifacts/                        # Datasets and saved model artifacts
│   ├── data.csv                      # Raw dataset
│   ├── train.csv / test.csv          # Train-test split
│   ├── model.pkl                     # Trained model
│   └── preprocessor.pkl              # Preprocessing pipeline
│
├── notebook/                         # Jupyter notebooks for EDA & model experiments
│   ├── EDA_STUDENT_PERFORMANCE.ipynb # Raw dataset
│   ├── MODEL_TRAINING.ipynb          # Train-test split
│
├── src/                              # Source code for MLOps workflow
│   ├── components/                   # Data ingestion, transformation, tuning, model training
│   ├── pipeline/                     # Training and prediction pipelines
│   ├── exception.py                  # Custom exception handling
│   ├── logger.py                     # Centralized logging
│   └── utils.py                      # Utility functions
│
├── templates/                        # Flask web templates
│   ├── index.html                    # Home page
│   └── home.html                     # Prediction interface
│
├── app.py                            # Flask app entry point
├── Dockerfile                        # Docker setup for containerized deployment
├── .dockerignore                     # Ignored files for Docker builds
├── requirements.txt                  # Full dependency list for dev/training
├── requirements_docker.txt           # Minimal dependencies for production (with Gunicorn)
└── README.md                         # Project documentation

```

## Key Features

End-to-End MLOps Pipeline
Includes data ingestion, transformation, model training, hyperparameter tuning, and deployment — all modular and scalable.

Best Model Selection: Linear Regression
After experimenting with multiple algorithms, Linear Regression provided the most interpretable and stable results for predicting student math performance.

Production-Ready Deployment
Containerized using Docker and deployed on Render (free service) with Gunicorn for handling concurrent requests efficiently.

Clean Engineering Practices
Built with structured logging, custom exception handling, and reusable components for easy debugging and extension.

## Key Learnings

Designed a complete ML pipeline that can be scaled or automated for larger datasets.

Learned how Docker simplifies containerization and deployment workflows.

Deployed ML models using Render, making cloud hosting seamless and cost-effective.

Gained hands-on experience in structuring ML projects for maintainability and clarity.

Understood why Linear Regression performs best for this problem — due to its interpretability and efficiency in predicting continuous numerical outcomes with low variance and minimal overfitting.

## Tech Stack

Languages & Libraries: Python, Flask, scikit-learn, pandas, numpy

Tools & Frameworks: Docker, Render, Logging, Exception Handling

Model: Linear Regression

Version Control: Git, GitHub
## How to Run Locally
# Clone the repository
git clone https://github.com/Sahilnegi4444/student-performance-indicator.git
cd student-performance-indicator

# Create and activate a virtual environment
python -m venv venv      # I have used python3.12 for this code
venv\Scripts\activate    # For Windows
# or
source venv/bin/activate # For Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py


For Dockerized deployment:

docker build -t student-performance .
docker run -p 8080:5000 student-performance

## Deployment

Deployed on Render using a Docker image with a lightweight setup (using requirements_docker.txt) and Gunicorn for scalability and multiple requests.

🔗 [View Live App](https://student-performance-indicator-3j4u.onrender.com/predictdata)

## Future Improvements

Add CI/CD pipeline for automated testing and deployment

Integrate MLflow or DVC for model versioning

Implement API-based model monitoring and retraining triggers
