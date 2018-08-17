// Recursion and Iteration

#include<stdio.h>

int climbStairsI(int stepCount);
int climbStairsR(int stepCount);

void main() {
  int stepCount, count;
  printf("Enter Step Count: ");
  scanf("%d", &stepCount);

  // Iteration
  count = climbStairsI(stepCount);
  printf("There are\"%d\" ways to climn \"%d\" stairs Iteration.\n", count, stepCount);

  // Recursion
  count = climbStairsR(stepCount);
  printf("There are %d ways to climn %d stairs. Recursion\n", count, stepCount);
}

int climbStairsR(int stepCount) {
  if (stepCount == 1) {
    return 1;
  } else if (stepCount == 2) {
    return 2;
  } else {
    return climbStairsR(stepCount - 1) + climbStairsR(stepCount - 2);
  }
}

int climbStairsI(int stepCount) {
  long int s[stepCount + 1];
  //Base cases.
  s[1] = 1;
  s[2] = 2;

  for (int i = 3; i <= stepCount; i++) {
    s[i] = s[i - 1] + s[i - 2];
  }

  return s[stepCount];

}

/*
  --> How many ways to climb n-stairs, if 1 or 2 stairs can be climbed at each step.
  Let f(n) be number of ways to climb n-steps
    - to reach nth stair there are 2 ways
      1. f(n - 2) to reach nth step.
      2. f(n - 1) to reach nth step.

      so now f(n) = f(n - 1) + f(n - 2) for recursive

      max input stepCount == 45

*/
