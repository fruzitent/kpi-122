#include <iostream>
#include <string>
#include <vector>

#define GET_INPUT(type, name)              \
    type name;                             \
    std::cout << "enter " << #name << ":"; \
    std::cin >> name

class gcd_abstract {
  protected:
    ~gcd_abstract() = default;

  public:
    std::string get_classname() {
        return typeid(*this).name();
    }

    virtual int get_value(int a, int b) = 0;
};

class gcd_do final : public gcd_abstract {
    // TODO(p10): add "do {} while ()" implementation
    int get_value(int a, int b) override {
        return -1;
    }
};

class gcd_for final : public gcd_abstract {
    int get_value(const int a, const int b) override {
        int gcd = -1;
        for (int i = 1; i <= a && i <= b; i++) {
            if (a % i == 0 && b % i == 0) {
                gcd = i;
            }
        }
        return gcd;
    }
};

class gcd_recursive final : public gcd_abstract {
    int get_value(const int a, const int b) override {
        return (b == 0) ? a : get_value(b, a % b);
    }
};

class gcd_while final : public gcd_abstract {
    int get_value(int a, int b) override {
        while (b != 0) {
            const auto tmp = a % b;
            a              = b;
            b              = tmp;
        }
        return a;
    }
};

class gcd {
  private:
    gcd_abstract *strategy_;

  public:
    explicit gcd(gcd_abstract *strategy = nullptr) :
        strategy_(strategy) {}

    [[nodiscard]] int get_value(const int a, const int b) const {
        return strategy_->get_value(a, b);
    }

    void set_strategy(gcd_abstract *strategy) {
        strategy_ = strategy;
    }
};

int main() {
    const std::vector<gcd_abstract *> gcds = {
        new gcd_do,
        new gcd_for,
        new gcd_recursive,
        new gcd_while,
    };

    for (int i = 0; i < gcds.size(); i++) {
        auto name = gcds[i]->get_classname();
        std::cout << i << " | " << name << "\n";
    }

    GET_INPUT(int, method);
    GET_INPUT(int, a);
    GET_INPUT(int, b);

    const auto ctx = new gcd(gcds[method]);
    const auto gcd = ctx->get_value(a, b);
    std::cout << "GCD: " << gcd << "\n";

    return 0;
}
