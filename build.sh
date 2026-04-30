# Compile the C engine
gcc -O3 axiom_json.c -o axiom_json

# Run it and time it
echo "--- Axiom-JSON Performance Result ---"
time ./axiom_json