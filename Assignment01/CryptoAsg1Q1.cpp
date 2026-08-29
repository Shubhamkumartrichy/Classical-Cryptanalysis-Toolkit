// Instructions for the Instructor:
//
// Compile:
//     g++ CryptoAsg1Q1.cpp -o freq_analyzer
//
// Run:
//     ./freq_analyzer input.txt
//
// The program accepts the input text file as a command-line argument.
// If no separate evaluation file is provided, the included sample file
// (input.txt) may be used for testing.

#include <bits/stdc++.h>
using namespace std;
//#define int long long int
#define endl '\n'

int main(int a, char* b[]) {

    char c;
    int d = 0;

    ifstream inFile(b[1]);
    
    map<char, int> m;

    while (inFile.get(c)) {

        if (c >= 'A' && c <= 'Z') {
            m[c]++;
        }else if (c >= 'a' && c <= 'z') {
            m[c - 'a' + 'A']++;  
        }            
        //my idea here is to convert the lowercase letter to uppercase by 
        //subtracting 'a' and adding 'A' to get the corresponding uppercase letter. (ASCII value operations)
        //This way, we can count both uppercase and lowercase letters together in the same map.
    }

    for (auto it : m) {
        d += it.second;
    }

    cout << "Letter" << "\t\t"<< "absolute count" << "\t\t"<< "relative frequency (%)" << endl;
    cout << "---------------------------------------------------------------"<< endl;  
    
    for (char c = 'A'; c <= 'Z'; c++) {            //not using (auto it : m) beccause it will not print the letters with 0 count
        double e = (double)m[c] * 100 / d;
        double f = ceil(e * 100.0) / 100.0;        //trying to round up to 2 decimal places
        cout << c << "\t\t"<< m[c] << "\t\t\t"<< f << endl;
    }
    
}

