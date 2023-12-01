#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int find_calibration(const char* str, int len) {
  int found_first = 0;
  int found_last = 0;
  int result = 0;

  for (int i = 0; i < len; ++i) {
    const char *first = &str[i];
    const char *last = &str[len - i - 1];

    if (isdigit(*first) && found_first == 0) {
      found_first = 1;
      result += 10 * atoi(first);
    }
    if (isdigit(*last) && found_last == 0) {
      found_last = 1;
      result += atoi(last);
    }
  }
  return result;
}

int main() {

  const char *list[4] = {"1abc2", "pqr4stu8vwx", "a1b2c3d4e5f", "treb7uchet"};

  int total = 0;
  for (int i = 0; i < 4; ++i){
    const char *s = list[i];
    int r = find_calibration(s, strlen(s) - 1);
    total += r;
    printf("%s %d %d\n", s, r, total);
  }

  return 0;
}
