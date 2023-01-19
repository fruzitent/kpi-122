#include <iostream>
#include <random>

namespace aids {
    template<typename T>
    struct remove_reference {
        using type = T;
    };

    template<typename T>
    struct remove_reference<T&> {
        using type = T;
    };

    template<typename T>
    struct remove_reference<T&&> {
        using type = T;
    };

    template<typename T>
    using remove_reference_t = typename aids::remove_reference<T>::type;

    template<typename Iterator, typename Generator>
    static constexpr void generate(Iterator first, Iterator last, Generator gen) {
        for (; first != last; ++first) {
            *first = gen();
        }
    }

    template<typename T>
    static constexpr aids::remove_reference_t<T>&& move(T&& arg) noexcept {
        return static_cast<aids::remove_reference_t<T>&&>(arg);
    }

    template<typename T>
    static constexpr void swap(T& lhs, T& rhs) {
        T temp = aids::move(lhs);
        lhs    = aids::move(rhs);
        rhs    = aids::move(temp);
    }

    template<typename Iterator>
    static constexpr void reverse(Iterator first, Iterator last) {
        while (first != last && first != --last) {
            aids::swap(*first++, *last);
        }
    }
}  // namespace aids

template<typename Iterator>
static constexpr void cocktail_sort(Iterator first, Iterator last) {
    bool swapped = true;

    while (first != last-- && swapped) {
        for (Iterator i = first; i != last; ++i) {
            if (*i > *(i + 1)) {
                aids::swap(*i, *(i + 1));
                swapped = true;
            }
        }

        if (!swapped) {
            break;
        }
        swapped = false;

        for (Iterator i = last; i != first; --i) {
            if (*i < *(i - 1)) {
                aids::swap(*i, *(i - 1));
                swapped = true;
            }
        }

        ++first;
    }
}

static constexpr void print(auto* array, std::size_t size) {
    for (std::size_t i = 0; i < size; ++i) {
        std::cout << array[i] << " ";
    }
    std::cout << "\n";
}

int main() try {
    static constexpr int rng_min = 0;
    static constexpr int rng_max = 50;

    std::random_device                 seed;
    std::mt19937                       gen(seed());
    std::uniform_int_distribution<int> dist(rng_min, rng_max);

    auto rng = [&dist, &gen]() {
        return dist(gen);
    };

    static constexpr std::size_t array_size = 50;
    static constexpr std::size_t view_size  = array_size / 2;

    int* array = new int[array_size];
    aids::generate(array, array + array_size, rng);
    print(array, array_size);

    int* view = new int[view_size];
    for (std::size_t i = 0; i < view_size; ++i) {
        view[i] = array[i * 2 + 1];
    }

    cocktail_sort(view, view + view_size);
    aids::reverse(view, view + view_size);
    for (std::size_t i = 0; i < view_size; ++i) {
        array[i * 2 + 1] = view[i];
    }

    print(array, array_size);
    delete[] array;
    delete[] view;

    return 0;
} catch (const std::exception& error) {
    std::cerr << "ERROR: " << error.what();
    return 1;
}
