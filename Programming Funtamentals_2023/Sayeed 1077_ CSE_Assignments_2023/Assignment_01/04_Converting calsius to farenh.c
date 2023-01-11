#include <stdio.h>
int main(){

float celsius, fahrenheit;

  printf("Enter the temperature in Celsius: ");
  scanf("%f", &celsius);

  fahrenheit = celsius * 9 / 5 + 32;

  printf("\n%.1f degrees Celsius is equal to %.1f degrees Fahrenheit.\n", celsius, fahrenheit);


return 0;
}
