#include <stdio.h>

int main(void){
    int n, s, aux = 0, total = 0;
    scanf("%i %i", &n, &s);
    int v[n], inter[100000];

    inter[0] = 1;
    for(int i = 1; i < 100000; i++) inter[i] = 0;

    for(int i = 0; i < n; i++){   
        scanf("%i", &v[i]);
        aux+=v[i];
        if(aux - s >= 0){
            total += inter[aux-s];
        }
        inter[aux]++;
    }
    printf("%i", total);
    return 0;
}