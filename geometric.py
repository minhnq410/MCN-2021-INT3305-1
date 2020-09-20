import math

def prob(n, p):
    '''
    Tra ve gia tri la xac suat cua symbol thu n cua nguon tin Geometric
    ---
    Parameters:
    -   n: int
        So thu tu cua symbol
    -   p: float
        Xac suat cua 1 phep thu
    Return:
        Xac suat cua symbol n
    '''
    return (1-p)**(n-1)*p

def infoMeasure(n, p):
    '''
    Tinh luong thong tin cua symbol n cua nguon tin Geometric
    ---
    Parameters:
    -   n: int
        So thu tu cua symbol
    -   p: float
        Xac suat cua 1 phep thu
    Return:
        Luong thong tin cua symbol n
    '''
    return -math.log2(prob(n, p))

def sumProb(N, p):
    '''
    Tinh tong xac suat cua cac symbol tu 1 den N cua nguon tin Geometric
    ---
    Parameters:
    -   N: int
        So thu tu cua symbol cuoi
    -   p: float
        Xac suat cua 1 phep thu
    Return:
        Tong xac suat cua symbol tu 1 den N
    ---
    Bien luan:
    Tong xac suat phan bo Geometric = 1
    Thuc nghiem:
        N = 1000, p = 0.3, ham tra ve 0.9999999999999998
        N = 1000, p = 0.9, ham tra ve 1.0
        N = 2000, p = 0.3, ham tra ve 0.9999999999999998
    '''
    S = 0.0
    n = N
    while n > 0:
        S += prob(n, p)
        n -= 1
    return S

def approxEntropy(N, p):
    '''
    Tinh luong tin trung binh cua cac symbol cua nguon tin Geometric tu 1 den N
    ---
    Parameters:
    - N: int
        So thu tu cua symbol cuoi
    - p: float
        Xac suat cua 1 phep thu
    Return:
        Luong tin trung binh cua cac symbol tu 1 den N
    ---
    Bien luan:
    Voi p = 0.5, entropy cua nguon tin la tong n/2^n voi n = 1..N va bang 2
    That vay:
        N =  500, ham tra ve 2.0
        N = 1000, ham tra ve 2.0
        N = 2000, ham tra ve 2.0
    '''
    H = 0.0
    n = N
    while n > 0:
        H += prob(n, p) * infoMeasure(n, p)
        n -= 1
    return H
