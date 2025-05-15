def chia_he_cho_5(so_nhi_phan):
    so_nhi_phan = int(so_nhi_phan,2)
    if so_nhi_phan % 5 == 0:
        return True
    else:
        return False
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân( phân tách bởi dấu phẩy): ")