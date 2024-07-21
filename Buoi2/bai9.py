def bits_needed(a):
    if a < 0:
        a = -a
    bit_count = 0
    while a > 0:
        bit_count += 1
        a = a >> 1  # Dịch phải số a để kiểm tra bit tiếp theo
    return bit_count

# Ví dụ
a = int(input("Nhap so a:"))
print(f"Số lượng bits cần thiết để biểu diễn số {a} ở dạng nhị phân là: {bits_needed(a)}")


x = "awesome"


print("Python is " + x)


print(f"Python is {x}")


print("Python is {}".format(x))
