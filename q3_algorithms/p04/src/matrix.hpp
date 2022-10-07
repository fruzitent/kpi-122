#ifndef MATRIX_HPP_
#define MATRIX_HPP_

#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string>  // sprintf, itoa, streams?

bool TRUE() {
    return true;
}

template<typename T>
auto product(T* arr, std::size_t size, bool (*predicate)(T value) = TRUE) {
    struct {
        std::string view;
        std::size_t value = 1;
    } result;

    for (T i = 0; i < size; i++) {
        auto value = arr[i];
        if (predicate(value)) {
            result.view += std::to_string(value) + " * ";
            result.value *= value;
        }
    }

    if (!result.view.empty()) {
        result.view.pop_back();
        result.view.pop_back();
        result.view += "= " + std::to_string(result.value);
    }

    delete[] arr;
    return result;
}

template<typename T>
class Matrix {
  private:
    std::size_t _rows {};
    std::size_t _cols {};
    T*          _data;

  public:
    Matrix(std::size_t rows, std::size_t cols) {
        _rows = rows;
        _cols = cols;
        _data = new T[_rows * _cols] {};
    }

    ~Matrix() {
        delete[] _data;
    }

    friend std::ostream& operator<<(std::ostream& os, Matrix<T>& matrix) {
        matrix.print(os);
        return os;
    }

    T* operator[](std::size_t index) {
        return &_data[index];
    }

    std::size_t rows() {
        return _rows;
    }

    std::size_t cols() {
        return _cols;
    }

    std::size_t items() {
        return _rows * _cols;
    }

    T* get_row(std::size_t index) {
        if (index >= _rows) {
            throw std::out_of_range("Row index out of range");
        }

        T* arr = new T[_cols] {};

        for (std::size_t i = 0; i < _cols; i++) {
            arr[i] = _data[index * _cols + i];
        }

        return arr;
    }

    T* get_col(std::size_t index) {
        if (index >= _cols) {
            throw std::out_of_range("Column index out of range");
        }

        T* arr = new T[_rows] {};

        for (auto i = 0; i < _rows; i++) {
            arr[i] = _data[i * _cols + index];
        }

        return arr;
    }

    std::size_t* get_max_widths() {
        auto* widths = new std::size_t[_cols] {};

        for (auto i = 0; i < _cols; i++) {
            for (auto j = 0; j < _rows; j++) {
                auto value  = _data[j * _cols + i];
                auto length = std::to_string(value).length();
                widths[i]   = std::max(widths[i], length);
            }
        }

        return widths;
    }

    void print(std::ostream& os) {
        auto* widths = get_max_widths();

        for (auto i = 0; i < _rows; i++) {
            for (auto j = 0; j < _cols; j++) {
                auto pad   = widths[j];
                auto value = _data[i * _cols + j];
                os << std::setw(pad) << value << " ";
            }
            os << "\n";
        }

        delete[] widths;
    }

    void fill(auto gen) {
        for (auto i = 0; i < items(); i++) {
            _data[i] = gen();
        }
    }

    auto row_product(std::size_t index, bool (*predicate)(T value) = TRUE) {
        return product(get_row(index), _cols, predicate);
    }

    auto col_product(std::size_t index, bool (*predicate)(T value) = TRUE) {
        return product(get_col(index), _rows, predicate);
    }
};

#endif  // MATRIX_HPP_
