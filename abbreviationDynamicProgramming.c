#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();

// Complete the abbreviation function below.

// Please either make the string static or allocate on the heap. For example,
// static char str[] = "hello world";
// return str;
//
// OR
//
// char* str = "hello world";
// return str;
//
int max (int a, int b)
{
    return (a>b)?a:b;
}
char* abbreviation(char* a, char* b) {
    int aSize = strlen(a);
    int bSize = strlen(b);
    int i=0, j=0, num=0; // num is total elements that are equal or can  be capitalized
    printf("aSize is %d and bSize is %d\n", aSize, bSize);
    for(int k=0;k<aSize;k++)
        printf("%c\n", a[k]);
    if(aSize<bSize)
        return "NO";
    else {
        while(j<aSize) // j iterates on a and i iterates on b 
        {
            if(a[j]==b[i])
            {
                i++; j++; num++;
            }
            else if((int)a[j] == (int)b[i] + 32)
            {
                i++; j++; num++;
            }
            else if((int)a[j] <=90){
                return "NO";
            }
            else {
                j++;
            }
        }
        printf("num is %d\n", num);
        if(num == bSize)
            return "YES";
        else
            return "NO";
    }
}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    char* q_endptr;
    char* q_str = readline();
    int q = strtol(q_str, &q_endptr, 10);

    if (q_endptr == q_str || *q_endptr != '\0') { exit(EXIT_FAILURE); }

    for (int q_itr = 0; q_itr < q; q_itr++) {
        char* a = readline();

        char* b = readline();

        char* result = abbreviation(a, b);

        fprintf(fptr, "%s\n", result);
    }

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}
