# Feature and Graph structure learning-integrated Graph Convolutional Network

This repository implements **FaGGCN**, a graph convolutional network that integrates feature learning and graph-structure learning for multi-omics cancer subtype classification and survival analysis.

<img width="624" height="441" alt="image" src="Figure 1.png" />

## 🧠 Overview

FaGGCN is composed of three main stages:

1. **Survival-Guided Feature Learning**  
   Trains convolutional autoencoders to obtain information-rich latent features, then leverages patient survival data to select key features significantly associated with outcomes.

2. **Graph Construction via Autoencoding & Similarity Fusion**  
   Uses a graph autoencoder to combine the selected key features with inter-omics similarity fusion matrices, yielding a comprehensive patient network.

3. **GCN-based Patient Classification**  
   Applies a graph convolutional network that integrates the key features and the learned patient network to perform precise subtype classification.

## 🚀 Quick Start

First, please unzip the example dataset `data.zip` for testing.

Before running the project, make sure you have Python 3.8 or later installed. Then install the required packages:

```bash
# Download the required installation package
pip install -r requirements.txt
```
Next, run `python main_GCN_BRCA.py` or `python main_GCN_COAD.py` for classification.

If you wish to begin experimenting with feature extraction, please install the package using:
```bash
# Download the installation package required for feature extraction and graph construction
pip install -r requirements_for_extract_feature.txt
```
Then run `python CAE_SNF_GAE.py`.


## ⚙️  Structure
```
FaGGCN/
├── data/# Example data
│   ├── BRCA/                           # BRCA-specific input files
│   └── COAD/                           # COAD-specific input files
│
├── DataProcess/
│   └── Process.py                      # Data preprocessing
│
├── model/
│   ├── GCNpackage.py                   # GCN model + training/validation
│   ├── edge_predictor.py               # Edge prediction / VGAE-related modules
│   ├── myCAE.py                        # Convolutional autoencoder (feature learning)
│   ├── myCAEsaveModel.py               # CAE variants and model save
│   ├── Survive_select.py               # Survival-guided feature selection (Cox, etc.)
│   └── utils.py                        # Survival-analysis utilities (CoxPH C-index, etc.)
│
├── CAE_SNF_GAE.py                      # Feature extraction + Graph construction
├── main_GCN_BRCA.py                    # Classification on BRCA
├── main_GCN_COAD.py                    # Classification on COAD
│
├── requirements.txt                    # Dependencies for GCN classification
├── requirements_for_extract_feature.txt# Extra deps for feature extraction (TF, lifelines, …)
├── data.zip                            # Compressed dataset (unzip into ./data/)
├── Figure 1.png                        # Method overview figure
└── README.md                           # Project README
```

## 🧪 Dataset
The complete dataset can be accessed from the TCGA hub at `https://xenabrowser.net/datapages/`
- **Source:** UCSC Xena (The Cancer Genome Atlas, TCGA) Data Hub
- **Types of Cancer Datasets:** 

Breast Cancer (BRCA), Bladder Cancer (BLCA), Colon Adenocarcinoma (COAD), Uterine Corpus Endometrial Carcinoma (UCEC), Stomach Adenocarcinoma (STAD), Head and Neck Squamous Cell Carcinoma (HNSC), Thyroid Cancer (THCA), and Renal Cell Carcinoma (RCC).
- **Types of Omics Datasets:**


RNA-seq, MiRNA-seq, Copy number variation (CNV), and Somatic mutations (SNP)


## ⚙️ Requirements

```bash
- numpy==1.26.4
- scipy==1.13.1
- pandas==1.5.3
- scikit-learn==1.5.2
- matplotlib==3.9.2
- seaborn==0.13.2
- snfpy==0.2.2
- torch==2.3.1
- torchvision==0.18.1
- torchaudio==2.3.1
- tensorflow==2.15.1
- keras==2.15.0
- lifelines==0.30.0
- tensorflow-metal==1.1.0
```

