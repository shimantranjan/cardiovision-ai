# CardioVision AI

### Retinal Fundus Image Analysis for Cardiovascular Risk Research

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![TorchVision](https://img.shields.io/badge/TorchVision-Computer%20Vision-EE4C2C)](https://pytorch.org/vision/)
[![Scikit--learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Experiments-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)](https://github.com/shimantranjan/cardiovision-ai)

> **CardioVision AI** is a research-oriented medical AI system investigating whether retinal fundus photographs contain useful signals associated with cardiovascular risk.

---

## Overview

The retina provides a non-invasive view of the body's microvascular structure.  
CardioVision AI explores the relationship between **retinal appearance, vascular characteristics, and cardiovascular-related risk indicators** using computer vision and machine learning.

The project combines:

- Retinal fundus image analysis
- Deep learning with EfficientNet
- Retinal vascular feature extraction
- Classical machine learning
- Multimodal feature fusion
- Explainable AI
- Threshold optimization
- Patient-level evaluation

### Research Pipeline

```text
Retinal Fundus Image
        │
        ▼
Image Preprocessing
        │
        ▼
Deep Learning Feature Extraction
        │
        ├───────────────┐
        ▼               ▼
EfficientNet-B0    Vascular Features
        │               │
        └───────┬───────┘
                ▼
        Feature Fusion
                │
                ▼
       Cardiovascular Risk
          Classification
                │
        ┌───────┴────────┐
        ▼                ▼
 Performance        Explainability
 Evaluation           Analysis
Key Objectives
1. Retinal Image Analysis

Develop a deep learning pipeline capable of learning visual representations from retinal fundus photographs.

2. Vascular Phenotyping

Extract quantitative characteristics from retinal vasculature and investigate their predictive value.

3. Multimodal Learning

Combine image-derived information with structured retinal/clinical features.

4. Explainable AI

Investigate which retinal regions and vascular characteristics influence model predictions.

5. Reliable Evaluation

Evaluate models using clinically relevant classification metrics rather than relying only on accuracy.

Dataset

CardioVision AI currently uses the China-Fundus-Carotid Intima-Media Thickness (CIMT) dataset.

Property	Value
Patients	2,903
Fundus Images	5,806
Eyes	Bilateral
Image Type	Retinal Fundus Photography
Target	CIMT-based cardiovascular-related classification
Input Resolution	512 × 512
Classes	Normal / Abnormal
Dataset Split
Split	Patients
Training	2,322
Validation	290
Test	291
Total	2,903

Important: Patient-level splitting is used to reduce the possibility of information leakage between training, validation, and test sets.

Model Architecture

The primary deep learning backbone is EfficientNet-B0 using pretrained ImageNet weights.

                 ┌──────────────────────┐
                 │   Retinal Fundus     │
                 │       Image          │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Image Preprocessing  │
                 │ Resize / Normalize   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    EfficientNet-B0   │
                 │   Feature Extractor  │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Learned Image        │
                 │ Representation       │
                 └──────────┬───────────┘
                            │
                 ┌──────────┴──────────┐
                 │                     │
                 ▼                     ▼
       ┌─────────────────┐   ┌─────────────────┐
       │ Vascular        │   │ Clinical /      │
       │ Features        │   │ Structured Data │
       └────────┬────────┘   └────────┬────────┘
                │                     │
                └──────────┬──────────┘
                           ▼
                 ┌──────────────────────┐
                 │   Feature Fusion     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Risk Classification  │
                 └──────────────────────┘
Machine Learning Components
Deep Learning
EfficientNet-B0
Transfer learning
Class-balanced loss
Adam optimizer
Learning-rate scheduling
Early stopping
Validation-based model checkpointing
Classical Machine Learning

Vascular features are additionally investigated using classical machine learning models:

RBF Support Vector Machine
Gradient Boosting
Extra Trees
Random Forest
Ensemble approaches

This allows comparison between deep visual representations and quantitative vascular features.

Explainable AI

Medical AI systems should not only produce predictions; they should also provide insight into why a prediction was produced.

CardioVision AI therefore includes an explainability pipeline based on Grad-CAM.

Fundus Image
     │
     ▼
Trained CNN
     │
     ▼
Model Prediction
     │
     ▼
Grad-CAM
     │
     ▼
Activation Heatmap
     │
     ▼
Important Retinal Regions

The objective is to investigate whether model attention aligns with meaningful retinal structures rather than irrelevant image artifacts.

Vascular Feature Analysis

The project also investigates retinal vascular characteristics as structured features.

Examples include:

Vessel density
Vessel calibre
Vessel branching characteristics
Vessel-related statistical measurements
Quantitative retinal vascular descriptors

These features can be evaluated independently and combined with deep image representations.

Evaluation

CardioVision AI evaluates models using multiple complementary metrics.

Metric	Purpose
Accuracy	Overall classification correctness
Precision	Reliability of positive predictions
Recall	Ability to identify positive cases
F1 Score	Balance between precision and recall
ROC-AUC	Ranking/discrimination performance
Confusion Matrix	Class-specific error analysis
Current Improved Image Model
Metric	Score
Accuracy	0.7766
Precision	0.8983
Recall	0.7718
F1 Score	0.8303
ROC-AUC	0.8538
Validation-Based Threshold Analysis

A validation-set threshold analysis was also performed to study the precision/recall trade-off.

The current research direction is to:

Select the classification threshold using validation data.
Lock the selected threshold.
Evaluate it once on the held-out test set.
Avoid using the test set repeatedly for optimization.

This prevents test-set overfitting and produces a more defensible evaluation.

Experimental Workflow
Dataset Audit
      │
      ▼
Patient-Level Split
      │
      ▼
Baseline EfficientNet
      │
      ▼
Model Improvement
      │
      ▼
Threshold Analysis
      │
      ▼
Vascular Feature Analysis
      │
      ▼
Multimodal Fusion
      │
      ▼
Explainability
      │
      ▼
Final Evaluation
Project Structure
cardiovision-ai/
│
├── app/
│   └── Application / inference components
│
├── configs/
│   └── baseline.yaml
│
├── data/
│   ├── raw/
│   │   └── china_fundus_cimt/
│   ├── processed/
│   └── external/
│
├── docs/
│   ├── dataset/
│   ├── DATASET_COMPARISON.md
│   ├── DATASET_RESEARCH.md
│   └── ROADMAP.md
│
├── experiments/
│   └── Experiment outputs and records
│
├── models/
│   └── Saved model checkpoints
│
├── notebooks/
│   ├── 01_dataset_audit.ipynb
│   ├── 02_model_improvement.ipynb
│   ├── 03_gradcam_explainability.ipynb
│   └── 04_vessel_analysis.ipynb
│
├── src/
│   ├── data/
│   ├── evaluation/
│   ├── models/
│   ├── config.py
│   ├── inference.py
│   └── seed.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
Research Experiments

The project is organized as a sequence of reproducible experiments.

Experiment	Objective
Dataset Audit	Understand data distribution and quality
Baseline Model	Establish initial performance
Improved Model	Improve representation learning
Threshold Optimization	Study precision/recall trade-offs
Vascular Analysis	Evaluate retinal vascular descriptors
Multimodal Fusion	Combine complementary information
Grad-CAM	Investigate model interpretability
Final Evaluation	Lock methodology and report results
Technology Stack
Category	Technology
Language	Python
Deep Learning	PyTorch
Computer Vision	TorchVision
Machine Learning	Scikit-learn
Data Processing	Pandas / NumPy
Visualization	Matplotlib
Experiments	Jupyter Notebook
Development	VS Code
Version Control	Git / GitHub
Why This Project Matters

Cardiovascular disease remains a major global health challenge, while retinal fundus photography provides a relatively inexpensive and non-invasive method of observing microvascular structures.

CardioVision AI investigates whether these retinal signals can support cardiovascular risk assessment through machine learning.

The project is particularly focused on:

Non-invasive screening
Computer vision for healthcare
Retinal vascular biomarkers
Explainable medical AI
Multimodal prediction
Reproducible model evaluation
Research Philosophy

The objective is not to artificially maximize a single metric.

Instead, the project prioritizes:

Generalization → Robust evaluation → Explainability → Reproducibility

A model that performs well on one dataset but fails on unseen data is not considered a successful medical AI system.

Current Status
Completed
 Dataset acquisition and organization
 Dataset audit
 Patient-level train/validation/test split
 EfficientNet-B0 baseline
 Improved EfficientNet-B0 training
 Class-balanced training
 Validation threshold analysis
 Vascular feature analysis
 Classical ML experiments
 Multimodal feature experiments
 GitHub-based experiment tracking
In Progress
 Robust Grad-CAM analysis
 Final multimodal architecture
 Improved vascular feature extraction
 Calibration and uncertainty analysis
 Final held-out test evaluation
 Research documentation

Limitations

This project is currently a research prototype and should not be interpreted as a clinical diagnostic system.

Important limitations include:

Dataset size and demographic coverage
Potential dataset-specific bias
Limited external validation
Retrospective dataset design
Possible confounding by age and other clinical variables
Need for prospective clinical validation

Clinical deployment would require substantially stronger validation, regulatory review, and evaluation across independent populations.

Future Roadmap
Current
   │
   ├── Deep Learning
   │      └── EfficientNet improvements
   │
   ├── Vascular Analysis
   │      └── Quantitative retinal features
   │
   ├── Explainability
   │      └── Grad-CAM
   │
   └── Multimodal Learning
          │
          ▼
     Better Feature Fusion
          │
          ▼
     Calibration & Uncertainty
          │
          ▼
     External Validation
          │
          ▼
     Research-Grade Prototype
Reproducibility

The project is developed with reproducibility in mind.

Key practices include:

Fixed random seeds where appropriate
Patient-level dataset splitting
Version-controlled notebooks
Saved model checkpoints
Explicit experiment configurations
Validation-based model selection
Held-out test evaluation
Disclaimer

CardioVision AI is an academic/research project.

It is not a medical device, does not provide medical diagnosis, and should not be used for clinical decision-making.

All model results should be interpreted as experimental findings requiring further validation.

Author

Shimant Ranjan

Computer Science & Engineering
Machine Learning • Computer Vision • Medical AI
