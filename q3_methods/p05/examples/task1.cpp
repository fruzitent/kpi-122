#include <cmath>
#include <iostream>
using namespace std;
float F(float x) {
  float y;
  y = 3 * pow(x, 4) + 4 * pow(x, 3) - 12 * pow(x, 2) + 1;
  return y;
};
float dF(float x) {
  float y;
  y = 12 * pow(x, 3) + 12 * pow(x, 2) - 24 * x;
  return y;
};
int main(int argc, char *argv[]) {
  int p = 0;
  float a, b, x, e, i, q;
  float y1, y2, x1, x2;
  cout << "\n Rozv’jazannja nelinijnogo rivnjannja metodom Njutona: ";
  cout << "\n 3*x^4+4*x^3-12*x^2+1=0";
  cout << "\n Vvedit promigok [a;b]:";
  cout << "\n a=";
  cin >> a;
  cout << " b=";
  cin >> b;
  cout << " Vvedit pohubky e=";
  cin >> e;
  i = 0;
  if (a > b) {
    x = a;
    a = b;
    b = x;
  }
  cout << " Koreni: \n";
  for (x = a; x < b; x += e * 100) {
    y1 = F(x);
    y2 = F(x + e * 100);
    if (((y1 > 0) && (y2 < 0)) || ((y1 < 0) && (y2 > 0))) {
      i++;
      do {
        x1 = x;
        x2 = x1 - F(x1) / dF(x1);
        x1 = x2;
        q = fabs(x1 - x2);
      } while (q > e);
      cout << " x" << i << "=" << x1 << "\n";
    }
  }
  return 0;
}
