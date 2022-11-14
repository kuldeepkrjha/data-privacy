import math

def openFile(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    string_line = []
    for line in lines:
        lst = list(line.strip('\n'))
        for l in lst:
            string_line.append(l)
    file.close()
    return string_line

def writeFile(filename, lines):
    f = open(filename, 'w')
    for line in lines:
        f.write("".join(line))
        f.write("\n")
    f.close()
    #print("done")

def encrypt(lines, col, enc=True):
    if enc:
        rows = int(math.ceil(len(lines) / col))
    else:
        rows = col
        col = int(math.ceil(len(lines) / col))
    encrypted_lines = []
    index = 0
    # convert to matrix form
    for i in range(rows):
        temp_row = []
        for count in range(col):
            try:
                temp_row.append(lines[index])
                index += 1
            except:
                temp_row.append('$')
                index += 1
        # print(temp_row)
        encrypted_lines.append(temp_row)
    result = []
    for i in range(len(encrypted_lines[0])):
        temp_res = []
        for j in range(len(encrypted_lines)):
            try:
                temp_res.append(encrypted_lines[j][i])
            except:
                continue
        if len(temp_res) != 0:
            result.append(temp_res)
    return result

def printResult(lines):
    for line in lines:
        print(line)

def main():
    print("\n1. Encrypt\n2. Decrypt")
    ch = int(input(">> "))
    filename = input("\nFile to read: ")
    cols = int(input("Key (column size): "))
    out_filename = input("File to write: ")
    lines = openFile(filename)
    if ch == 1:
        enc_lines = encrypt(lines, cols, enc=True)
    if ch == 2:
        enc_lines = encrypt(lines, cols, enc=False)
    printResult(enc_lines)
    writeFile(out_filename, enc_lines)

if __name__ == '__main__':
    main()
