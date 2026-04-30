import time

# Start the clock
start = time.time()

count = 0
with open("data.txt", "rb") as f:
    for line in f:
        count += 1

end = time.time()

print(f"Total Lines: {count}")
print(f"Time taken: {end - start:.4f} seconds")
