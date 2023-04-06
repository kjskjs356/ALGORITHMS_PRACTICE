#include<iostream>
 
using namespace std;

 int n, k;

int Factorial(int num){
    if(num == 0) return 1;
    int result = 1;
    for(int i=num; i>=1 ; i--){
        result *= i;
    }
    return result;
}
 
 
int main(void){

    cin >> n >> k;
    cout << Factorial(n) / (Factorial(k) * Factorial(n-k));
    return 0;    
}
