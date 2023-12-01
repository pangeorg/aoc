#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

const char *literal_numbers[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
const int literal_numbers_value[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

int find_calibration_1(const char *str, int len)
{
  int *buffer = calloc(len, sizeof(int));
  int pos = 0;

  for (int i = 0; i < len; ++i)
  {
    const char s = str[i];
    if (isdigit(s))
    {
      buffer[pos] = atoi(&s);
      pos++;
    }
  }

  int result = buffer[0] * 10 + buffer[pos - 1];
  free(buffer);
  return result;
}

void slice(const char *str, char *result, size_t start, size_t end)
{
  strncpy(result, str + start, end - start);
}

int find_calibration_2(const char *str, int len)
{
  int *buffer = malloc(len * sizeof(int));
  char *sbuffer = malloc(len * sizeof(char));
  int pos = 0;

  for (int i = 0; i < len; ++i)
  {
    const char s = str[i];
    if (isdigit(s))
    {
      buffer[pos] = atoi(&s);
      pos++;
      continue;
    }

    for (int lni = 0; lni < 9; ++lni)
    {
      const char *num = literal_numbers[lni];
      const int val = literal_numbers_value[lni];
      int slen = strlen(num);

      if (i + slen < len + 1)
      {
        memset(sbuffer, 0, len);
        slice(str, sbuffer, i, i + slen);
        if (strcmp(sbuffer, num) == 0)
        {
          buffer[pos] = val;
          pos++;
        }
      }
    }
  }

  int result = buffer[0] * 10 + buffer[pos - 1];
  free(buffer);
  free(sbuffer);
  return result;
}

int main()
{
  int total = 0;

  printf("\n#### CALIBRATION 1 #####\n");
  const char *list1[4] = {
    "1abc2",
    "pqr4stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
  };

  for (int i = 0; i < 4; ++i)
  {
    const char *s = list1[i];
    int r = find_calibration_1(s, strlen(s));
    total += r;
    printf("%s %d %d\n", s, r, total);
  }

  printf("\n#### CALIBRATION 2 #####\n");
  const char *list2[7] = {
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
  };

  total = 0;
  for (int i = 0; i < 7; ++i)
  {
    const char *s = list2[i];
    int r = find_calibration_2(s, strlen(s));
    total += r;
    printf("%s %d %d\n", s, r, total);
  }
  return 0;
}
