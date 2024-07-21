def sohoanhao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return n == tong

def main():
    a = int(input("Nhap so nguyen duong a: "))
    count = 0  # Biến đếm số lượng số hoàn hảo tìm được
    for i in range(1, a + 1):
        if sohoanhao(i):
            print(i)
            count += 1
    if count == 0:
        print("Khong co so hoan hao")
main()
