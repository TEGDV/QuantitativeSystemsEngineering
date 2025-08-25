#include <stdio.h>
#include <string.h>
#include <stdlib.h>
/*
 * Made a Hexadecimal to Decimal to Binary converter
 * the input has to be like 0x00 for HEX 0b00 for Binary
 * and 00 for decimal
 *
 * */

void d2h(int number, char hexString[]);
void reverseString(char str[]);

int main(int argc, char *argv[]) {
  char hexResult[50];
  int decimalNumber;
  
  for (int i = 1; i<argc; i++) {
    decimalNumber = atoi(argv[i]);
    if (decimalNumber == 0) {
      printf("0 -> 0x0\n");
      continue;
    }
    d2h(decimalNumber, hexResult);
    printf("%d -> 0x%s\n", decimalNumber, hexResult);
    memset(hexResult,0, sizeof(hexResult));
  }

  return 0;
}

void d2h(int number, char hexString[]) {
  int i = 0;
  while (number > 0) {
    int remainder = number % 16;
    if (remainder < 10) {
      hexString[i] = remainder + '0';
    } else {
      hexString[i] = (remainder - 10) + 'A';
    }
    number = number / 16;
    i++;
  }
  reverseString(hexString);
}

void reverseString(char str[]){
  int i = 0;
  int j = strlen(str) - 1;
  while (i < j) {
    char temp = str[i];
    str[i] = str[j];
    str[j] = temp;
    i++;
    j--;
  }
}
