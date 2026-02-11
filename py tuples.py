if __name__ == '__main__':
    n = int(input())
    # 1. Ambil input dan langsung ubah jadi list
    # 2. Map ke integer
    # 3. Masukkan ke dalam tuple
    t = tuple(map(int, input().split()))
    
    # 4. Cetak hash-nya
    print(hash(t))
