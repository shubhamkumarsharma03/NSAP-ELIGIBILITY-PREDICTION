## 📘 Overview
This project automates the classification of applicants under the **National Social Assistance Programme (NSAP)** using machine learning models built on **IBM Watsonx.ai**. NSAP is a flagship welfare program by the Government of India targeting elderly citizens, widows, and persons with disabilities in **Below Poverty Line (BPL)** households.

The solution leverages AI to replace manual eligibility verification with a **multi-class classification model** that predicts the appropriate NSAP sub-scheme for each applicant based on socio-economic and demographic data.

---

## 🔍 Problem Statement
Manual verification of applications is often error-prone and time-consuming, leading to delays in benefit distribution. There is a strong need for an intelligent, automated system that can efficiently assign the correct scheme to each applicant.

**Objective:**  
Build a reliable machine learning classifier to predict eligibility for:
- 🧓 IGNOAPS (Old Age Pension)
- 👩‍🦳 IGNWPS (Widow Pension)
- ♿ IGNDPS (Disability Pension)

---

## 🛠️ Technologies Used
- ☁️ IBM Cloud Lite (Watson Studio, Cloud Object Storage)
- 🤖 IBM Watsonx.ai – AutoAI for automated ML pipeline generation
- 🐍 Python – Data formatting and preprocessing
- 📊 Dataset: [AI Kosh NSAP Dataset](https://aikosh.indiaai.gov.in/web/datasets/details/district_wise_pension_data_under_the_national_social_assistance_programme_nsap_1.html)

---

## 📊 Model Training Process
- AutoAI trained 8 pipelines using the provided dataset
- Best model: **Decision Tree Classifier**
- Achieved **96.7% accuracy**
- Automatic feature engineering and hyperparameter optimization (HPO)

---

## 💡 Prediction & Deployment
- Supports input in **table** and **JSON** formats
- Outputs: Predicted scheme + class probabilities
- Real-time predictions via IBM Watsonx.ai user interface
- Export-ready results in table or JSON format

---

## 📸 Results

### 🔷 AutoAI Pipeline Leaderboard
![AutoAI Leaderboard](images/autoai_leaderboard.png)

### ✅ Best Model Output Example
![Model Output](images/best_model_output.png)

### 🚀 Deployed Watsonx Interface
![Deployment UI](images/deployment_ui.png)

> 📁 Place your screenshots in a folder named `images/` in the repo root

---

## 🔭 Future Scope
- Add more NSAP schemes and eligibility logic
- Hybrid rule-based + ML classification system
- Aadhaar-linked verification for improved targeting
- REST API deployment for scalable bulk processing

---

## 🙏 Acknowledgements
- 💻 IBM Cloud Academic Initiative  
- 🇮🇳 AI Kosh Dataset by IndiaAI  
- 📚 Government of India – Ministry of Rural Development

---

## 📜 License
This project is open-sourced under the [MIT License](LICENSE).
