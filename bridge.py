import ctypes
import time

# 1. Connect to the C-Engine
lib = ctypes.CDLL('./libaxiom.so')

# 2. Tell Python: "The C-Engine expects a string and returns a long number"
lib.count_criticals.argtypes = [ctypes.c_char_p]
lib.count_criticals.restype = ctypes.c_long

# 3. Use it!
print("🚀 Starting High-Speed Axiom Scan...")
start_time = time.perf_counter()

# We send the filename to the C-Engine
result = lib.count_criticals(b"monster_logs.json")

end_time = time.perf_counter()

print(f"✅ Found {result} CRITICAL entries")
print(f"⏱️ Time Taken: {end_time - start_time:.4f} seconds")