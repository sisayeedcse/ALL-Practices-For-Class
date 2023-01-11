#include <stdio.h>
int main(){
// --------- Program that prints numbers 1 to 4

// ----- a ------ without using conversion specifiers
printf("This is without conversion specifiers\n");
printf("1234");

// ----- b ------ with conversion specifers
printf("\n\nThis is with conversion specifiers\n");
printf("%d%d%d%d", 1 ,2, 3, 4);

// ------ c ------ using four PF statem.

printf("\n\nThis is using four printf statements\n");
printf("%d", 1);
printf("%d", 2);
printf("%d", 3);
printf("%d", 4);



return 0;
}
