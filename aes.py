# -------------------------------
# S-BOX (use generated or fixed)
# -------------------------------
def generate_sbox():
    sbox = [0]*256

    def gf_mul(a, b):
        p = 0
        for _ in range(8):
            if b & 1:
                p ^= a
            hi = a & 0x80
            a = (a << 1) & 0xFF
            if hi:
                a ^= 0x1B
            b >>= 1
        return p

    def inv(x):
        if x == 0:
            return 0
        for i in range(1,256):
            if gf_mul(x,i) == 1:
                return i

    for i in range(256):
        x = inv(i)
        y = x
        for _ in range(4):
            y = ((y << 1) | (y >> 7)) & 0xFF
            x ^= y
        sbox[i] = x ^ 0x63

    return sbox

SBOX = generate_sbox()

# -------------------------------
# Convert text to state matrix
# -------------------------------
def text_to_matrix(text):
    return [[ord(text[i*4+j]) for j in range(4)] for i in range(4)]

def print_state(state, title):
    print(title)
    for row in state:
        print([hex(x) for x in row])
    print()

# -------------------------------
# SubBytes
# -------------------------------
def sub_bytes(state):
    return [[SBOX[val] for val in row] for row in state]

# -------------------------------
# ShiftRows
# -------------------------------
def shift_rows(state):
    return [
        state[0],
        state[1][1:] + state[1][:1],
        state[2][2:] + state[2][:2],
        state[3][3:] + state[3][:3]
    ]

# -------------------------------
# MixColumns
# -------------------------------
def gmul(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi = a & 0x80
        a = (a << 1) & 0xFF
        if hi:
            a ^= 0x1B
        b >>= 1
    return p

def mix_columns(state):
    new = []
    for col in range(4):
        a = [state[row][col] for row in range(4)]

        new.append([
            gmul(a[0],2) ^ gmul(a[1],3) ^ a[2] ^ a[3],
            a[0] ^ gmul(a[1],2) ^ gmul(a[2],3) ^ a[3],
            a[0] ^ a[1] ^ gmul(a[2],2) ^ gmul(a[3],3),
            gmul(a[0],3) ^ a[1] ^ a[2] ^ gmul(a[3],2)
        ])

    # transpose back
    return [[new[j][i] for j in range(4)] for i in range(4)]

# -------------------------------
# AddRoundKey
# -------------------------------
def add_round_key(state, key):
    return [[state[i][j] ^ key[i][j] for j in range(4)] for i in range(4)]

# -------------------------------
# MAIN
# -------------------------------
plaintext = "CONFIDENTIAL123"  # 16 chars
key = "ABCDEFGHIJKLMNOP"      # 16 chars

state = text_to_matrix(plaintext)
key_state = text_to_matrix(key)

print_state(state, "Initial State:")

# Round Steps
state = sub_bytes(state)
print_state(state, "After SubBytes:")

state = shift_rows(state)
print_state(state, "After ShiftRows:")

state = mix_columns(state)
print_state(state, "After MixColumns:")

state = add_round_key(state, key_state)
print_state(state, "After AddRoundKey (Final State):")
