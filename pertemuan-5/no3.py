keterangan = '''masukan pilihan:
1.masukan rumus luas persegi
2.masukan rumus luas lingkaran
3.masukan rumus luas segitiga'''

print(keterangan)
pilihan = input("pilihanmu")

match pilihan:
    case "no1":
        print("masukan rumus persegi")
        sisi =int(input("masukan sisi persegi"))
        luasPersegi = sisi*sisi
        print("luas persegi adalah", luasPersegi)
    case "no2":
        print("masukan rumus lingkaran")
        jari2 =float(input("masukan jari-jari"))
        luasLingkaran = 3.14 * jari2 * jari2
        print("luas lingkaran adalah", luasLingkaran)
    case "no3":
        print("masukan rumus segitiga")
        alas =int(input("masukan alas segitiga"))
        tinggi =int(input("masukan tinggi segitiga"))
        luasSegitiga = (0.5) * alas * tinggi
        print("luas segitiga adalah", luasSegitiga)
