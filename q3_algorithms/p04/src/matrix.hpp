#ifndef MATRIX_HPP_
#define MATRIX_HPP_

#include <algorithm>
#include <iomanip>
#include <memory>
#include <string>  // itoa, stream, sprintf?

template<typename T>
class Array {
  protected:
    T*          _data;
    std::size_t _size;

  public:
    explicit Array(std::size_t size) {
        _data = new T[size]();
        _size = size;
    }

    ~Array() {
        delete[] _data;
    }

    T& operator[](std::size_t index) {
        if (index >= _size) {
            throw std::out_of_range("Index out of range");
        }
        return _data[index];
    }

    friend std::ostream& operator<<(std::ostream& os, Array<T>& array) {
        array.print(os);
        return os;
    }

    auto begin() {
        return _data;
    }

    auto end() {
        return _data + _size;
    }

    auto size() {
        return _size;
    }

    void fill(auto gen) {
        for (auto& value : *this) {
            value = gen();
        }
    }

    auto filter(bool (*predicate)(T)) {
        auto result   = std::make_unique<Array<T>>(_size);
        result->_size = 0;

        for (auto value : *this) {
            if (predicate(value)) {
                result->_data[result->_size++] = value;
            }
        }

        if (realloc(result->_data, result->_size * sizeof(T)) == nullptr) {
            throw std::bad_alloc();
        }

        return result;
    }

    virtual void print(std::ostream& os) {
        for (auto value : *this) {
            os << value << " ";
        }
        os << "\n";
    }

    auto reduce(auto reducer, T initial) {
        auto result = initial;
        for (auto value : *this) {
            result = reducer(result, value);
        }
        return result;
    }
};

template<typename T>
class Matrix : public Array<T> {
  private:
    std::size_t _rows;
    std::size_t _cols;

  public:
    explicit Matrix(std::size_t rows, std::size_t cols) :
        Array<T>(rows * cols) {
        _rows = rows;
        _cols = cols;
    }

    ~Matrix() = default;

    friend std::ostream& operator<<(std::ostream& os, Matrix<T>& matrix) {
        matrix.print(os);
        return os;
    }

    auto row(std::size_t index) {
        if (index >= _rows) {
            throw std::out_of_range("Row index out of range");
        }

        auto arr = std::make_unique<Array<T>>(_cols);

        for (auto i = 0; i < _cols; i++) {
            (*arr)[i] = this->_data[index * _cols + i];
        }

        return arr;
    }

    auto col(std::size_t index) {
        if (index >= _cols) {
            throw std::out_of_range("Column index out of range");
        }

        auto arr = std::make_unique<Array<T>>(_rows);

        for (auto i = 0; i < _rows; i++) {
            (*arr)[i] = this->_data[i * _cols + index];
        }

        return arr;
    }

    auto get_max_widths() {
        auto arr = std::make_unique<Array<std::size_t>>(_cols);

        for (auto i = 0; i < _cols; i++) {
            for (auto j = 0; j < _rows; j++) {
                auto value = this->_data[j * _cols + i];
                auto width = std::to_string(value).length();
                (*arr)[i]  = std::max((*arr)[i], width);
            }
        }

        return arr;
    }

    void print(std::ostream& os) {
        auto widths = get_max_widths();

        for (auto i = 0; i < _rows; i++) {
            for (auto j = 0; j < _cols; j++) {
                auto value = this->_data[i * _cols + j];
                auto width = (*widths)[j];
                os << std::setw(width) << value << " ";
            }
            os << "\n";
        }
    }
};

#endif  // MATRIX_HPP_
