import numpy as np
import math

a = np.array([3,2])
b = np.array([1,4])

print(a + b)  #ベクトル和
print(a - b)  #ベクトル差

print(np.linalg.norm(a)) #ベクトルの大きさa
print(np.linalg.norm(b)) #ベクトルの大きさb

#ベクトルの大きさを計算する関数を作って出力するやり方
def norm(x):
    return math.sqrt(sum([i ** 2 for i in x]))

print(norm(a))
print(norm(b))
