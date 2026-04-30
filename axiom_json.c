#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>

// This is the function Python will call
long count_criticals(const char* filename) {
    int fd = open(filename, O_RDONLY);
    if (fd < 0) return -1;

    struct stat st;
    fstat(fd, &st);

    // Memory Map the file
    char* data = mmap(NULL, st.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
    if (data == MAP_FAILED) { close(fd); return -1; }

    long count = 0;
    char* ptr = data;
    char* end = data + st.st_size;

    // Fast scan
    while ((ptr = memmem(ptr, end - ptr, "\"CRITICAL\"", 10)) != NULL) {
        count++;
        ptr += 10;
    }

    munmap(data, st.st_size);
    close(fd);
    return count; // Return the result to Python
}