# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:34:30 2024

@author: Nguyễn Hoài Khánh Trang - 23709171
"""

can_nang= float(input("Nhập cân nặng (kg): "))
chieu_cao= float(input("Nhập chiều cao (m): "))

BMI =  can_nang/(chieu_cao**2)

if BMI < 16:
    print("Tình trạng sức khỏe: Gầy độ III")
elif 16 <= BMI < 17 :
    print("Tình trạng sức khỏe: Gầy độ II")
elif 17 <= BMI < 18.5:
    print("Tình trạng sức khỏe: Gầy độ I")
elif 18.5 < BMI < 25:
    print("Tình trạng sức khỏe: Bình thường")
elif 25 <= BMI < 30:
    print("Tình trạng sức khỏe: Thừa cân")
elif 30 <= BMI < 35:
    print("Tình trạng sức khỏe: Béo phì độ I")
elif 35 <= BMI < 40:
    print("Tình trạng sức khỏe: Béo phì độ II")
else:
    print("Tình trạng sức khỏe: Béo phì độ III")

print("BMI = ", round(BMI,3))
