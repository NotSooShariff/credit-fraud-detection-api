# 💳 Credit Card Fraud Detection Flask API

This repository contains a Flask API for credit card fraud detection using a machine learning model. The project includes pre-trained models, data preprocessing, and an API for making predictions. Below, you'll find information on how to use this code for local development, the project structure, and an explanation of the machine learning model.

## ⚠️ Disclaimer

Please note that this project is a proof of concept and can be used for educational and experimental purposes only. It is based on the Kaggle dataset obtained from [MLG - ULB's Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). 

As this dataset contains actual banking data, the original features have been omitted and replaced with derived features obtained through Principal Component Analysis (PCA) for privacy and security reasons. While this project provides a credit card fraud detection model in the "model/source-model.ipynb" notebook, it is essential to understand that the model's performance and suitability may vary when applied to different datasets or real-world scenarios. Feel free to use the model as a starting point and make suitable modifications to adapt it to your specific data and requirements. Always exercise caution and follow best practices when working with sensitive financial or personal data. 

## 📁 Project Structure

The project is organized as follows:

- `testcode/`: A folder containing a test script, `sample.py`, for checking if the API works.
- `model/source-model.ipynb`: The Directory for the Jupyter Notebook containing the machine learning model development and training process.
- `app.py`: The Flask application file that runs the API.
- `model.h5`: A pre-trained machine learning model for fraud detection.
- `README.md`: This readme file.
- `requirements.txt`: A file listing the required Python packages.
- `vectorizer.pkl`: A pre-trained vectorizer or scaler for data preprocessing.


## 🚀 How to Use the Code

Follow these steps to set up and run the Credit Card Fraud Detection Flask API locally:

1. Clone this repository:

   ```bash
   git clone https://github.com/NotSooShariff/CC-Fraud-Detection.git
   ```

2. Navigate to the project directory:

   ```bash
   cd credit-card-fraud-detection
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server by running:

   ```bash
   python app.py
   ```

   This will start the server on `http://127.0.0.1:5000`.

5. To expose the API to the web, you can use [ngrok](https://ngrok.com/). After registering for Ngrok, go to the [Setup Page](https://dashboard.ngrok.com/get-started/setup) and download and unzip the executable.
6. Launch the executable. Once the terminal pops, Configure the auth token by using the `ngrok config add-authtoken` command. Your auth token will be displayed in the same dashboard.

7. You can now expose the port to the web with a secure tunnel, by using:

   ```bash
   ngrok http 5000
   ```

   Use the URL under "Forwarding" in Ngrok to make API calls.


## 🧠 Machine Learning Model Explanation

The machine learning model for credit card fraud detection was developed in the `source-model.ipynb` Jupyter Notebook. This model aims to detect fraudulent credit card transactions based on various features from the dataset. Here's an overview of the key steps and techniques used in developing this model:

1. **Data Loading and Preprocessing**:
   - The dataset for credit card fraud detection was loaded from a CSV file using Pandas.
   - The dataset contains features, including transaction amount, time, and other anonymized features.
   - Data preprocessing was performed to prepare the dataset for modeling.

2. **Exploratory Data Analysis (EDA)**:
   - Exploratory data analysis was conducted to gain insights into the dataset.
   - Visualizations, such as histograms, were used to understand the distribution of features, including the distribution of fraud and non-fraud transactions.

3. **Feature Scaling and Transformation**:
   - Feature scaling was applied to the "Amount" column using the RobustScaler to handle outliers effectively.
   - The "Time" column was normalized to bring it within a consistent range.

4. **Data Splitting**:
   - The dataset was split into training, testing, and validation sets for model development and evaluation.
   - The training set contains the majority of the data, while the validation set is used for fine-tuning hyperparameters.

5. **Model Selection and Training**:
   - Several machine learning models were used for credit card fraud detection, including:
     - Logistic Regression
     - Random Forest Classifier
     - Gradient Boosting Classifier
     - Support Vector Classifier (SVC)
   - Each model was trained on the training dataset.

6. **Model Evaluation**:
   - Model performance was evaluated using classification metrics such as accuracy, precision, recall, and F1-score.
   - Classification reports were generated to assess the model's ability to detect fraud and non-fraud transactions.

7. **Handling Class Imbalance**:
   - In cases where class imbalance was present (i.e., a significant difference between fraud and non-fraud samples), techniques like oversampling and undersampling were used to balance the dataset.

8. **Model Fine-Tuning and Improvement**:
   - Model hyperparameters were fine-tuned to optimize performance.
   - Different architectures and hyperparameters were explored for neural network models to enhance fraud detection.

9. **Exporting the Final Model**:
   - The final trained model, along with any required preprocessing transformers (e.g., scalers or encoders), was serialized and saved for later use in the Flask API.

10. **Model Selection and Comparison**:
    - The performance of multiple models, including logistic regression, random forest, gradient boosting, and support vector classification, was compared to identify the best-performing model for credit card fraud detection.

11. **Handling Class Imbalance (Balanced Dataset)**:
    - In situations with class imbalance, a balanced dataset was created by sampling an equal number of fraudulent and non-fraudulent transactions.

12. **Reevaluation on Balanced Dataset**:
    - The best-performing models were reevaluated on the balanced dataset to assess their performance on detecting fraud while mitigating the effects of class imbalance.

13. **Summary of Model Performance**:
    - The classification reports provide a detailed summary of each model's performance in terms of precision, recall, F1-score, and accuracy for both fraud and non-fraud classes.

These steps outline the process of developing and evaluating the machine learning models for credit card fraud detection. The final models, along with the preprocessing steps, are integrated into the Flask API for real-time fraud detection.

## 🌐 API Endpoints and Example Usage

The Credit Card Fraud Detection Flask API provides the following endpoint for predicting whether a given transaction is fraudulent or not:

### `/predict` (POST)

This endpoint accepts a JSON request containing the transaction data to be predicted. To use this endpoint, you should also set a request header to skip the ngrok browser warning, as ngrok may display a warning page otherwise.

**Request Header:**
```
ngrok-skip-browser-warning: true
```

**Request Body:**
```json
{
    "data": {
        "V1": -1.359807,
        "V2": -0.072781,
        "V3": 2.536347,
        ...
        "V28": -0.021053,
        "Amount": 149.62,
        "Time": 1
    }
}
```

**Response:**
- If the response is `1`, it indicates that the transaction is likely fraudulent.
- If the response is `0`, it indicates that the transaction is not fraudulent.
- If there is an error, the API may respond with an appropriate HTTP status code and an error message.

### Example Usage

You can use the provided test script in the `testcode/` folder, `sample.py`, to make requests to the API. Here's how to use it:

1. Ensure that the Flask API is running locally, and ngrok is set up to expose the API.

2. Navigate to the `testcode/` folder in your terminal:

   ```bash
   cd testcode/
   ```

3. Run the test script, specifying the transaction data you want to predict as a JSON object:

   ```bash
   python sample.py 
   ```

   This script sends a POST request to the `/predict` endpoint with the provided transaction data and the `ngrok-skip-browser-warning` header set to `true`.

4. The script will display the API response, indicating whether the transaction is likely fraudulent or not.

Example Output:
```
Prediction: 0.0 --> Not Fraud
```


## 🙏 Acknowledgments

Much of what I learned and applied in this project was learnt from [Gregg Hogg's](https://www.youtube.com/GregHogg) YouTube channel. His tutorials and content in machine learning and data science significantly influenced the development.

## 🤝 Contributions Welcome

Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or new features, please feel free to fork this repository, make your changes, and submit a pull request. Let's collaborate to make this project even better.
