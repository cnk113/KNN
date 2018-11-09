# Chang Kim, Bryan Tor

import argparse
import pandas as pd
import math

def distance(x,y,l):
    dist = 0
    if l == 'L1':
        for i in range(4):
            dist += abs(x[i]-y[i]) 
    elif l == 'L2':
        for i in range(4):
            dist += (x[i]-y[i])**2
            dist = math.sqrt(dist)
    else:
        highest = abs(x[3]-y[3])
        for i in range(3):
            if abs(x[i]-y[i]) > highest:
                highest = abs(x[i]-y[i])
            dist = highest
    return dist 

def KNN(train,K,test,l):
    S = {}
    for n in range(len(train)):
        S[distance(train[n],test,l)] = train[n][4]
    sort = sorted(S.items(), key=lambda x: x[0])
    label = 0
    nn = sort[0:K]
    for n in nn:
        label += S.get(n[0])
    if label < 0:
        return -1
    else:
        return 1

def parse_args():
    parser = argparse.ArgumentParser(description = 'Implements KNN and takes in K and distance metric')
    parser.add_argument('--K', type=int, help = 'number of nearest neighbors')
    parser.add_argument('--method', help = 'distance metric: L1, L2, or Linf')
    return parser.parse_args()

def parse_csv(csv):
    df = pd.read_csv(csv)
    lists = [list(x) for x in df.values]
    return lists

def main():
    opts = parse_args()
    train = parse_csv('knn_train.csv')
    test = parse_csv('knn_test.csv')
    for i in range(len(test)):
        print(KNN(train,opts.K,test[i],opts.method))
    
if __name__ == '__main__':
    main()
