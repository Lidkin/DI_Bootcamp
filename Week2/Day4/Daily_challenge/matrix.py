matrix = [
    "7ii",
    "Tsx",
    "h%?",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]

num_rows = len(matrix)
num_cols = len(matrix[0])

decoded_message = ""

for col in range(num_cols):
    alpha_chars = []
    prev_char = ''
    for row in range(num_rows):
        char = matrix[row][col]  
        if char.isalpha():
            alpha_chars.append(char)
        else:
            if prev_char.isalpha():
                alpha_chars.append(" ")  
        prev_char = char         
 
    decoded_message += ''.join(alpha_chars)

print(decoded_message.strip())
