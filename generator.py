import json, random, string, os
def generate_monster_json(filename, target_size_mb):
    print(f"🚀 Generating {target_size_mb}MB of Monster JSON logs...")
    target_bytes = target_size_mb * 1024 * 1024
    current_bytes = 0
    with open(filename, 'w') as f:
        f.write('[\n')
        while current_bytes < target_bytes:
            log = {"id": "".join(random.choices(string.ascii_letters, k=16)),
                   "level": random.choice(["INFO", "ERROR", "CRITICAL"]),
                   "payload": {"data": "x" * 100, "user_id": random.randint(1,1000)}}
            s = json.dumps(log) + ",\n"
            f.write(s)
            current_bytes += len(s)
        f.write('{"end": true}\n]')
    print(f"✅ Done: {os.path.getsize(filename)/1e6:.2f} MB")

if __name__ == "__main__":
    generate_monster_json("monster_logs.json", 500)