import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import configparser  # in Python 2.x use 'configParser'
import tensorflow as tf
from keras.models import Sequential 


if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read('config.ini')
    DATA_DIR = config['PATHS']['DATA_DIR']
    HEADER = int(config['DEFAULT']['HEADER'])
    INDEX_COL  = int(config['DEFAULT']['INDEX_COL'])

    #print(data_dir)
    df = pd.read_csv(DATA_DIR, header=HEADER, index_col=INDEX_COL)
 
    df['Close'].plot()
    plt.title('AT&T share prices')
    plt.xlabel('Date')
    plt.ylabel('Price (US$)')
    plt.legend()
    plt.show()
    print("Hello world")

