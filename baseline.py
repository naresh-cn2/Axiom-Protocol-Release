import json, time, os, psutil
def test_python(filename):
    print(f"🧪 Starting Standard Python Baseline...")
    proc = psutil.Process(os.getpid())
    start_mem = proc.memory_info().rss / 1e6
    start_time = time.perf_counter()
    
    with open(filename, 'r') as f:
        data = json.load(f) # Standard Python Parser
        
    end_time = time.perf_counter()
    end_mem = proc.memory_info().rss / 1e6
    print(f"⏱️ Time Taken: {end_time - start_time:.2f}s")
    print(f"📈 RAM Bloat: {end_mem - start_mem:.2f} MB")

if __name__ == "__main__":
    if os.path.exists("monster_logs.json"):
        test_python("monster_logs.json")
    else:
        print("❌ Error: File not found. Run generator.py first.")