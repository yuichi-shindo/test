#アルゴリズム系を管理するモジュール

__all__ = ['parSum']

#部分和関数,ansに一致するものの組み合わせを選んだものを２進数に変換し、全てリストに格納して返す
def parSum(ans,lst):
    result = []
    for i in range(2**len(lst)):
        sum_lst = sum(ai for idx, ai in enumerate(lst) if i & (1 << idx))
        if sum_lst == ans:
            result.append(format(i,'b'))    
    return result
