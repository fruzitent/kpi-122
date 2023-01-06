#include <cstdint>
#include <cstdlib>

extern "C" int LLVMFuzzerTestOneInput(
    [[maybe_unused]] const uint8_t *Data,
    [[maybe_unused]] size_t         Size
) {
    return 0;
}
