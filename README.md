# CNA*

CNA* is an exention of [CNA](https://github.com/immunogenomics/cna) ([Reshef*, Rumker* et al. 2022 Nat Biotech](https://www.nature.com/articles/s41587-021-01066-4)), for estimating, $\sigma^2_{na}$, the variance in disease phenotypes explained by variations in cell abundance in each cell neighborhoods across donors.

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

# Using CNA*

## Estimating $\sigma^2_{na}$ for individual cell neighborhoods

The user may use the [demo for CNA](https://github.com/immunogenomics/cna/blob/master/demo/demo.ipynb) as a reference, since CNA* has a similar interface as CNA.

CNA* also supports the following function arguments in ```cna_star.tl.association```:

* ```Nbs``` -- number of bootstrap samples for estimating standard errors of $\sigma^2_{na}$ for individual cell neighborhood
* ```cluster_neighborhood``` -- if set to ```True```, CNA* will perform clustering of cell neighborhoods based on the neighborhood abundance matrix
* ```num_kmeans_cluster``` -- number of neighborhood clusters for statistical block bootstrap for estimating standard errors for aggregated $\sigma^2_{na}$

CNA* returns the following results in addition the outputs from CNA:

* ```nbhood_varexp``` -- $\sigma^2_{na}$ at each cell neighborhood
* ```nbhood_varexp_anse``` -- analytical standard error for $\sigma^2_{na}$
* ```nbhood_varexp_bsse``` -- bootstrap standard error for $\sigma^2_{na}$ (if ```Nbs``` > 0)
* ```nbhood_cluster``` -- cluster that cell neighborhood is assigned to (if ```cluster_neighborhood``` is set to ```True```)

# Testing CNA*

We provide examples script to test CNA* [here](https://github.com/Genentech/cna_star/tree/master/test).

# Contact

Please create a GitHub issue if you experience any issue with running scEPS.

# Reference

The current draft of the manuscript that describes CNA* is available [here](https://www.medrxiv.org/content/10.64898/2026.06.26.26356714v1).