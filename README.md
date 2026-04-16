# ⚖️ AI Mizan Analytics: Iranian Food Price Predictor

[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Yousef-Elbeyaly/AI_Mizan)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AI Mizan** is an advanced predictive analytics system built to monitor and forecast food commodity prices within the Iranian market. Leveraging Machine Learning, this project provides data-driven insights into market trends amidst high economic volatility.

## 🚀 Project Overview
In fluctuating economies, accurate data is the only stable metric. This project analyzes historical World Food Programme (WFP) data to predict future prices in Iranian Rials (**IRR**), while providing a real-time estimation in United States Dollars (**USD**) based on unofficial market rates. This helps users understand inflation trends from both a local and global perspective.

## ✨ Key Features
* **High-Precision Forecasting:** Built on optimized Regression models trained on large-scale historical price datasets.
* **Premium Dashboard:** A modern, sleek Dark Mode UI crafted with Tailwind CSS and Flask.
* **Dual-Currency Support:** Displays predictions in IRR with an automatic conversion to USD (Unofficial Exchange).
* **Volatility Analysis:** Incorporates "Market Condition" variables (Standard vs. Conflict) to simulate crisis impact on pricing.
* **Dynamic UX:** Interactive commodity filtering system for a seamless user experience.

## 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning:** Scikit-Learn (Pipeline architecture, ColumnTransformer, Standard Scaler)
* **Data Processing:** Pandas, NumPy
* **Backend:** Flask
* **Frontend:** HTML5, Jinja2, Tailwind CSS
* **Deployment:** Docker & Hugging Face Spaces

## 📂 Project Structure
```text
├── artifacts/           # Trained models & preprocessing pickles
├── src/
│   ├── components/      # Data Ingestion, Transformation, Model Trainer
│   ├── pipeline/        # Training & Prediction pipelines
│   ├── logger.py        # Custom logging system
│   └── exception.py     # Custom exception handling
├── templates/           # Web interface (Home & Predictor pages)
├── app.py               # Flask application entry point
└── requirements.txt     # Dependency list
```
## ⚙️ Installation & Usage
```Clone the Repository:

Bash
git clone [https://github.com/Yousef-Elbeyaly/Iran_food_price_predictor.git](https://github.com/Yousef-Elbeyaly/Iran_food_price_predictor.git)
cd Iran_food_price_predictor
Install Dependencies:

Bash
pip install -r requirements.txt
Run Locally:

Bash
python app.py
Access the app at http://127.0.0.1:5000
```

👨‍💻 Developer
** Yousef Elbeyaly **

** LinkedIn: Yousef Elbeyaly **

** GitHub: @Yousef-Elbeyaly **

Developed with ⚡ by Yousef Elbeyaly - 2026
