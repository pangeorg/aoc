#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

void part_1() {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("/home/georg/source/aoc/2025/data/day01.txt", "r");
    if (fp == NULL) {
        printf("File not found");
        exit(EXIT_FAILURE);
    }

    int pos = 50;
    int zeros = 0;
    while ((read = getline(&line, &len, fp)) != -1) {
        char *p_end;
        long n = strtol(&line[1], &p_end, 10);
        if (line[0] == 'L') {
            long n = strtol(&line[1], &p_end, 10);
            pos = (pos - n) % 100;
        } else {
            pos = (pos + n) % 100;
        }
        if (pos == 0) {
            zeros++;
        }
    }

    fclose(fp);
    if (line)
        free(line);
    printf("%d", zeros);
    exit(EXIT_SUCCESS);
}

int modi(int a, int b) {
    return ((a % b) + b) % b;
}

int divi(int a, int b) {
    return (a - modi(a, b)) / b;
}

void next_pos(char dir, int pos, int ticks, int* zeros, int* npos) {
    if (dir == 'L'){
        int pn = pos - ticks;
        *npos = modi(pn, 100);
        if (pn <= 0) {
            *zeros = divi(abs(pn) , 100) + 1;
        }
        if (pos == 0) *zeros -= 1;
    } else {
        *npos = modi((pos + ticks), 100);
        *zeros = divi((pos + ticks), 100);
    }
}

void part_2() { 
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("/home/georg/source/aoc/2025/data/day01.txt", "r");
    if (fp == NULL) {
        printf("File not found");
        exit(EXIT_FAILURE);
    }

    int pos = 50;
    int zeros = 0;
    while ((read = getline(&line, &len, fp)) != -1) {
        char *p_end;
        long ticks = strtol(&line[1], &p_end, 10);
        int n_zeros = 0;
        int npos = pos;
        next_pos(line[0], pos, ticks, &n_zeros, &npos);
        pos = npos;
        zeros += n_zeros;
    }

    fclose(fp);
    if (line)
        free(line);
    printf("%d", zeros);
    exit(EXIT_SUCCESS);
}

int main(int argc, char** argv) {
    if (argc != 2) {
        printf("day01 <part>");
        exit(EXIT_SUCCESS);
    }  
    char *p;
    size_t n = strtol(argv[1], &p, 10);
    if (n == 1) {
        part_1();
    }
    else {
        part_2();
    }
}

