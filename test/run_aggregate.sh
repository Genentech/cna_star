python ../aggregate_cna.py \
    --cna-ncorrs ./output/test_scdata_output.parquet \
    --donor-id-col "Donor" \
    --block-bootstrap "CNA_nbhood_cluster" \
    --cell-type-col CellType \
    --out ./output/test_scdata_output.aggregate.CellType.txt.gz
