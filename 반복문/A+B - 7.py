import sys

repeat = int(sys.stdin.readline()) # 반복

data_out = list(range(repeat))

# map()은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수입니다.
# data = np.array([sys.stdin.readline().split()  for i in range(repeat)])
# data = data.astype(int)

data = [sys.stdin.readline().split()  for i in range(repeat)]

for i in range(repeat):
    data_out[i] = int(data[i][0]) + int(data[i][1])
    print(f'Case #{i+1}: {data_out[i]}')
