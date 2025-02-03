#include <stdio.h>
#include <stdlib.h>

int polynomial(int x, int *A, int size){
	int sum = 0;
	for (int i = 0; i < size; i++){
		int y = 1; 
		if (i > 0){
			for(int j = 0; j < i; j++){
				y = y*x;
			}
			*(A+i) = *(A+i) * y;
		}
		sum = sum + *(A+i);
	}
	return sum;

}

int main(){
	int A[] = {6, 2, 5, 4, 1, 3};
	printf("Enter an integer: \n");
	int point;
	scanf("%d", &point);
	int size = sizeof(A)/sizeof(A[0]);
	int eval = polynomial(point, A, size);
	printf("\n%d\n", eval);
}
