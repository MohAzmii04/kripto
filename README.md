Untuk melakukan enkripsi menggunakan Playfair Cipher dengan kunci "TEKNIK INFORMATIKA," kita akan mengikuti langkah-langkah berikut:

### Langkah 1: Membuat Kunci Matrix 5x5
Playfair Cipher menggunakan matrix 5x5 dengan huruf-huruf alfabet. Huruf-huruf dalam kunci dimasukkan terlebih dahulu, kemudian sisanya diisi dengan huruf yang belum ada. Huruf "I" dan "J" diperlakukan sebagai huruf yang sama.

#### Kunci: TEKNIK INFORMATIKA
Setelah membuang huruf yang berulang dan menggabungkan "I" dan "J":
- Kunci yang digunakan: **TEKNIKOFARM**

Matrix kunci akan terlihat seperti ini:

```
T E K N I
K O F A M
B C D G H
L P Q R S
U V W X Y
```

### Langkah 2: Memproses Plaintext
1. Hilangkan spasi dari plaintext.
2. Bagi huruf menjadi pasangan (digraphs). Jika ada dua huruf yang sama dalam satu pasangan, tambahkan "X" di antaranya. Jika jumlah huruf ganjil, tambahkan "X" di akhir.

#### Plaintext 1: "GOOD BROOM SWEEP CLEAN"
- Setelah dihilangkan spasi dan diubah menjadi digraphs: `GO OD BR OM SW EE PC LE AN`
  
Plaintext 2: "REDWOOD NATIONAL STATE PARK"
- Digraphs: `RE DW OD NA TI ON AL ST AT EP AR KX` (menambahkan X karena huruf ganjil)

Plaintext 3: "JUNK FOOD AND HEALTH PROBLEMS"
- Digraphs: `JU NK FO OD AN DH EA LT HP RO BL EM SX` (menambahkan X di akhir)

### Langkah 3: Enkripsi Setiap Digraph
- Jika kedua huruf berada dalam baris yang sama, geser ke kanan satu posisi (dengan wrap-around).
- Jika kedua huruf berada dalam kolom yang sama, geser ke bawah satu posisi (dengan wrap-around).
- Jika kedua huruf tidak dalam baris atau kolom yang sama, tukar mereka di posisi sudut persegi panjang yang mereka bentuk.

#### Enkripsi Digraph dari Plaintext 1: "GOOD BROOM SWEEP CLEAN"
- GO → FP
- OD → KA
- BR → LC
- OM → AF
- SW → YX
- EE → II (karena satu baris, geser ke kanan)
- PC → LB
- LE → PT
- AN → TI

Ciphertext: **FPKALCAFYXIILBPTTI**

#### Enkripsi Digraph dari Plaintext 2: "REDWOOD NATIONAL STATE PARK"
- RE → PL
- DW → VQ
- OD → KA
- NA → IT
- TI → IR
- ON → NG
- AL → LT
- ST → HY
- AT → IT
- EP → LP
- AR → LT
- KX → MU

Ciphertext: **PLVQKAITIRNGLTHYITLPLTMU**

#### Enkripsi Digraph dari Plaintext 3: "JUNK FOOD AND HEALTH PROBLEMS"
- JU → QV
- NK → QA
- FO → FM
- OD → KA
- AN → TI
- DH → GH
- EA → PO
- LT → HY
- HP → LB
- RO → NG
- BL → LT
- EM → AF
- SX → YU

Ciphertext: **QVQA FMKATIGHYPLBLTNG LTAFYU**

Jadi, hasil enkripsi dari ketiga plaintext dengan Playfair Cipher dan kunci "TEKNIK INFORMATIKA" adalah:

1. **FPKALCAFYXIILBPTTI**
2. **PLVQKAITIRNGLTHYITLPLTMU**
3. **QVQAFMKATIGHYPLBLTNG LTAFYU**

   ![Cuplikan layar 2024-10-15 085737](https://github.com/user-attachments/assets/e73cdd4d-e22e-4eec-bc86-89f0c236d78d)

