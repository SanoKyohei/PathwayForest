import pandas as pd
import numpy as np

def MTX(Df,gene_100):
    Df100=Df.loc[gene_100]    
    MTX=pd.DataFrame()
    N=len(gene_100)
    
    for col in Df100.columns:
        data=pd.DataFrame(Df100[col].sort_values(ascending=False))
        k=0
        i=1
        Equal={}
        Equal[k]=[]
        while i <N:
            gene=data.index[i]
            if data.iloc[i,0]==data.iloc[i-1, 0]:
                Equal[k].append(i-1)
                Equal[k].append(i)
                i=i+1
            else:
                k=k+1
                Equal[k]=[]
                i=i+1


        X=np.repeat(-2,N*N).reshape(N, N)
        X[np.diag_indices_from(X)]=-1
        X=np.tril(X)
        X=X+1
        X=pd.DataFrame(X)

        for k in Equal.keys():
            X.iloc[Equal[k], Equal[k]]=0

        Mtx10000=X
        Mtx10000.index=data.index
        Mtx10000.columns=data.index
        Mtx10000=Mtx10000.sort_index()
        Mtx10000=Mtx10000.T
        Mtx10000=Mtx10000.sort_index()
        Mtx10000=Mtx10000.T

        Mtx10000=np.array(Mtx10000)
        Mtx10000=list(Mtx10000[np.triu_indices(N, k = 1)])
        Mtx10000=pd.DataFrame(Mtx10000)
        Mtx10000.columns=[col]
        MTX=pd.concat([MTX,Mtx10000 ],axis=1)
    return MTX
    
