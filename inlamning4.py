# # 1
# def skrivOrd(ordet):
#     for i in range(len(ordet)):
#         print(ordet)

# valtOrd = input("Write a word: ")
# skrivOrd(valtOrd)

# 2

def skrivOrd(ordet):
    for i in range(1, len(ordet) + 1):
        print(f'{i}. {ordet[i-1]}')

valtOrd = input("Write a word: ")
skrivOrd(valtOrd)