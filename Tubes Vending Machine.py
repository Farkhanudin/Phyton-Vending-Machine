print("Welcome to ITB Vending Machine")

product_1, product_1_price = "Fanta", 5000
product_2, product_2_price = "Coke", 7000
product_3, product_3_price = "Sprite", 6000
product_4, product_4_price = "Pepsi", 5000
product_5, product_5_price = "Tebs", 4000

def show() :
    print("Item:", product_1, "Price :", product_1_price)
    print("Item:", product_2, "Price :", product_2_price)
    print("Item:", product_3, "Price :", product_3_price)
    print("Item:", product_4, "Price :", product_4_price)
    print("Item:", product_5, "Price :", product_5_price)
    print("")
    return("")

show()

run = True
while run == True :
    user = input("Admin atau Buyer? ")
    if user == "Admin" :
        password = "tariksisemongko"
        try_again = True
        while try_again == True :
            attempt = input("Masukkan password Admin : ")
            if attempt != password :
                try_again2 = input("Wrong password, Would you like to try again? (yes / no) ")
                if try_again2 == "yes" :
                    continue
                elif try_again2 == "no" :
                    edit = False
                    break
            if attempt == password :
                try_again = False
                edit = True
        while edit == True :
            print("\n1. Edit Stok Produk.\n2. Edit Harga produk.\n3. Selesai ")
            choice = int(input("Masukkan pilihan Anda (angka)"))
            if choice == 1 :
                product_1 = str(input("Minuman pertama : "))
                product_2 = str(input("Minuman kedua : "))
                product_3 = str(input("Minuman ketiga : "))
                product_4 = str(input("Minuman keempat : "))
                product_5 = str(input("Minuman kelima : "))
                print("\nUpdated Stock :")
                show()
                continue

            elif choice == 2 :
                product_1_price = int(input("Harga minuman pertama : "))
                product_2_price = int(input("Harga minuman kedua : "))
                product_3_price = int(input("Harga minuman ketiga : "))
                product_4_price = int(input("Harga minuman keempat : "))
                product_5_price = int(input("Harga minuman kelima : "))
                print("\nUpdated Stock :")
                show()
                continue

            elif choice == 3 :
                print("\nUpdated Stock :")
                show()
                break

    elif user == "Buyer" :
        print("")
        show()
        jumlah_2k = int(input("Berapa jumlah uang Rp2000,00 yang ingin dimasukkan? "))
        while jumlah_2k < 0:
            jumlah_2k = int(input("Nominal tidak terdefinisi, silahkan input angka postitif"))
        jumlah_5k = int(input("Berapa jumlah uang Rp5000,00 yang ingin dimasukkan? "))
        while jumlah_5k < 0:
            jumlah_5k = int(input("Nominal tidak terdefinisi, silahkan input angka postitif"))
        jumlah_10k = int(input("Berapa jumlah uang Rp10.000,00 yang ingin dimasukkan? "))
        while jumlah_10k < 0:
            jumlah_10k = int(input("Nominal tidak terdefinisi, silahkan input angka postitif"))
        jumlah_20k = int(input("Berapa jumlah uang Rp20.000,00 yang ingin dimasukkan?"))
        while jumlah_20k < 0:
            jumlah_20k = int(input("Nominal tidak terdefinisi, silahkan input angka postitif"))

        kembalian = (((jumlah_2k * 2000) + (jumlah_5k * 5000) + (jumlah_10k * 10000) + (jumlah_20k * 20000)))

        print("\nSaldo awal Anda : Rp.", kembalian, ",00\n")
        print(show())

        product_1_bought = 0
        product_2_bought = 0
        product_3_bought = 0
        product_4_bought = 0
        product_5_bought = 0


        def bill():
            totalprice_1 = product_1_bought * product_1_price
            totalprice_2 = product_2_bought * product_2_price
            totalprice_3 = product_3_bought * product_3_price
            totalprice_4 = product_4_bought * product_4_price
            totalprice_5 = product_5_bought * product_5_price

            sum = totalprice_1 + totalprice_2 + totalprice_3 + totalprice_4 + totalprice_5

            total_product1 = (str(product_1) + " x " + str(product_1_bought))
            total_product2 = (str(product_2) + " x " + str(product_2_bought))
            total_product3 = (str(product_3) + " x " + str(product_3_bought))
            total_product4 = (str(product_4) + " x " + str(product_4_bought))
            total_product5 = (str(product_5) + " x " + str(product_5_bought))
            matriks = [[0 for i in range(2)] for j in range(6)]

            matriks[0][0] = "Jumlah produk yang dibeli"
            matriks[0][1] = "Harga"
            matriks[1][0] = total_product1
            matriks[1][1] = int(totalprice_1)
            matriks[2][0] = total_product2
            matriks[2][1] = int(totalprice_2)
            matriks[3][0] = total_product3
            matriks[3][1] = int(totalprice_3)
            matriks[4][0] = total_product4
            matriks[4][1] = int(totalprice_4)
            matriks[5][0] = total_product5
            matriks[5][1] = int(totalprice_5)

            for j in range(6):
                print(matriks[j])
            print()
            print("Total= Rp." + str(sum) + ",00.")
            return ("")


        while kembalian >= 0:
            pilihan_user = input("Silahkan pilih produk yang tersedia. Ketik 'end' jika sudah selesai\n")
            if pilihan_user == product_1 or pilihan_user == product_1.lower():
                kembalian = ((kembalian - product_1_price))
                if kembalian > 0 :
                    product_1_bought += 1
                    print("*********KELUAR " + product_1.upper() + "*************")
                    print("Uang tersisa : Rp.", kembalian, ",00")
                    print(show())
                    print("Beli lagi?")
                elif kembalian < 0 :
                    kembalian+=product_1_price
                    print("Saldo Anda tidak mencukupi.")
                    print("Uang tersisa : Rp.", kembalian, ",00")
                    print(show())
                    print("Beli lagi?")
                else :
                    product_1_bought += 1
                    print("*********KELUAR " + product_1.upper() + "*************")
                    print("Tidak ada uang tersisa di dalam mesin")
                    print("\nBill Anda : \n")
                    bill()
                    print("Thank you,Have a nice day!")
                    break

            elif pilihan_user == product_2 or pilihan_user == product_2.lower():
                kembalian = ((kembalian - product_2_price))
                if kembalian > 0 :
                    product_2_bought += 1
                    print("*********KELUAR " + product_2.upper() + "*************")
                    print("Uang tersisa : Rp.", kembalian, ",00")
                    print(show())
                    print("Beli lagi?")
                elif kembalian < 0 :
                    kembalian+=product_2_price
                    print("Saldo Anda tidak mencukupi.")
                    print("Uang tersisa : Rp.", kembalian, ",00")
                    print(show())
                    print("Beli lagi?")
                else :
                    product_2_bought += 1
                    print("*********KELUAR " + product_2.upper() + "*************")
                    print("Tidak ada uang tersisa di dalam mesin")
                    print("\nBill Anda : \n")
                    bill()
                    print("Thank you,Have a nice day!")
                    break

            elif pilihan_user == product_3 or pilihan_user == product_3.lower():
                kembalian = ((kembalian - product_3_price))
                if kembalian > 0 :
                    product_3_bought += 1
                    print("*********KELUAR " + product_3.upper() + "*************")
                    print("Uang tersisa : Rp.", kembalian, ",00")
                    print(show())
                    print("Beli lagi?")
                elif kembalian < 0 :
                    kembalian+=product_3_price
                    print("Saldo Anda tidak mencukupi.")
                    print("Uang tersisa : Rp.", kembalian, ",00")
                    print("\nBill Anda : \n")
                    print(show())
                    print("Beli lagi?")
                else :
                    product_3_bought += 1
                    print("*********KELUAR " + product_3.upper() + "*************")
                    print("Tidak ada uang tersisa di dalam mesin")
                    bill()
                    print("Thank you,Have a nice day!")
                    break


            elif pilihan_user == product_4 or pilihan_user == product_4.lower():
                kembalian = ((kembalian - product_4_price))
                if kembalian > 0 :
                    product_4_bought += 1
                    print("*********KELUAR " + product_4.upper() + "*************")
                    print("Uang tersisa : Rp.", kembalian, ",00")
                    print(show())
                    print("Beli lagi?")
                elif kembalian < 0 :
                    kembalian+=product_4_price
                    print("Saldo Anda tidak mencukupi.")
                    print("Uang tersisa : Rp.", kembalian, ",00")
                    print(show())
                    print("Beli lagi?")
                else :
                    product_4_bought += 1
                    print("*********KELUAR " + product_4.upper() + "*************")
                    print("Tidak ada uang tersisa di dalam mesin")
                    print("\nBill Anda : \n")
                    bill()
                    print("Thank you,Have a nice day!")
                    break

            elif pilihan_user == product_5 or pilihan_user == product_5.lower():
                kembalian = ((kembalian - product_5_price))
                if kembalian > 0 :
                    product_5_bought += 1
                    print("*********KELUAR " + product_5.upper() + "*************")
                    print("Uang tersisa : Rp.", kembalian, ",00")
                    print(show())
                    print("Beli lagi?")
                elif kembalian < 0 :
                    kembalian+=product_5_price
                    print("Saldo Anda tidak mencukupi.")
                    print("Uang tersisa : Rp.", kembalian, ",00")
                    print(show())
                    print("Beli lagi?")
                else :
                    product_5_bought += 1
                    print("*********KELUAR " + product_5.upper() + "*************")
                    print("Tidak ada uang tersisa di dalam mesin")
                    print("\nBill Anda : \n")
                    bill()
                    print("Thank you,Have a nice day!")
                    break

            elif pilihan_user == "end" or pilihan_user == "End":
                print("\nPembelian Anda : \n")
                bill()
                print("Kembalian= Rp." + str(kembalian) + ",00.")
                print("Thank you,Have a nice day!")
                break

            else:
                print("Terjadi kesalahan dalam transaksi Anda karena produk yang Anda masukkan tidak sesuai. ")
        run=False
    else:
        print("pilihan yang anda masukkan tidak tersedia")

