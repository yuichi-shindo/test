#数学系関数を管理するモジュール
__all__ = ['gcd']

#二つの数の最大公約数を返す関数
def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n