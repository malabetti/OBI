#include <stdio.h>

int main(){
    int n, m, s, i = -1;

    scanf("%i", &n);
    scanf("%i", &m);
    scanf("%i", &s);

    int k, digitos;

    for(int j = n; j <= m; j++){
        k = j;
        digitos = 0;
        while(k){
            digitos += k%10;
            k = k/10;
        }
        if(digitos == s) i = j;
    }
    printf("%i", i);
    return 0;
}