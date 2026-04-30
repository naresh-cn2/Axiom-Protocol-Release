double fast_atof(const char* s) {
    // 1. Safety Gate: Handle empty or null strings
    if (!s || *s == '\0') return 0.0;

    double val = 0.0;
    long long int_part = 0;
    double weight = 1.0;
    int has_digit = 0;

    // 2. Integer part with Validation
    while (*s >= '0' && *s <= '9') {
        int_part = int_part * 10 + (*s - '0');
        s++;
        has_digit = 1;
    }
    
    // 3. Error Trap: If first part isn't a number and isn't a decimal, skip
    if (!has_digit && *s != '.') return -1.0; 

    val = (double)int_part;

    // 4. Fractional part with Validation
    if (*s == '.') {
        s++;
        long long frac_part = 0;
        while (*s >= '0' && *s <= '9') {
            frac_part = frac_part * 10 + (*s - '0');
            weight *= 10.0;
            s++;
        }
        val += (double)frac_part / weight; 
    }
    
    return val;
}