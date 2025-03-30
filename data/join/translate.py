import numpy as np

# npy 파일 로드
R = np.load('R_relation.npy')
S = np.load('S_relation.npy')
result = np.load('result_tuples.npy')
result_sum = np.load('result_sum_tuples.npy')

# txt로 저장
np.savetxt('R.txt', R, fmt='%d')
np.savetxt('S.txt', S, fmt='%d')
np.savetxt('result.txt', result, fmt='%d')
np.savetxt('result_sum.txt', result_sum, fmt='%d')

print("변환 완료!")