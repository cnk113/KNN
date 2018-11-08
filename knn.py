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
            dist += (x[i]*y[i])**2
        dist = math.sqrt(dist)
    else:
        highest = abs(x[3]-y[3])
        for i in range(4):
            if abs(x[i]-y[i]) > highest:
                highest = abs(x[i]-y[i])
        dist = highest
    return (dist,)

def KNN(train,K,test,l):
    S = []
    for n in range(len(test)):
        S.append(distance(test,test[n],n,l))
    S.sort()
    label = 0
    labels = []
    for k in range(K):
        if distance(test[k],S[k],l) ...:
            label =
        else:
            label = 
        labels.append(label)
    return label

def parse_args(): # DONE
    parser = argparse.ArgumentParser(description = 'Implements KNN and takes in K and distance metric')
    parser = add_argument('--K', type=int, help = 'number of nearest neighbors')
    parser = add_argument('--method', help = 'distance metric: L1, L2, or Linf')
    return parser.parse_args()

def parse_csv(csv): #DONE
    df = pd.read_csv(csv,delimter='\t')
    lists = [list(x) for in df.values]
    return lists

def main():
    opts = parse_args()
    train = parse_csv('knn_train.csv')
    test = parse_csv('knn_test.csv')
    labels = KNN(train,opts.K,test,opts.method)
    for n in labels:
        print(n)
    
if __name__ == '__main__':
    main()
