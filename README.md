# FaGGCN
FaGGCN is a joint feature-learning and graph-structure-learning framework for multi-omics cancer subtyping: convolutional autoencoders learn survival-guided latent features, while a graph autoencoder plus GCN fuse inter-omics similarities into a comprehensive patient graph for precise classification.

<img width="416" height="274" alt="image" src="Figure 1.png" />

# How to run
First, please unzip the dataset `data.zip`.

Then install the required packages using `pip install -r requirements.txt`.

Next, run `python main_GCN_BRCA.py` or `python main_GCN_COAD.py` for classification.

If you wish to begin experimenting with feature extraction, please install the package using
`pip install -r requirements_for_extract_feature.txt`.Then run `python CAE_SNF_GAE.py`.
# Requirements
- Python 3.9
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
