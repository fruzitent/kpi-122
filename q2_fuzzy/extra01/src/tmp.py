def scalar_mult(a, f):
    def g(x):
        return a * f(x)

    return g


def plot_func(func):
    dom = np.linspace(0, 100, 10000)
    y = [func(i) for i in dom]
    fig, axs = plt.subplots(1, 1)

    axs.plot(dom, y, "r:", label="f")
    axs.set_ylim([-0.1, 1.1])
    axs.legend()
    plt.savefig("out.png")
    plt.show()


def union(f, g):
    def wrapper(x):
        return max(f(x), g(x))

    return wrapper


class Larsen:
    def __init__(self, defuzzifier, op):
        self.defuzzifier = defuzzifier
        self.op = op

    def predict(self, variables, umbral_corts, rules):
        out_var_func = {}
        for i, r in enumerate(rules):
            var_name, value = r.consequent
            dom = variables[var_name].domains[value]
            f = variables[var_name].values[value]
            f = scalar_mult(umbral_corts[i], f)
            if not out_var_func.__contains__(var_name):
                out_var_func[var_name] = f, dom
            else:
                last_f, last_dom = out_var_func[var_name]
                a, b = dom
                la, lb = last_dom
                na = min(a, la)
                nb = max(b, lb)
                f = union(f, last_f)
                out_var_func[var_name] = f, (na, nb)
        defuzzi_values = {}
        for var, value in out_var_func.items():
            f, dom = value
            a, b = dom
            plot_func(f)
            defuzzi_values[var] = self.defuzzifier(f, a, b)
        return defuzzi_values
