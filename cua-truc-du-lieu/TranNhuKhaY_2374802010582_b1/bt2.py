# mã sách:
class Sach:
    def __init__(self, ma_sach, ten_sach, gia):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.gia = gia

def nhap_danh_sach_sach(n):
    sach_list = []
    for i in range(n):
        ma_sach = input(f"Nhap ma sach {i+1}: ")
        ten_sach = input(f"Nhap ten sach {i+1}: ")
        gia = int(input(f"Nhap gia sach {i+1}: "))
        sach_list.append(Sach(ma_sach, ten_sach, gia))
    return sach_list

def xuat_danh_sach_sach(sach_list):
    for sach in sach_list:
        print(f"Ma sach: {sach.ma_sach}, Ten sach: {sach.ten_sach}, Gia: {sach.gia}")

def tim_sach_tuan_tu(sach_list, ma_sach):
    for sach in sach_list:
        if sach.ma_sach == ma_sach:
            print(f"Tim thay sach co ma {ma_sach}")
            return
    print(f"Khong tim thay sach co ma {ma_sach}")

def tim_sach_nhi_phan(sach_list, ma_sach):
    sach_list.sort(key=lambda x: x.ma_sach)
    left, right = 0, len(sach_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sach_list[mid].ma_sach == ma_sach:
            print(f"Tim thay sach co ma {ma_sach}")
            return
        elif sach_list[mid].ma_sach < ma_sach:
            left = mid + 1
        else:
            right = mid - 1
    print(f"Khong tim thay sach co ma {ma_sach}")

def liet_ke_sach_gia_lon_hon(sach_list, G):
    found = False
    for sach in sach_list:
        if sach.gia > G:
            print(f"Ma sach: {sach.ma_sach}, Ten sach: {sach.ten_sach}, Gia: {sach.gia}")
            found = True
    if not found:
        print(f"Khong co sach nao co gia lon hon {G}")

def tim_sach_gia_lon_nhat(sach_list):
    max_gia = sach_list[0].gia
    max_sach = sach_list[0]
    for sach in sach_list[1:]:
        if sach.gia > max_gia:
            max_gia = sach.gia
            max_sach = sach
    print(f"Sach co gia lon nhat la: Ma sach: {max_sach.ma_sach}, Ten sach: {max_sach.ten_sach}, Gia: {max_sach.gia}")

n = int(input("Nhap so cuon sach: "))
sach_list = nhap_danh_sach_sach(n)
xuat_danh_sach_sach(sach_list)

ma_sach = input("Nhap ma sach can tim: ")
tim_sach_tuan_tu(sach_list, ma_sach)
tim_sach_nhi_phan(sach_list, ma_sach)

G = int(input("Nhap gia G: "))
liet_ke_sach_gia_lon_hon(sach_list, G)

tim_sach_gia_lon_nhat(sach_list)