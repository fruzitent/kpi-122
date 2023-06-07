# syntax=docker/dockerfile:1.5-labs

# [18.04]: bionic, [20.04]: focal, [22.04]: jammy, [22.10]: kinetic, [23.04]: lunar, [23.10]: mantic
ARG VARIANT="lunar"

FROM ubuntu:${VARIANT}

ARG DEBIAN_FRONTEND="noninteractive"

# Let apt cache packages
# Reference: https://github.com/moby/buildkit/blob/master/frontend/dockerfile/docs/reference.md#run---mounttypecache

RUN <<EOF
    rm -rf "/etc/apt/apt.conf.d/docker-clean"
EOF

COPY <<EOF "/etc/apt/apt.conf.d/keep-cache"
Binary::apt::APT::Keep-Downloaded-Packages "true";
EOF

# Some mirrors may use HTTPS

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked <<EOF
    apt-get update
    apt-get -y install --no-install-recommends ca-certificates

    mirror_url="mirror://mirrors.ubuntu.com/mirrors.txt"
    ubuntu_url="http://archive.ubuntu.com/ubuntu"
    sed -e "s%${ubuntu_url}%${mirror_url}%" -i "/etc/apt/sources.list"

    apt-get update
    apt-get -y install --no-install-recommends gnupg2 wget
EOF

# Setup locales and timezones

ENV TZ="UTC"

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked <<EOF
    apt-get update
    apt-get -y install --no-install-recommends locales tzdata

    sed -e "/en_US.UTF-8/s/^# //g" -i "/etc/locale.gen"
    locale-gen

    ln -fs "/usr/share/zoneinfo/${TZ}" "/etc/localtime"
    dpkg-reconfigure tzdata
EOF

ENV LANG="en_US.UTF-8"
ENV LANGUAGE="en_US:en"
ENV LC_ALL="en_US.UTF-8"

# Install GCC
# Reference: https://gcc.gnu.org/install

ARG GCC_VERSION="13"

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked <<EOF
    . /etc/os-release

    {
        filename="ubuntu-toolchain-r-ubuntu-ppa-${VERSION_CODENAME}"
        key="https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x60c317803a41ba51845e371a1e9377a2ba9ef27f"
        url="https://ppa.launchpadcontent.net/ubuntu-toolchain-r/ppa/ubuntu"
        if wget --spider "${url}/dists/${VERSION_CODENAME}"; then
            wget -O - "${key}" | gpg --batch --dearmor --no-tty --output "/usr/share/keyrings/${filename}.gpg"
            echo "deb [signed-by=/usr/share/keyrings/${filename}.gpg] ${url} ${VERSION_CODENAME} main" >> "/etc/apt/sources.list.d/${filename}.list"
        fi
    }

    {
        filename="ubuntu-toolchain-r-ubuntu-test-${VERSION_CODENAME}"
        key="https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x60c317803a41ba51845e371a1e9377a2ba9ef27f"
        url="https://ppa.launchpadcontent.net/ubuntu-toolchain-r/test/ubuntu"
        if wget --spider "${url}/dists/${VERSION_CODENAME}"; then
            wget -O - "${key}" | gpg --batch --dearmor --no-tty --output "/usr/share/keyrings/${filename}.gpg"
            echo "deb [signed-by=/usr/share/keyrings/${filename}.gpg] ${url} ${VERSION_CODENAME} main" >> "/etc/apt/sources.list.d/${filename}.list"
        fi
    }

    apt-get update
    apt-get -y install --no-install-recommends g++-${GCC_VERSION} gcc-${GCC_VERSION} gdb make
    update-alternatives --install "/usr/local/bin/gcc" gcc "/usr/bin/gcc-${GCC_VERSION}" 1
    update-alternatives --install "/usr/local/bin/g++" g++ "/usr/bin/g++-${GCC_VERSION}" 1
EOF

# Install LLVM
# Reference: https://llvm.org/docs/GettingStarted.html

