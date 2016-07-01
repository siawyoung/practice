
/*
Given a list of non negative integers, arrange them such that they form the largest number.
Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
*/

#include <string>
#include <iostream>
#include <vector> 

using namespace std;

string largestNumberArrangement(const vector<int> &A) {
    struct {
        bool operator()(string a, string b)
        {   
            string ab = a + b;
            string ba = b + a;
            if(ab > ba) return 1;
            else return 0;
        }   
    } less;
    
    int n = A.size();
    vector<string> arr;
    string res;
    for(int i: A){
        arr.push_back(to_string(i));
    }
    
    sort(arr.begin(), arr.end(), less);
    for(int i=0;i<n;i++){
        res += arr[i];
    }
    int i = 0;
    while(i<res.size()){
        if(res[i]=='0') i++;
        else break;
    }
    res.erase(res.begin(), res.begin()+i);
    return res;
}

int main(){
    int a[] = {3, 30, 34, 5, 9};
    vector<int> A(a, a+sizeof(a)/sizeof(int));
    cout << largestNumberArrangement(A) << endl;
}