import math

def prob(n, p, N):
    '''
    Tinh xac suat symbol n cua nguon tin Binomial
    khi thuc hien N phep thu voi xac suat p
    ---
    Parameters:
    -   n: int
        So thu tu cua symbol
    -   p: float
        Xac suat cua 1 phep thu
    -   N: int
        So phep thu thuc hien
    Return:
        Xac suat cua symbol n
    '''
    return math.comb(N, n)*(p**n)*((1-p)**(N-n))

def infoMeasure(n, p, N):
    '''
    Tinh luong tin symbol n cua nguon tin Binomial
    khi thuc hien N phep thu voi xac suat p
    ---
    Parameters:
    -   n: int
        So thu tu cua symbol
    -   p: float
        Xac suat 1 phep thu
    -   N: int
        So phep thu thuc hien
    Return:
        Luong thong tin cua symbol n
    '''
    return -math.log2(prob(n, p, N))

def sumProb(N, p):
    '''
    Tinh tong xac suat cua cac symbol cua nguon tin Binomial
    khi thuc hien N phep thu voi xac suat p
    ---
    Parameters:
    -   N: int
        So phep thu thuc hien
    -   p: float
        Xac suat 1 phep thu
    Return:
        Tong xac suat cac symbol cua nguon tin
    ---
    Bien luan:
        sumProb(100, 0.4) = 1.0000000000000002
        sumProb(1000, 0.4) = 1.0
        sumProb(1000, 0.2) = 1.0000000000000555
    Vay tong xac suat cua phan bo Binomial = 1
    '''
    S = 0.0
    n = N
    while n >= 0:
        S += prob(n, p, N)
        n -= 1
    return S

def approxEntropy(N, p):
    '''
    Tinh luong tin trung binh cac symbol cua nguon tin Binomial
    khi thuc hien N phep thu voi xac suat p
    ---
    Parameters:
    -   N: int
        So phep thu thuc hien
    -   p: float
        Xac suat 1 phep thu
    Return:
        Luong tin trung binh cua nguon tin
    '''
    H = 0.0
    n = N
    while n >= 0:
        H += prob(n, p, N) * infoMeasure(n, p, N)
        n -= 1
    return H
