#include <stdio.h>
#include <stdlib.h>

int polynomial(int x, int *A, int size, int count, int sum){
	if(size-2 == count){
		return A[size-2] + x*A[size-1];
	}
	else{
		return A[count] + x*polynomial(x, A, size, ++count, sum);
	}
}

int main(){
	int A[] = {6, 2, 5, 4, 1, 3};
	int point;
	printf("Enter an integer: \n");
	scanf("%d", &point);
	int sum = 0;
	int count = 0;
	int size = sizeof(A)/sizeof(A[0]);
        int eval = polynomial(point, A, size, count, sum);
	printf("\n%d\n", eval);
}
