#include <iostream>
#include <stack>
#include <string>
#include <vector>

#define GET_INPUT(type, name)              \
    type name;                             \
    std::cout << "enter " << #name << ":"; \
    std::cin >> name

class ackermann_abstract {
  protected:
    ~ackermann_abstract() = default;

  public:
    std::string get_classname() {
        return typeid(*this).name();
    }

    virtual double get_value(double m, double n) = 0;
};

class ackermann_for final : public ackermann_abstract {
    double get_value(double m, double n) override {
        std::stack<double> stack {};
        stack.push(m);
        while (!stack.empty()) {
            m = stack.top();
            stack.pop();
            if (m == 0 || m == 1) {
                n = m + n + 1;
            } else if (m == 2) {
                n = 2 * n + 3;
            } else if (m == 3) {
                n = std::pow(2, n + 3) - 3;
            } else if (n == 0) {
                stack.push(--m);
                n = 1;
            } else {
                stack.push(--m);
                stack.push(++m);
                n--;
            }
        }
        return n;
    }
};

class ackermann_recursive final : public ackermann_abstract {
    double get_value(const double m, const double n) override {
        if (m == 0 || m == 1) {
            return m + n + 1;
        }
        if (m == 2) {
            return 2 * n + 3;
        }
        if (m == 3) {
            return std::pow(2, n + 3) - 3;
        }
        if (n == 0) {
            return get_value(m - 1, 1);
        }
        return get_value(m - 1, get_value(m, n - 1));
    }
};

class ackermann {
  private:
    ackermann_abstract *strategy_;

  protected:
    static void validate(const double m, const double n) {
        if (m < 0 || n < 0) {
            throw std::invalid_argument("received negative value");
        }
    }

  public:
    explicit ackermann(ackermann_abstract *strategy = nullptr) :
        strategy_(strategy) {}

    [[nodiscard]] double get_value(const double m, const double n) const {
        validate(m, n);
        return strategy_->get_value(m, n);
    }

    void set_strategy(ackermann_abstract *strategy) {
        strategy_ = strategy;
    }
};

int main() {
    const std::vector<ackermann_abstract *> ackermanns = {
        new ackermann_for,
        new ackermann_recursive,
    };

    for (int i = 0; i < ackermanns.size(); i++) {
        auto name = ackermanns[i]->get_classname();
        std::cout << i << " | " << name << "\n";
    }

    GET_INPUT(int, method);
    GET_INPUT(double, m);
    GET_INPUT(double, n);

    const auto ctx = new ackermann(ackermanns[method]);
    const auto res = ctx->get_value(m, n);
    std::cout << "res: " << res << "\n";

    return 0;
}
