#-*- coding: utf-8 -*-
from time import *
from random import random 
from time import perf_counter
from tqdm import tqdm

# DROP = 10000*1000
# hits = 0.0
# for i in tqdm(range(DROP + 1)):
#     x, y = random(), random()
#     dist = pow(x**2 + y**2, 0.5)
#     if dist < 1.0:
#         hits += 1.0
# print(hits)
# f = (hits / DROP) * 4
# print("pi data: %.10f" %f)
def pi_count(bit):
    t = bit + 10
    b = 10**t
    ser_fw = 4 * b // 5
    ser_bw = b // -239
    rst_sum = ser_fw + ser_bw
    step = n * 2
    for i in tqdm(range(3, step, 2), desc="Processing"):
        ser_fw //= -25
        ser_bw //= -57121
        ser = (ser_fw + ser_bw)// i
        rst_sum += ser
    pi = rst_sum * 4
    pi //= 10**10
    return pi

dect_len = 0
try:
    file_dect = open("pi_data.txt", "r")
    file_dect.seek(0, 2)
    dect_len = file_dect.tell()
    file_dect.seek(0, 0)
    pi = file_dect.read(dect_len)
    print("file exist pi length is: {}".format(dect_len))
except FileNotFoundError as e:
    print(e) 

n = int(input('Digit calculation:'))

if n > dect_len:
    pi = pi_count(n)
    data = open("pi_data.txt", "w")
    data.write(str(pi))
    data.close()
else:
    pass
# print('pi: ', pi) 

requ_bit = int(input("data bit requeire: ")) + 1        #实际位置偏移量（加小数点）
print("required bit is: %s" %str(pi)[requ_bit-1 : requ_bit])    #字符串切片偏移量（0为起始）
print("[%d --> %d]: %s" %(requ_bit-3, requ_bit+10, str(pi)[requ_bit-3 : requ_bit+10]))
