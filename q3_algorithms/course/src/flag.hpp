#ifndef FLAG_HPP_
#define FLAG_HPP_

#include <cstring>
#include <stdexcept>

using namespace std::string_literals;

namespace flag {
    enum class Type {
        Bool,
        CStr,
    };

    union Value {
        bool  as_bool;
        char *as_cstr;
    };

    enum class Error {
        NONE,
        UNKNOWN,
        NO_VALUE,
        INVALID_NUMBER,
        INTEGER_OVERFLOW,
        INVALID_SIZE_SUFFIX,
    };

    struct Flag {
        char *name;
        char *usage;
        Type  type;
        Value value;
        Value default_value;
    };

    static constexpr std::size_t CAPACITY = 256;

    static struct Context {
        Flag        flags[CAPACITY];
        std::size_t count;

        Error error;
        char *error_name;

        int    argc;
        char **argv;
    } global {};  // NOLINT

    inline Flag *create(Type type, const char *name, const char *usage) {
        if (global.count >= CAPACITY) {
            throw std::out_of_range("Not enough capacity\n");
        }

        Flag *flag = &global.flags[global.count++];
        // memset(flag, 0, sizeof(*flag));
        flag->type  = type;
        flag->name  = const_cast<char *>(name);   // NOLINT
        flag->usage = const_cast<char *>(usage);  // NOLINT

        return flag;
    }

    inline bool *Bool(const char *name, bool value, const char *usage) {
        Flag *flag                  = create(Type::Bool, name, usage);
        flag->default_value.as_bool = value;
        flag->value.as_bool         = value;
        return &flag->value.as_bool;
    }

    inline char **CStr(const char *name, const char *value, const char *usage) {
        Flag *flag                  = create(Type::CStr, name, usage);
        flag->value.as_cstr         = const_cast<char *>(value);  // NOLINT
        flag->default_value.as_cstr = const_cast<char *>(value);  // NOLINT
        return &flag->value.as_cstr;
    }

    static char *shift(int *argc, char ***argv) {
        if (*argc <= 0) {
            throw std::invalid_argument("No arguments\n");
        }
        char *result = **argv;
        *argv += 1;
        *argc -= 1;
        return result;
    }

    inline void parse(int argc, char **argv) {
        shift(&argc, &argv);

        while (argc > 0) {
            char *flag = shift(&argc, &argv);

            if (*flag != '-') {
                global.argc = argc + 1;
                global.argv = argv - 1;
                return;
            }

            if (std::strcmp(flag, "--") == 0) {
                global.argc = argc;
                global.argv = argv;
                return;
            }

            flag += 1;
            bool found = false;

            for (std::size_t i = 0; i < global.count; ++i) {
                if (std::strcmp(global.flags[i].name, flag) == 0) {
                    switch (global.flags[i].type) {
                        case Type::Bool: {
                            global.flags[i].value.as_bool = true;
                            break;
                        }

                        case Type::CStr: {
                            if (argc == 0) {
                                throw std::invalid_argument("No value\n");
                            }

                            char *arg = shift(&argc, &argv);

                            global.flags[i].value.as_cstr = arg;
                            break;
                        };

                        default: {
                            throw std::runtime_error("Unreachable\n");
                        }
                    }
                }

                found = true;
            }

            if (!found) {
                throw std::invalid_argument("Unknown flag\n");
            }
        }

        global.argc = argc;
        global.argv = argv;
    }

    inline void options(std::FILE *stream) {
        for (size_t i = 0; i < global.count; ++i) {
            Flag *flag = &global.flags[i];

            std::fprintf(stream, "    -%s\n", flag->name);
            std::fprintf(stream, "        %s\n", flag->usage);

            switch (global.flags[i].type) {
                case Type::Bool: {
                    if (flag->default_value.as_bool) {
                        // cppcheck-suppress knownConditionTrueFalse
                        std::fprintf(stream, "        Default: %s\n", flag->default_value.as_bool ? "true" : "false");
                    }
                    break;
                }

                case Type::CStr: {
                    if (flag->default_value.as_cstr != nullptr) {
                        std::fprintf(stream, "        Default: %s\n", flag->default_value.as_cstr);
                    }
                    break;
                }

                default: {
                    throw std::runtime_error("Unreachable\n");
                }
            }
        }
    }
}  // namespace flag

#endif  // FLAG_HPP_
