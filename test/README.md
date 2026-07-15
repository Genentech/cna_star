To run the test case, please first run
```
python generate_test_data.py
```

This will create 1 file under ./input:
1. test_scdata.h5ad -- a simulated single-cell data with 600 cells of 10 different cell types across 20000 genes for 30 donors

Please then run:
1. ```python run_cna_star.py``` -- for estimating variance in phenotype attributable variations in cell abundance at each cell neighborhood
2. ```sh run_aggregate.sh``` -- for aggregating the results in the previous step by cell types

In ./output, please find:
1. Output from running ```python run_cna_star.py```: test_scdata_output.parquet
2. Output from running ```sh run_aggregate.sh```: test_scdata_output.aggregate.CellType.txt.gz