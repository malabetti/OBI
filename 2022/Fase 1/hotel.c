#include <stdio.h>

int main(){
    int d, a, n;
    scanf("%i", &d);
    scanf("%i", &a);
    scanf("%i", &n);

    int valor = 0;

    if(n < 16)
        if(n == 1)
            valor = 31 * d;
        else
            valor = (32 - n) * (d + ((n-1) * a));
    else
        valor = (32 - n) * (d + (14 * a));

    printf("%i", valor);
    return 0;
}