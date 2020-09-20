import math

def prob(n, p, r):
    '''
    Tinh xac suat symbol n cua nguon tin Negative Binomial voi
    p la xac suat 1 phep thu, n la so lan that bai den khi r lan thanh cong
    ---
    Parameters:
    -   n: int
        So lan that bai den khi dat dieu kien
    -   p: float
        Xac suat 1 phep thu
    -   r: int
        So lan thuc hien thanh cong
    Return:
        Xac suat symbol n
    '''
    return math.comb(n+r-1, n)*(p**r)*((1-p)**n)

def infoMeasure(n, p, r):
    '''
    Tinh luong tin cua symbol n cua nguon tin Negative Binomial voi
    p la xac suat 1 phep thu, n la so lan that bai den khi r lan thanh cong
    ---
    Parameters:
    -   n: int
        So lan that bai den khi dat dieu kien
    -   p: float
        Xac suat 1 phep thu
    -   r: int
        So lan thuc hien thanh cong
    Return:
        Luong tin cua symbol n
    '''
    return -math.log2(prob(n, p, r))

def sumProb(N, p, r):
    '''
    Tong xac suat cac symbol cho den symbol thu N
    ---
    Parameters:
    -   N: int
        So thu tu cua symbol cuoi
    -   p: float
        Xac suat cua 1 phep thu
    -   r: int
        So lan thuc hien thanh cong
    Return:
        Tong xac suat cho den symbol N
    ---
    Bien luan:
        sumProb(100, 0.6, 40) = 0.9999999999999867
        sumProb(1000, 0.6, 40) = 1
        sumProb(1000, 0.2, 60) = 1.0000000000000169
    Vay tong xac suat phan bo NegBinomial = 1
    '''
    S = 0.0
    n = N
    while n >= 0:
        S += prob(n, p, r)
        n -= 1
    return S

def approxEntropy(N, p, r):
    '''
    Luong tin trung binh cua cac symbol cho den symbol thu N
    ---
    Parameters:
    -   N: int
        So thu tu cua symbol cuoi
    -   p: float
        Xac suat cua 1 phep thu
    -   r: int
        So lan thuc hien thanh cong
    Return:
        Luong tin trung binh cua cac symbol den N
    '''
    H = 0.0
    n = N
    while n >= 0:
        H += prob(n, p, r) * infoMeasure(n, p, r)
        n -= 1
    return H
