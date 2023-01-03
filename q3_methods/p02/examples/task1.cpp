#include <iostream>
#include <iomanip>
using namespace std;
double XX[] = {0.0, 2.0, 3.0, 5.0};
double YY[] = {1.0, 3.0, 2.0, 5.0};
double g, l, r;
int i, j;
int main(int argc, char *argv[])
{
    cout << "Table of values of a function:" << endl;
    cout << "X:";
    for (i = 0; i <= 3; i++)
        cout << setw(5) << XX[i] << "|";
    cout << endl;
    cout << "Y:";
    for (i = 0; i <= 3; i++)
        cout << setw(5) << YY[i] << "|";
    cout << endl;
    cout << endl;
    cout << "Enter value X: ";
    cin >> r;
    l = 0;
    for (i = 0; i <= 3; i++)
    {
        g = 1;
        for (j = 0; j <= 3; j++)
        {
            if (i != j)
                g = g * ((r - XX[j]) / (XX[i] - XX[j]));
        }
        l = l + YY[i] * g;
    }
    cout << "Y = " << l;
    return 0;
}
