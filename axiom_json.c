double fast_atof(const char* s) {
    double val = 0.0;
    long long int_part = 0;
    double weight = 1.0;

    while (*s >= '0' && *s <= '9') {
        int_part = int_part * 10 + (*s - '0');
        s++;
    }
    val = (double)int_part;

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
