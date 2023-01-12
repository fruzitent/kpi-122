#ifndef IO_HPP_
#define IO_HPP_

#if defined(__linux__)
    #include "src/io/linux.hpp"
#elif defined(_WIN32)
    #include "src/io/win64.hpp"
#else
    #error Unknown target
#endif

#include "src/aids/memory/unique_ptr.hpp"
#include "src/io/standard.hpp"

namespace io {
    static aids::unique_ptr<char[]> read(const char* filepath) {
        auto inp_file = aids::make_unique<std::FILE*>(std::fopen(filepath, "rb"));  // NOLINT
        if (*inp_file == nullptr) {
            throw std::runtime_error("Could not open file\n");
        }

        const std::size_t        file_size = get_filesize(filepath);
        aids::unique_ptr<char[]> buffer(new char[file_size + 1]);  // NOLINT
        const std::size_t        buffer_size = std::fread(buffer.get(), 1, file_size, *inp_file);
        if (buffer_size < file_size) {
            throw std::runtime_error("Could not read file\n");
        }

        buffer.get()[buffer_size] = '\0';
        return buffer;
    }
}  // namespace io

#endif  // IO_HPP_
