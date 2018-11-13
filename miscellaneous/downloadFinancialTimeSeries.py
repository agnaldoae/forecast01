#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Requirements instructions: https://pypi.org/project/fix-yahoo-finance/#description

import fix_yahoo_finance as yt
import os

ticker = "  "

s_data = input("Enter start date (YYYY-MM-DD): ")
e_data = input("Enter end date (YYYY-MM-DD): ")
ticker = input("Enter stock symbol (e.g. APPL) or ! to exit: ")

os.makedirs("datasets",exist_ok=True)

while ticker != "!":
    print('\nloading: \'{0}\' '.format(ticker))
    try:
        stockPrices = yt.download(ticker, start= s_data, end= e_data)
        print('ok: \'{0}\' '.format(ticker))
        stockPrices.to_csv("./datasets/"+ ticker +".csv", sep=',')
    except ValueError:
        print("Error - maybe wrong Symbol - check out!")
    ticker = input("Enter stock symbol (e.g. APPL) or ! to exit: ")

print("... Finished.")
