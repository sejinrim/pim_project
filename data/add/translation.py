import numpy as np

# npy 파일 로드
data = np.load('resadd_input1_64.npy')

# txt로 저장
# np.savetxt('your_file.txt', data, fmt='%d')  # 정수형 데이터의 경우
np.savetxt('input1.txt', data, fmt='%.6f')  # 실수형 데이터의 경우

print("변환 완료!")