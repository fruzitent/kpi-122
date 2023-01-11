#ifndef IO_LINUX_HPP_
#define IO_LINUX_HPP_

#include <sys/stat.h>

#include <stdexcept>

namespace io {
    static std::size_t get_filesize(const char* filepath) {
        struct stat stbuf {};

        if (stat(filepath, &stbuf) != 0) {
            throw std::runtime_error("Could not get file size");
        }

        return static_cast<std::size_t>(stbuf.st_size);
    }
}  // namespace io

#endif  // IO_LINUX_HPP_
