<div align="center">

# 🫀 CardioVision AI

### AI-Assisted Cardiovascular Risk Screening from Retinal Fundus Images

**Deep Learning • Computer Vision • Explainable AI • Medical AI**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-orange?logo=pytorch)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?logo=opencv)
![Jupyter](https://img.shields.io/badge/Jupyter-Research-orange?logo=jupyter)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

**Exploring whether retinal fundus images can provide useful signals for cardiovascular risk prediction.**

</div>

---

## 🔍 About

**CardioVision AI** is a research-oriented medical AI project that uses **retinal fundus photography and deep learning** to investigate cardiovascular risk.

The retina provides a non-invasive view of the body's microvasculature. CardioVision AI explores whether retinal features, vascular characteristics, and clinical information can be combined to estimate cardiovascular risk.

> **Retinal Image → AI Analysis → Cardiovascular Risk Prediction**

---

## 🏗️ System Architecture

```mermaid
flowchart LR

A[👁️ Retinal Fundus Image]
--> B[Image Preprocessing]

B --> C[🧠 Deep Learning Model]

C --> D[Retinal Features]

D --> E[🩸 Vessel Analysis]

E --> F[Multimodal Fusion]

M[Clinical Metadata<br/>Age • Sex • Risk Factors]
--> F

F --> G[❤️ Risk Prediction]

G --> H[📊 Risk Score]

G --> I[🔍 Explainability]

🚀 Key Features
🧠 Deep Learning using EfficientNet
👁️ Retinal fundus image analysis
🩸 Retinal vessel analysis
🧬 Multimodal image + clinical data fusion
🔍 Explainable AI with Grad-CAM & SHAP
📊 Clinical-style risk visualization
🛡️ Calibration & uncertainty estimation
🌍 External validation & subgroup analysis
📊 Current Results
EfficientNet-B0 — Improved Model
Metric	Score
Accuracy	77.66%
Precision	89.83%
Recall	77.18%
F1 Score	83.03%
ROC-AUC	85.38%
Confusion Matrix
                 Predicted
              Normal  Abnormal
Actual Normal    67       18
       Abnormal  47      159

These are research-stage results and should not be interpreted as clinical performance.

🧪 Research Approach

CardioVision AI follows a controlled experimental workflow:

Dataset Audit
     ↓
Patient-Level Split
     ↓
EfficientNet Baseline
     ↓
Model Improvement
     ↓
Validation & Evaluation
     ↓
Explainability
     ↓
Vessel-Aware Modeling
     ↓
Multimodal Learning
     ↓
External Validation

Patient-level splitting is used to reduce the risk of data leakage when multiple images belong to the same patient.

🛠️ Tech Stack
Area	Technology
Language	Python 3.11
Deep Learning	PyTorch
Vision	Torchvision, Timm
Computer Vision	OpenCV
ML & Evaluation	Scikit-learn
Augmentation	Albumentations
Research	Jupyter Notebook
Development	VS Code
Version Control	Git + GitHub
Hardware	Apple Silicon / MPS
📁 Project Structure
cardiovision-ai/
│
├── data/              # Dataset & processed data
├── docs/              # Research documentation
├── experiments/       # Experiment artifacts
├── models/            # Model checkpoints
├── notebooks/         # Research experiments
├── src/               # Core Python code
├── tests/             # Tests
│
├── configs/           # Configuration files
├── requirements.txt
├── environment.yml
└── README.md
🛣️ Roadmap
 Project foundation
 Dataset research & audit
 EfficientNet baseline
 Model improvement
 Robust threshold selection
 Grad-CAM explainability
 Retinal vessel segmentation
 Vessel feature extraction
 Multimodal learning
 Calibration & uncertainty
 External validation
 Clinical-style dashboard
🎯 What Makes CardioVision AI Different?

Instead of building only an image classifier, the project aims to combine:

👁️ Retinal Features + 🩸 Vascular Features + 🧬 Clinical Metadata

with:

Explainability + Calibration + External Validation

The focus is on building a research-grade and interpretable medical AI pipeline, rather than simply maximizing one metric.

⚠️ Medical Disclaimer

CardioVision AI is an academic/research prototype.

It is not a medical device and has not been clinically validated for patient care.

It must not be used to diagnose disease, estimate individual clinical risk, recommend treatment, or replace a qualified medical professional.

👨‍💻 Author

Shimant Ranjan
Computer Science & Engineering | Machine Learning | Computer Vision

GitHub

<div align="center">
🫀 CardioVision AI

AI × Retinal Imaging × Cardiovascular Research

⭐ Star the repository if you find the project interesting.

</div> ```