#include <stdio.h>
int main(){

float radius, diameter, circumference, area;
const float PI = 3.14159;

  printf("Enter the radius of the circle: ");
  scanf("%f", &radius);

  diameter = 2 * radius;
  circumference = 2 * PI * radius;
  area = PI * radius * radius;

  printf("Diameter: %.2f \n Circumference: %.2f \n Area: %.2f", diameter, circumference, area);


return 0;
}
