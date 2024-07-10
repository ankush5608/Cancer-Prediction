# Cancer Prediction Web App
link: https://cancer-prediction-16mz.onrender.com/

This is a web application built using Streamlit to predict cancer. The app leverages machine learning models to provide predictions based on user input data.

## Features

- User-friendly interface to input patient data.
- Real-time cancer prediction based on the input data.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/mlopscancpred.git
    cd mlopscancpred
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

### Using Docker

Alternatively, you can run the app using Docker.

1. Pull the Docker image:

    ```sh
    docker pull ankush5608/mlopscancpred:latest
    ```

2. Run the Docker container:

    ```sh
    docker run -p 8501:8501 ankush5608/mlopscancpred:latest
    ```

### Access the App

Once the app is running, open your web browser and go to: http://localhost:8501



## Usage

1. Open the web app in your browser.
2. Enter the required patient data in the input fields.
3. Click on the 'Predict' button to get the cancer prediction results.
4. View the prediction results
