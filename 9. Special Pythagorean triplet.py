
def get_pythagorean(limit):

    # variable product untuk nemapung hasil a x b x c
    product = 0

    # variable is_true dengan nilai awal false.
    # jika variable is_true bernilai True maka
    # lakukan break karena hasil sudah didapatkan
    is_true = False

    # perulangan dari 1 sampai limit
    for a in range(1, limit):

        # perulangan dari a sampai limit - a
        # contoh: (1, 1000 - 1) -> (1, 999)
        for b in range(a, limit - a):

            # mendapatkan nilai c dari limit - a - b
            # contoh: (1000 - 1 - 1) -> (998)
            c = limit - a - b

            # jika hasil dari (a * a) + (b * b) == (c * c)
            # maka masuk ke if statement

            # contoh 1: (1 * 1) + (1 * 1) == (998 * 998)
            # ========> 1 + 1 == 996004
            # ========> 2 == 996004
            # ========> False

            # contoh 2: (200 * 200) + (375 * 375) == (425 * 425)
            # ========> 40000 + 140625 == 180625
            # ========> 180625 == 180625
            # ========> True
            if (a * a) + (b * b) == (c * c):

                # ubah nilai product berdasarkan kondisi True di atas
                product = a * b * c

                # ubah nilai is_true menjadi true
                is_true = True

                # lakukan break
                break

        # jika is_true maka lakukan break agar perulangan berhenti
        # karena hasil sudah didapatkan
        if is_true:
            break

    # return product
    return product


# simpan hasil ke dalam variable result
result = get_pythagorean(1000)

# tampilkan hasil
print(result)
