# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:50:03 2024

@author: Nguyễn Hoài Khánh Trang -23709171
"""
so = input("Nhập 4 số xe: ")

tong = int(so[0]) +int(so[1]) + int(so[2]) + int(so[3])
if len(str(tong)) == 2:
    tong = tong %10 + tong //10

print("Tổng số nút của xe = ",tong)