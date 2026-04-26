import numpy as np
import time

# Create 10 million random xG values between 0.01 and 1.0
python_xg_list = list(np.random.uniform(0.01, 1.0, 10000000))
numpy_xg_array = np.array(python_xg_list)

multiplier = 0.85

# --- SLOW PYTHON LOOP ---
start_time = time.time()
updated_python_xg = []
for xg in python_xg_list:
    updated_python_xg.append(xg * multiplier)
python_time = time.time() - start_time
print(f"Python Loop Time: {python_time:.4f} seconds")

# --- FAST NUMPY VECTORIZATION ---
start_time = time.time()

# TODO: Write the single line of code to multiply every value in numpy_xg_array by the multiplier
updated_numpy_xg = numpy_xg_array * multiplier

numpy_time = time.time() - start_time
print(f"NumPy Time: {numpy_time:.4f} seconds")