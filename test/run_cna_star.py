import sys
sys.path.append('..')
from src import cna_star

import scanpy as sc
import multianndata as mad

def main():

    # read in data
    adata = sc.read_h5ad('./input/test_scdata.h5ad')

    # run cna_star
    d = mad.MultiAnnData(adata, sampleid='Donor')
    d.obs_to_sample(['Pheno'])
    res = cna_star.tl.association(d,
                            d.samplem['Pheno'],
                            seed=0,
                            ks=[4,5,6,7,8,9,10,11,12,13,14,15],
                            Nbs=1000,
                            cluster_neighborhood=True,
                            num_kmeans_cluster=100)

    # save output
    obs = adata.obs[res.kept].copy()
    obs['CNA_ncorrs'] = res.ncorrs
    obs['CNA_nbhood_varexp'] = res.nbhood_varexp
    obs['CNA_nbhood_varexp_anse'] = res.nbhood_varexp_anse
    obs['CNA_nbhood_varexp_bsse'] = res.nbhood_varexp_bsse
    obs['CNA_nbhood_cluster'] = res.nbhood_cluster
    obs.to_parquet('./output/test_scdata_output.parquet', compression='gzip')

if __name__ == '__main__':
    main()