import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
import gseapy as gp

#Inputs
expr_csv = "Summarized_gene_counts_2025-10-17v2.csv"

df = pd.read_csv(expr_csv)

