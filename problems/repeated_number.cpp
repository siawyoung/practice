/*
given a read only array of n integers. Find out if any integer occurs 
more than n/3 times in the array in linear time and constant additional 
space.
If so, return the integer. If not, return -1. If there are multiple 
solutions, return any one.
*/


#include <vector>
#include <iostream>
using namespace std;

int repeatedNumber(const vector<int> &A) {
    if(A.size() == 0) return -1;
    pair<int, int> e1(0, 0);
    pair<int, int> e2(0, 0); 
    int n = A.size();
    for(int i=0;i<n;i++){
        if(A[i]==e1.first) {e1.second ++;}
        else if(A[i]==e2.first) {e2.second ++;}
        else{
            if(e1.second==0) {e1.first = A[i]; e1.second = 1; }
            if(e2.second==0) {e2.first = A[i]; e2.second = 1; }
            e1.second --;
            e2.second --;
        }
    }
    int c1 = 0, c2 = 0;
    for(int i=0;i<n;i++){
        if(A[i]==e1.first) c1 ++;
        if(A[i]==e2.first) c2 ++;
    }
    if(c1 > n/3) return e1.first;
    if(c2 > n/3) return e2.first;
    return -1;
}

int main(){
    cout << "hello" << endl;

    int a[] = {1000441, 1000441, 1000994};
    vector<int> A(a, a+sizeof(a)/sizeof(int));
    cout << repeatedNumber(A) << endl; //1000441

    int b[] = {1, 1, 1, 2, 2, 3, 3, 3, 3}; 
    vector<int> B(b, b+sizeof(b)/sizeof(int));
    cout << repeatedNumber(B) << endl; //3

    int c[] = {0, 0, 0, 1, 1, 1, 2, 2, 2, 3};
    vector<int> C(c, c+sizeof(c)/sizeof(int));
    cout << repeatedNumber(C) << endl; //-1

}