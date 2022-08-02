import sys
S = sys.stdin.readline()
S = S.strip("\n")

aalphabet_count = [-1 for i in range(26)]
for i in range(26):
    aalphabet_count[i] = S.find(chr(i+97))

for i in range(26):
    print(f'{aalphabet_count[i]}',end=' ')