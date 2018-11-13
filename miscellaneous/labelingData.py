#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os


def labelingSignal(ts, index, window):
    signal = 'hold'
    high = 0
    low = 99999
    if (index+window) > len(ts):
        return 'error'
    for i in range(index-window, index+window+1):
        if ts[i] > high:
            high = ts[i]
        elif ts[i] < low:
                low = ts[i]
    if ts[index] == high:
        signal = 'sell'
    elif (ts[index] == low):
            signal = 'buy'
    return signal


## Main
if __name__ == "__main__":

    window = int(input("Enter window size: "))
    wd = int(window/2)
    path = input("Enter relative path to folder: ")
    symbol = input("Enter stock symbol: ")
    
    os.makedirs("./labels",exist_ok=True)
    
    while symbol != "!":
        # reading file
        df = pd.read_csv(path+"/"+symbol+".csv", engine='python')
        # getting "Adjust Closes prices" as float
        ts = df["Adj Close"].values
        # empty list to store the labels
        lts = list()
        size = len(ts)
        # for each window
        for idx in range(0, size):
            if (idx < wd or idx >= size - wd) :
                lts.append(np.NaN)
            else:
                label = labelingSignal(ts.astype('float32'), idx, wd)
                lts.append(label)
        # including column of labels
        df["Labels"] = lts
        #wrinting result
        filepath = "./labels/"+symbol+".csv" 
        df.to_csv(filepath)
        
        # Updating symbol to next interation
        symbol = input("Enter stock symbol or ! to stop: ")

        
