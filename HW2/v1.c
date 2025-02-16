#include <stdio.h>
#include <stdlib.h>


int test_func(int n, int a, int b){
	if(n==0){
		return a;
	}
	n--;
	int c = a + b;
	return test_func(n, b, c);

}


int main(){
	int input;
	printf("Enter number: \n");
	scanf("%d", &input);
	int output;
	output = test_func(input, 0, 1);
	printf("output: %d\n", output);

}