ARG LLVM_VERSION="17"

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked <<EOF
    apt-get update
    apt-get -y install --no-install-recommends gnupg lsb-release software-properties-common wget

    wget -O - "https://apt.llvm.org/llvm.sh" | bash -s ${LLVM_VERSION} all
    echo "update-alternatives --install /usr/local/bin/clang       clang       /usr/bin/clang-${LLVM_VERSION}       1 $(find -L "/usr/lib/llvm-${LLVM_VERSION}/bin" -type f -executable -not -name "clang"       -not -name "llvm*" -printf "--slave /usr/local/bin/%f %f /usr/bin/%f-${LLVM_VERSION} ")" | sh
    echo "update-alternatives --install /usr/local/bin/llvm-config llvm-config /usr/bin/llvm-config-${LLVM_VERSION} 1 $(find -L "/usr/lib/llvm-${LLVM_VERSION}/bin" -type f -executable -not -name "llvm-config"      -name "llvm*" -printf "--slave /usr/local/bin/%f %f /usr/bin/%f-${LLVM_VERSION} ")" | sh
EOF

# Install Python
# Reference: https://docs.python.org/3/using/index.html
# Reference: https://pip.pypa.io/en/stable/installation
# Reference: https://python-poetry.org/docs/#installation

ARG PYTHON_VERSION="3.11"

ENV PYTHONUNBUFFERED="1"

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked <<EOF
    . /etc/os-release

    {
        filename="deadsnakes-ubuntu-nightly-${VERSION_CODENAME}"
        key="https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xf23c5a6cf475977595c89f51ba6932366a755776"
        url="https://ppa.launchpadcontent.net/deadsnakes/nightly/ubuntu"
        if wget --spider "${url}/dists/${VERSION_CODENAME}"; then
            wget -O - "${key}" | gpg --batch --dearmor --no-tty --output "/usr/share/keyrings/${filename}.gpg"
            echo "deb [signed-by=/usr/share/keyrings/${filename}.gpg] ${url} ${VERSION_CODENAME} main" >> "/etc/apt/sources.list.d/${filename}.list"
        fi
    }

    {
        filename="deadsnakes-ubuntu-ppa-${VERSION_CODENAME}"
        key="https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xf23c5a6cf475977595c89f51ba6932366a755776"
        url="https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu"
        if wget --spider "${url}/dists/${VERSION_CODENAME}"; then
            wget -O - "${key}" | gpg --batch --dearmor --no-tty --output "/usr/share/keyrings/${filename}.gpg"
            echo "deb [signed-by=/usr/share/keyrings/${filename}.gpg] ${url} ${VERSION_CODENAME} main" >> "/etc/apt/sources.list.d/${filename}.list"
        fi
    }

    apt-get update
    apt-get -y install --no-install-recommends python${PYTHON_VERSION}-dev
    update-alternatives --install "/usr/local/bin/python3" python3 "/usr/bin/python${PYTHON_VERSION}" 1

    wget -O - "https://bootstrap.pypa.io/get-pip.py" | python3 -        --break-system-packages
    python3 -m pip install --upgrade pip setuptools tk virtualenv wheel --break-system-packages

    python3 -m pip install poetry --break-system-packages
    poetry config virtualenvs.in-project true
EOF

# Install common
# Reference: https://github.com/git/git/blob/master/INSTALL
# Reference: https://github.com/git-lfs/git-lfs#installing
# Reference: https://github.com/neovim/neovim/wiki/Installing-Neovim

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked <<EOF
    apt-get update
    apt-get -y install --no-install-recommends git git-lfs neovim
EOF

# Install C++ tooling
# Reference: https://cmake.org/install
# Reference: https://ninja-build.org
# Reference: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
# Reference: https://github.com/danmar/cppcheck
# Reference: https://doxygen.nl/manual/install.html
# Reference: https://graphviz.org/download
# Reference: https://github.com/cheshirekow/cmake_format#installation
# Reference: https://google.github.io/styleguide/cppguide.html#cpplint

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked <<EOF
    {
        wget -O - "https://apt.kitware.com/kitware-archive.sh" | sh -s -- --rc
    } || true

    apt-get update
    apt-get -y install --no-install-recommends cmake cmake-curses-gui ninja-build
    apt-get -y install --no-install-recommends ccache cppcheck doxygen graphviz

    python3 -m pip install --upgrade cmakelang cpplint --break-system-packages
