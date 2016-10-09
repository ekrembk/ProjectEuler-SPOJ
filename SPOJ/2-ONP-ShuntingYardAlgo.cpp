//SHUNTING YARD ALGORITHM
#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    string oper = "+-*/^";
    const short int prec[5] = {1,1,2,2,3};
    for (int testCase = 1; testCase <= t; testCase++) {
        stack<char> st;
        string expression;
        cin >> expression;
        for (int i = 0; i < expression.length(); i++)
        {
            char token = expression[i];
            if (isalnum(token)) { //number input, print it
                cout << token;
            }
            else if (oper.find(token) != string::npos) { //operator input
                //set operator precendences
                int precToken = prec[oper.find(token)];
                int precTop = prec[oper.find(st.top())];
                if (st.empty() || st.top() == '(') {
                    st.push(token);
                }
                else if (precToken > precTop || (st.top() == '^' && token == '^')) {
                    st.push(token);
                }
                else {
                    while (precToken < precTop || (precToken == precTop && token != '^' )) {
                        cout << st.top();
                        st.pop();
                        precTop = prec[oper.find(st.top())];
                    }
                }
            }
            else { //paranthesis input
                if (token == '(') {
                    st.push(token);
                }
                else {
                    while (st.top() != '(') {
                        cout << st.top();
                        st.pop();
                    }
                    st.pop();
                }
            }
        }
        while (! st.empty()) {
            cout << st.top();
            st.pop();
        }
        cout << endl;
    }
    return 0;
}
