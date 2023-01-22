#include <cmath>
#include <iostream>
using namespace std;
int main(int argc, char *argv[]) {
  float a, b, h, n;
  float X[100], Y[100], F[100];
  cout << " ZDR. Metod Eilera:" << endl;
  cout << " y'=sin(x)-cos(y)" << endl << endl;
  cout << " Vvedit promigok [a;b]:" << endl;
  cout << " a=";
  cin >> a;
  cout << " b=";
  cin >> b;
  cout << " Krok h=";
  cin >> h;
  cout << " Pochatkova umova: y(" << a << ")=";
  cin >> Y[0];
  X[0] = a;
  n = (b - a) / h;
  cout << endl << " Tablytsya znachenʹ:" << endl;
  for (int i = 0; i <= n; i++) {
    X[i + 1] = X[i] + h;
    Y[i + 1] = Y[i] + h * (sin(X[i]) - cos(Y[i]));
    cout << " " << X[i] << '\t' << Y[i] << endl;
  }
  return 0;
}
