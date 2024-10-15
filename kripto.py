# Membuat matrix Playfair
def generate_key_matrix(key):
    key = key.replace("J", "I")  # Mengganti 'J' dengan 'I'
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Tanpa 'J'
    
    # Menghapus duplikat dari kunci dan menggabungkan dengan sisa alfabet
    used_chars = set()
    for char in key.upper():
        if char not in used_chars and char in alphabet:
            matrix.append(char)
            used_chars.add(char)

    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

# Mencari posisi karakter dalam matrix
def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

# Melakukan enkripsi pada digraph
def encrypt_digraph(matrix, digraph):
    row1, col1 = find_position(matrix, digraph[0])
    row2, col2 = find_position(matrix, digraph[1])

    if row1 == row2:  # Jika dalam baris yang sama
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Jika dalam kolom yang sama
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  # Membentuk persegi panjang
        return matrix[row1][col2] + matrix[row2][col1]

# Memproses plaintext menjadi digraphs
def process_plaintext(plaintext):
    plaintext = plaintext.replace(" ", "").upper().replace("J", "I")
    digraphs = []
    i = 0
    while i < len(plaintext):
        digraph = plaintext[i]
        if i + 1 < len(plaintext) and plaintext[i] != plaintext[i + 1]:
            digraph += plaintext[i + 1]
            i += 2
        else:
            digraph += 'X'  # Menambahkan 'X' jika huruf sama atau tunggal
            i += 1
        digraphs.append(digraph)
    return digraphs

# Fungsi enkripsi Playfair Cipher
def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    digraphs = process_plaintext(plaintext)
    ciphertext = ""

    for digraph in digraphs:
        ciphertext += encrypt_digraph(matrix, digraph)

    return ciphertext

# Main program
if __name__ == "__main__":
    key = "TEKNIK INFORMATIKA"
    
    plaintexts = [
        "GOOD BROOM SWEEP CLEAN",
        "REDWOOD NATIONAL STATE PARK",
        "JUNK FOOD AND HEALTH PROBLEMS"
    ]

    for plaintext in plaintexts:
        ciphertext = playfair_encrypt(plaintext, key)
        print(f"Plaintext: {plaintext}")
        print(f"Ciphertext: {ciphertext}\n")
