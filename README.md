# CNA*

CNA* is an exention of [CNA](https://github.com/immunogenomics/cna), for estimating the variance in disease phenotypes explained by variations in cell abundance in each cell neighborhoods across donors.

# Installation

## Option 1: using Anaconda or Miniforge
The easiest way to install CNA* is by creating a dedicated environment through [Anaconda](https://www.anaconda.com/download) or [Miniforge](https://github.com/conda-forge/miniforge). To do this, please first install Anaconda or Miniforge on your machine. You may then install CNA* using the following commands:
``` shell
git clone git@github.com:Genentech/cna_star.git
cd cna_star
conda env create -f cna_star.yml
conda activate cna_star
```

## Option 2: manually install required packages

The user may also manually install the required packages to run CNA* using the following commands:
```shell
conda install pandas=1.5.3
conda install numpy=1.26.2
conda install scipy=1.13.1
conda install scanpy=1.10.3
conda install anndata=0.10.7
conda install scikit-learn=1.3.2
conda install pyarrow=21.0.0
pip install multianndata==0.0.4
```

Once the required packages to run CNA* are installed, the user may then install CNA* using:
```shell
git clone git@github.com:Genentech/cna_star.git
```

# Testing CNA*

We provide examples script to test CNA* [here](https://github.com/Genentech/cna_star/tree/master/test).

# Contact

Please create a GitHub issue if you experience any issue with running scEPS.

# Reference

The current draft of the manuscript is available [here](https://www.medrxiv.org/content/10.64898/2026.06.26.26356714v1).
