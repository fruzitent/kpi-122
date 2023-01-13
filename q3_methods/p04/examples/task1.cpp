#include <cmath>
#include <iostream>
using namespace std;
double f(double x) { return sqrt(0.3 * x + 1.2); }
double LeftS(double a, double b, int n) // Метод лівих прямокутників
{
  double s = 0;
  double x = a;
  double h = (b - a) / double(n);
  for (int i = 0; i < n; i++) {
    s += f(x);
    x += h;
  }
  s *= h;
  return s;
}
double RightS(double a, double b, int n) // Метод правих прямокутників
{
  double s = 0;
  double h = (b - a) / double(n);
  double x = a + h;
  for (int i = 1; i <= n; i++) {
    s += f(x);
    x += h;
  }
  s *= h;
  return s;
}
double MidelS(double a, double b, int n) // Метод середніх прямокутників
{
  double s = 0;
  double x = a;
  double h = (b - a) / double(n);
  for (int i = 0; i < n; i++) {
    s += f(x + h / 2);
    x += h;
  }
  s *= h;
  return s;
}
double SiS(double a, double b, int n) // Метод Сімпсона
{
  double s = 0;
  double s1 = 0;
  double s2 = 0;
  double h = (b - a) / double(n);
  double x = a + h;
  for (int i = 1; i < n; i += 2) {
    s1 += f(x);
    x += 2 * h;
  }
  x = a + 2 * h;
  for (int i = 2; i < n; i += 2) {
    s2 += f(x);
    x += 2 * h;
  }
  s += f(a) + f(b) + s1 * 4 + s2 * 2;
  s *= h / 3;
  return s;
}
double TrS(double a, double b, int n) // Метод трапецій
{
  double s = 0;
  double x = a;
  double h = (b - a) / double(n);
  for (int i = 1; i < n; i++) {
    x += h;
    s += f(x);
  }
  s += f(a) / 2 + f(b) / 2;
  s *= h;
  return s;
}
int main(int argc, char *argv[]) {
  double a;
  double b;
  int n;
  cout << " Integration of a function f(x)= sqrt(0.3*x+1.2) on the interval "
          "[a;b]";
  cout << endl;
  cout << " a = ";
  cin >> a;
  cout << " b = ";
  cin >> b;
  cout << " Enter the number of division segments n = ";
  cin >> n;
  cout << " With method of left-hand rectangles:";
  cout << " S = " << LeftS(a, b, n) << endl;
  cout << " With method of right-hand rectangles:";
  cout << " S = " << RightS(a, b, n) << endl;
  cout << " With mid-square method:";
  cout << " S = " << MidelS(a, b, n) << endl;
  cout << " With Simpson's method:";
  cout << " S = " << SiS(a, b, n) << endl;
  cout << " With method of trapezoids:";
  cout << " S = " << TrS(a, b, n) << endl;
  return 0;
}
