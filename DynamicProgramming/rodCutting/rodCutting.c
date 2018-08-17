#include "stdio.h"

int rodCut(int len, int *prices);

void main() {
  int len;
  printf("Enter the Length of the rod:  ");
  scanf("%d", &len);
  int prices[len + 1];
  for (int i = 0 ; i < len ; i++) {
    printf("Enter price %d piece of rod:   ", (i + 1));
    scanf("%d", &prices[i]);
  }

  int maxRevenue = rodCut(len, prices);

  printf("\n\nMax Revenue generated was:   %d\n", maxRevenue);
}

int rodCut(int len, int *prices) {
  /*int i = 0;
  while (i <= len) {
    printf("%d\n", prices[i]);
    i++;
  }
  return 1;*/
  if (len == 0) {
    return 0;
  } else {
    int maxLen = -1, temp = 0;
    for ( int i = 0; i < len; i++) {
      temp = prices[len - i - 1] + rodCut(i, prices);
      maxLen = (maxLen < temp) ? temp : maxLen;
    }
    return maxLen;
  }
}
