#ifndef IO_WIN64_HPP_
#define IO_WIN64_HPP_

#include <Windows.h>

#include <stdexcept>

namespace io {
    static std::size_t get_filesize(const char* filepath) {
        HANDLE handle = CreateFile(
            filepath, GENERIC_READ, FILE_SHARE_READ | FILE_SHARE_WRITE, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL
        );

        if (handle == INVALID_HANDLE_VALUE) {
            throw std::runtime_error("Could not open file handle\n");
        }

        LARGE_INTEGER file_size;
        if (!GetFileSizeEx(handle, &file_size)) {
            CloseHandle(handle);
            throw std::runtime_error("Could not get file size\n");
        }

        CloseHandle(handle);
        return static_cast<std::size_t>(file_size.QuadPart);
    }

}  // namespace io

#endif  // IO_WIN64_HPP_