EOF

# Install IWYU
# Reference: https://github.com/include-what-you-use/include-what-you-use/tree/master#instructions-for-users

RUN <<EOF
    {
        mkdir -p "/usr/src/iwyu"
        wget -O - "https://github.com/include-what-you-use/include-what-you-use/archive/refs/heads/clang_${LLVM_VERSION}.tar.gz" ||
        wget -O - "https://github.com/include-what-you-use/include-what-you-use/archive/refs/heads/master.tar.gz"
    } | tar --directory "/usr/src/iwyu" --extract --gzip --strip-components 1

    CC="clang-${LLVM_VERSION}"
    CXX="clang++-${LLVM_VERSION}"

    mkdir -p        "/usr/src/iwyu/build"
    cmake -B        "/usr/src/iwyu/build" -S "/usr/src/iwyu" -DCMAKE_PREFIX_PATH="/usr/lib/llvm-${LLVM_VERSION}" -G "Ninja"
    cmake --build   "/usr/src/iwyu/build" -j $(nproc --all)
    cmake --install "/usr/src/iwyu/build"
    rm -rf "/usr/src/iwyu"

    iwyu_resources="$(include-what-you-use  --print-resource-dir 2>/dev/null)"
    llvm_resources="$(clang-${LLVM_VERSION} --print-resource-dir 2>/dev/null)"

    mkdir -p "${iwyu_resources}"
    ln -s    "${llvm_resources}/include" "${iwyu_resources}/include"
EOF

# Install Rust
# Reference: https://rust-lang.github.io/rustup/installation/index.html
# Reference: https://rust-analyzer.github.io/manual.html#installation
# Reference: https://github.com/rust-lang/miri#using-miri

ARG RUST_VERSION="1.70.0"

ENV CARGO_HOME="/opt/cargo"
ENV RUSTUP_HOME="/opt/rustup"
ENV PATH="${CARGO_HOME}/bin:${PATH}"

RUN <<EOF
    wget -O - "https://sh.rustup.rs" | sh -s -- -y --default-toolchain "${RUST_VERSION}"
    rustup          component add rust-analyzer rust-src
    rustup +nightly component add miri
EOF

# Install SCCache
# Reference: https://github.com/mozilla/sccache#installation

ARG SCCACHE_VERSION="0.5.3"

RUN <<EOF
    filename="sccache-v${SCCACHE_VERSION}-$(uname -m)-unknown-linux-musl"
    wget -O - "https://github.com/mozilla/sccache/releases/download/v${SCCACHE_VERSION}/${filename}.tar.gz" | tar --directory "/usr/local/bin" --extract --gzip --strip-components 1 "${filename}/sccache"
EOF

COPY <<EOF "${CARGO_HOME}/config.toml"
[build]
rustc-wrapper = "sccache"
EOF

# Install TeXLive
# Reference: https://tug.org/texlive/doc/install-tl.html

ENV PATH="/usr/local/texlive:${PATH}"

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked <<EOF
    apt-get update
    apt-get -y install --no-install-recommends fontconfig perl

    mkdir -p "/opt/texlive"
    wget -O - "https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz" | tar --directory "/opt/texlive" --extract --gzip --strip-components 1
    perl  "/opt/texlive/install-tl" --no-interaction --scheme "scheme-minimal" --texdir="/opt/texlive"
    ln -s "/opt/texlive/bin/$(uname -m)-linux" "/usr/local/texlive"

    tlmgr update --all --self
    tlmgr install latexmk

    apt-get -y install --no-install-recommends cpanminus
    cpanm install File::HomeDir YAML::Tiny
EOF

CMD sleep infinity
