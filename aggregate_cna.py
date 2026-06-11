import sys, random, pickle, argparse, logging, gzip, os
import numpy as np
import pandas as pd
import scipy
import scipy.stats as stats

random.seed(0)
np.random.seed(0)

from tqdm import tqdm

def main():
    
    args = get_command_line()

    df_cna = pd.read_parquet(args.cna_ncorrs)
    dfd = pd.unique(df_cna[args.donor_id_col]).shape[0] - args.num_params

    df_out = []
    all_ct = pd.unique(df_cna[args.cell_type_col])
    for ct in tqdm(all_ct):

        df_cna_ct = df_cna[df_cna[args.cell_type_col]==ct]
        ncell = df_cna_ct.shape[0]
        if df_cna_ct.shape[0] == 0:
            continue

        nbhood_varexp = df_cna_ct['CNA_nbhood_varexp'].values
        nbhood_varexp_se = df_cna_ct['CNA_nbhood_varexp_anse'].values
        block_val = None
        if args.block_bootstrap != '':
            block_val = df_cna_ct[args.block_bootstrap].values

        mean_nbhood_varexp, se_mean_nbhood_varexp, p_mean_nbhood_varexp = \
            get_mean_nbhood_varexp(nbhood_varexp, nbhood_varexp_se, dfd, block_val)
        if args.parent_cell_type_col == '':
            df_out.append([ct, ncell, mean_nbhood_varexp, se_mean_nbhood_varexp, p_mean_nbhood_varexp])
        else:
            parent_ct = pd.unique(df_cna_ct[args.parent_cell_type_col])[0]
            df_out.append([ct, parent_ct, ncell, mean_nbhood_varexp, se_mean_nbhood_varexp, p_mean_nbhood_varexp])
    
    df_out = pd.DataFrame(df_out)
    if args.parent_cell_type_col == '':
        df_out.columns = ['CELL_TYPE', 'NCELL', 'MEAN_NBHOOD_VAREXP', 'SE_MEAN_NBHOOD_VAREXP', 'P_MEAN_NBHOOD_VAREXP']
    else:
        df_out.columns = ['CELL_TYPE', 'PARENT_CELL_TYPE', 'NCELL', 'MEAN_NBHOOD_VAREXP', 'SE_MEAN_NBHOOD_VAREXP', 'P_MEAN_NBHOOD_VAREXP']
    df_out.to_csv(args.out, sep='\t', index=False)


def get_mean_nbhood_varexp(nbhood_varexp, nbhood_varexp_se, dfd, block_val=None, nbs=1000):

    if block_val is not None:
        all_block = pd.unique(block_val)

    mean_nbhood_varexp = np.mean(nbhood_varexp)

    all_mean_nbhood_varexp_bs = np.zeros(nbs)

    if block_val is None:
        ncell = nbhood_varexp.shape[0]
        all_idx = np.array(range(ncell))
        for i in range(nbs):
            use_idx = np.random.choice(all_idx, size=ncell, replace=True)
            all_mean_nbhood_varexp_bs[i] = np.mean(nbhood_varexp[use_idx])
    else:
        nblock = all_block.shape[0]
        for i in range(nbs):
            use_block = np.random.choice(all_block, size=nblock, replace=True)
            use_idx = np.concatenate([np.where(block_val == blk)[0] for blk in use_block])
            all_mean_nbhood_varexp_bs[i] = np.mean(nbhood_varexp[use_idx])

    se_mean_nbhood_varexp = np.std(all_mean_nbhood_varexp_bs)
    z_mean_nbhood_varexp = mean_nbhood_varexp / (se_mean_nbhood_varexp + 1e-8)

    if block_val is None:
        p_mean_nbhood_varexp = 2 * (1 - stats.norm.cdf(np.fabs(z_mean_nbhood_varexp)))
    else:
        p_mean_nbhood_varexp = (1-scipy.stats.t.cdf(np.fabs(z_mean_nbhood_varexp), df=nblock-1))*2.0
    
    return mean_nbhood_varexp, se_mean_nbhood_varexp, p_mean_nbhood_varexp


def get_command_line():
 
    # Create the parser
    parser = argparse.ArgumentParser(description="Generate simulated data")

    # arguments for specifying input data
    parser.add_argument('--cna-ncorrs', type=str, required=False, help='CNA analysis output')
    
    parser.add_argument('--cell-type-col', type=str, required=False, help='Cell type column')

    parser.add_argument('--parent-cell-type-col', type=str, default='', required=False, help='Parent cell type column')

    parser.add_argument('--num-params', type=int, required=False, default=1,
                        help='Number of parameters in the regression model')

    parser.add_argument('--donor-id-col', type=str, required=False, default='',
                        help='Column for donor ID')

    parser.add_argument('--block-bootstrap', type=str, required=False, default='',
                        help='Perform block bootstrap based on the groups specified in the column')

    # output directory
    parser.add_argument('--out', type=str, required=False, help='Output prefix')

    # Execute the parse_args() method
    args = parser.parse_args()
    
    return args



if __name__ == '__main__':
    main()