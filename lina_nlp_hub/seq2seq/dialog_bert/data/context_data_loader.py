from torch.utils.data import Dataset

import os, sys
import dask.dataframe as dd

class ContextDataset(Dataset):
    def __init__(self, file_path_regex):
        df = dd.read_csv(file_path_regex)

    def __getitem__(self, index):
        pass

    def __len__(self):
        pass

        

