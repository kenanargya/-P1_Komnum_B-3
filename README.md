# P1_Komnum_B3

 Kelompok 3
* Ken Anargya Alkausar - 5025211168
* Faiz haq noviandra - 5025211132
* Muhammad Arkan K. D - 5025211236

## Metode Bolzano

Secara analitis, sangat mudah untuk menemukan solusi bilangan bulat dari persamaan kuadrat, baik dengan memfaktorkan atau menggunakan akar bilangan bulat dari fungsi kuadrat, juga dikenal sebagai rumus ABC. Tapi bagaimana menemukan akar bilangan bulat dari polinomial derajat lebih besar dari dua? Jelas cukup sulit untuk menemukan akarnya dengan metode analitis.

Jika metode analitik sulit dilakukan, metode numerik diperlukan. Salah satu metode numerik untuk menemukan solusi bilangan bulat dari persamaan polinomial adalah dikotomi (atau di Indonesia, metode setengah). Metode ini dapat menemukan akar dari polinomial nyata dengan derajat apa pun. Metode Bolzano adalah metode untuk menemukan akar suatu fungsi dengan menentukan batas interval di mana interval tersebut berisi nilai akar yang diinginkan. Interval tersebut kemudian dibelah dua dan kemudian diambil interval baru yang masih mengandung nilai aslinya. Pembagian ini dilakukan secara terus menerus untuk mendapatkan margin yang mendekati nilai aslinya.

![bolzano2](https://user-images.githubusercontent.com/92387421/198125864-ca22bcbd-9591-4943-b7b3-6dbc002cff74.png)

## Penjelasan Singkat

1. Pertama, kita akan mengimport library plotting dari python yaitu matplotlib dan numpy untuk menampilkan hasil grafik fungsi selama eksekusi program.
2. Kami telah membuat dua fungsi yang disebut f(x) dan midPoint. Fungsi di sini digunakan untuk menghitung hasil akhir ketika nilai x disubstitusikan ke dalam fungsi. Sedangkan fungsi midPoint digunakan untuk menghitung titik tengah (x3).
3. Selanjutnya program akan meminta user untuk memasukkan x1, x2 dan jumlah iterasi. Jika x1 lebih besar dari x2, posisinya akan ditukar.
4. Nilai koordinat x akan disimpan di xP dengan rentang x1 - x2 dengan selisih 0,1, kemudian hasil alternatif (f(x)) akan disimpan di yP sebagai koordinat y.
5. Kemudian gunakan for loop dengan sebanyak rentang iterasi seperti yang dimasukkan dalam input.
6. Masukkan nilai x1 dan x2 ke dalam fungsi f(x) untuk mendapatkan hasil fungsi kemudian untuk mencari nilai x3 masukkan dua nilai x1 dan x2 di midPoint fungsi dan masukkan nilai x3 yang diterima ke dalam fungsi fungsi untuk mencari hasil dari fungsi x3.
7. Mengoutput x1, x2, x3, f (x1), (x2), f (x3) dengan 8 angka desimal dibelakang koma.
8. Kemudian, dengan menggunakan percabangan if, periksa pergantian antara x1, x2 dan x3. Jika f(x3) positif maka x3 akan menggantikan x2 dan jika f(x3) negatif maka x3 akan menggantikan x1.
9. Setelah loop selesai, cetak nilai akhir x1 dan x2 yang merupakan rentang jawaban yang diinginkan berdasarkan jumlah iterasi.
10. Kemudian grafik akan ditampilkan
