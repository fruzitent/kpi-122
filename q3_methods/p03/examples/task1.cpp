#include <iostream>
using namespace std;
const int n = 6;
double X[] = {0.0, 0.1, 0.2, 0.3, 0.4, 0.5};
double Y[] = {1.2733, 1.8007, 2.3606, 2.9577, 3.5969, 4.2833};
double y1[n];
double y2[n];
double y3[n];
double y4[n];
double y5[n];
double xx, t, G, L, h;
int k, i, j;
int main(int argc, char *argv[])
{
    cout << "Table of values of a function:" << endl;
    cout << "\tX"
         << "\t|"
         << "\tY" << endl;
    cout << "  ---------------------------" << endl;
    for (i = 0; i < n; i++)
        cout << "\t" << X[i] << "\t|"
             << "\t" << Y[i] << endl;
    cout << endl;
    cout << "Enter  value X: ";
    cin >> xx;
    h = 0;
    i = 1;
    t = 0;
    k = 0;
    h = (X[i] - X[i - 1]);
    t = (xx - X[i - 1]) / h;
    for (j = 1; j < n; j++)
    {
        y1[k] = Y[j] - Y[j - 1];
        k++;
    }
    k = 0;
    for (j = 1; j < n - 1; j++)
    {
        y2[k] = y1[j] - y1[j - 1];
        k++;
    }
    k = 0;
    for (j = 1; j < n - 2; j++)
    {
        y3[k] = y2[j] - y2[j - 1];
        k++;
    }
    k = 0;
    for (j = 1; j < n - 3; j++)
    {
        y4[k] = y3[j] - y3[j - 1];
        k++;
    }
    k = 0;
    for (j = 1; j < n - 4; j++)
    {
        y5[k] = y4[j] - y4[j - 1];
        k++;
    }
    G = (y1[0] + y2[0] * (2 * t - 1) / 2 + y3[0] * (3 * t * t - 6 * t + 2) / 6 + y4[0] * (4 * t * t * t - 18 * t * t + 22 * t - 6) / 24 + y5[0] * (5 * t * t * t * t - 40 * t * t * t + 105 * t * t - 100 * t + 24) / 120) / h;
    cout << "Y' = " << G << endl;
    L = (y2[0] + y3[0] * (t - 1) + y4[0] * (12 * t * t - 36 * t + 22) / 24 + y5[0] * (20 * t * t * t - 120 * t * t + 210 * t - 100) / 120) / (h * h);
    cout << "Y\" = " << L;
    return 0;
}
