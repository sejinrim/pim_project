import numpy as np

dtype = np.uint32
max_key = 1000
np.random.seed(1113)

# User-defined number of tuples
num_r_tuples = min(10000, max_key)
num_s_tuples = min(10000, max_key)

# Generate R and S relations
r_keys = np.random.choice(max_key, size=num_r_tuples, replace=False).astype(dtype)
r_vals = np.random.randint(0, 64, size=num_r_tuples, dtype=dtype)
R = np.stack((r_keys, r_vals), axis=1)

s_keys = np.random.choice(max_key, size=num_s_tuples, replace=False).astype(dtype)
s_vals = np.random.randint(0, 64, size=num_s_tuples, dtype=dtype)
S = np.stack((s_keys, s_vals), axis=1)

# Shuffle R and S
np.random.shuffle(R)
np.random.shuffle(S)

# Save R and S
np.save("R_relation", R)
np.save("S_relation", S)

print("R_type: "    , R.dtype)
print("S_type: "    , S.dtype)

# Perform equi-join on the key
result = []
result1 = [] #sum for the same key
s_dict = {k: v for k, v in S}
for rk, rv in R:
    if rk in s_dict:
        result.append((rk, rv, s_dict[rk]))
        result1.append((rk, rv + s_dict[rk]))
        
        
result_array = np.array(result, dtype=np.uint32).reshape(len(result), 3)
result_sum_array = np.array(result1, dtype=np.uint32).reshape(len(result1), 2)

np.save("result_tuples", result_array)
np.save("result_sum_tuples", result_sum_array)

print(f"R: {R.shape[0]} tuples, S: {S.shape[0]} tuples, Result: {result_array.shape[0]} tuples")
print(f"Total memory used: {(R.nbytes + S.nbytes + result_array.nbytes) / (1024**2):.2f} MB")

print("R relation:", R)
print("S relation:", S)
print("Result relation:", result_array)
print("Result sum relation:", result_sum_array)