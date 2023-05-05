# syntax=docker/dockerfile:1.4-labs

ARG VARIANT="kinetic"

FROM ubuntu:$VARIANT

RUN yes | unminimize

ARG USERNAME="user"
ARG PASSWORD="password"
ARG USER_GID=1000
ARG USER_UID=1000

RUN <<EOF
    groupadd --gid $USER_GID $USERNAME
    useradd --create-home $USERNAME --gid $USER_GID --shell /bin/bash --uid $USER_UID
    echo "$USERNAME:$PASSWORD" | chpasswd
EOF

COPY <<EOF /etc/sudoers.d/$USERNAME
$USERNAME ALL=(root) NOPASSWD: ALL
EOF

RUN <<EOF
    apt-get update
    apt-get install -y --no-install-recommends apt-utils coreutils lsb-release software-properties-common sudo
    apt-get install -y --no-install-recommends build-essential ca-certificates curl git git-lfs gnupg2 libssl-dev openssl pkg-config rsync unzip wget zip
    apt-get install -y --no-install-recommends htop iproute2 less lsof ncdu neovim net-tools procps psmisc strace tree
    apt-get autoremove -y
    apt-get clean -y
    rm -rf /var/lib/apt/lists/*
EOF

ARG SSHD_PORT=22

RUN <<EOF
    apt-get update
    apt-get install -y --no-install-recommends openssh-client openssh-server
    apt-get autoremove -y
    apt-get clean -y
    rm -rf /var/lib/apt/lists/*
EOF

COPY <<EOF /etc/pam.d/sshd
session optional pam_loginuid.so
EOF

COPY <<EOF /etc/ssh/sshd_config
PermitRootLogin yes
Port            $SSHD_PORT
UsePAM          yes
EOF

RUN <<EOF
    apt-get update
    apt-get install -y --no-install-recommends locales
    apt-get autoremove -y
    apt-get clean -y
    rm -rf /var/lib/apt/lists/*
EOF

ENV LANG="en_US.UTF-8"
ENV LANGUAGE="en_US.UTF-8"
ENV LC_ALL="C.UTF-8"

COPY <<EOF /etc/locale.gen
$LANG UTF-8
EOF

RUN <<EOF
    locale-gen
EOF

USER $USERNAME

ARG FONTS_URL="https://github.com/ryanoasis/nerd-fonts/releases/latest/download/Meslo.zip"

RUN <<EOF
    sudo apt-get update
    sudo apt-get install -y --no-install-recommends fontconfig
    sudo apt-get autoremove -y
    sudo apt-get clean -y
    sudo rm -rf /var/lib/apt/lists/*
EOF

RUN <<EOF
    curl -L $FONTS_URL -o    /tmp/fonts.zip
    mkdir -p                 /home/$USERNAME/.local/share/fonts
    unzip  /tmp/fonts.zip -d /home/$USERNAME/.local/share/fonts
    rm -rf /tmp/fonts.zip
    fc-cache -fv
EOF

RUN <<EOF
    sudo apt-get update
    sudo apt-get install -y --no-install-recommends exa fish fzf
    sudo apt-get autoremove -y
    sudo apt-get clean -y
    sudo rm -rf /var/lib/apt/lists/*
    sudo chsh $USERNAME -s /usr/bin/fish
EOF

SHELL ["/usr/bin/fish", "-c"]

ARG FISHER_URL="https://git.io/fisher"

RUN <<EOF
    curl -L $FISHER_URL | source
    fisher install "edc/bass"
    fisher install "gazorby/fish-abbreviation-tips"
    fisher install "jethrokuan/fzf"
    fisher install "jethrokuan/z"
    fisher install "jorgebucaran/fisher"
    fisher install "joseluisq/gitnow"
    fisher install "laughedelic/pisces"
    fisher install "markcial/upto"
    fisher install "meaningful-ooo/sponge"
    fisher install "nickeb96/puffer-fish"
EOF

ARG STARSHIP_URL="https://starship.rs/install.sh"

RUN <<EOF
    sh -c "$(curl -L $STARSHIP_URL)" -s --yes
    mkdir -p                              /home/$USERNAME/.config
    starship preset pastel-powerline    > /home/$USERNAME/.config/starship.toml
    mkdir -p                              /home/$USERNAME/.config/fish/conf.d
    echo "starship init fish | source" >> /home/$USERNAME/.config/fish/conf.d/config.fish
EOF

ARG NODE_VER="19.x"
ARG YARN_VER="stable"

RUN <<EOF
    curl -L https://deb.nodesource.com/setup_$NODE_VER | sudo sh
    sudo apt-get update
    sudo apt-get install -y --no-install-recommends nodejs
    sudo apt-get autoremove -y
    sudo apt-get clean -y
    sudo rm -rf /var/lib/apt/lists/*
    sudo corepack enable
    corepack prepare yarn@$YARN_VER --activate
EOF

ARG PYTHON_VER="3.11"

RUN <<EOF
    sudo apt-get update
    sudo apt-get install -y --no-install-recommends python$PYTHON_VER python$PYTHON_VER-dev python$PYTHON_VER-venv
    sudo apt-get autoremove -y
    sudo apt-get clean -y
    sudo rm -rf /var/lib/apt/lists/*
    sudo update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python$PYTHON_VER 1
EOF

ARG PIP_URL="https://bootstrap.pypa.io/get-pip.py"

RUN <<EOF
    mkdir -p      /home/$USERNAME/.local/bin
    fish_add_path /home/$USERNAME/.local/bin
    curl -L $PIP_URL | python3 -
    python3 -m pip install --upgrade --user pip setuptools virtualenv wheel
EOF

ARG POETRY_URL="https://install.python-poetry.org"

RUN <<EOF
    curl -L $POETRY_URL | python3 -
    mkdir -p                  /home/$USERNAME/.config/fish/completions
    poetry completions fish > /home/$USERNAME/.config/fish/completions/poetry.fish
    poetry config virtualenvs.in-project true
EOF

RUN <<EOF
    sudo apt-get update
    sudo apt-get install -y --no-install-recommends ccache cmake cmake-curses-gui cppcheck make ninja-build
    sudo apt-get autoremove -y
    sudo apt-get clean -y
    sudo rm -rf /var/lib/apt/lists/*
EOF

ARG GCC_VER="12"

RUN <<EOF
    sudo apt-get update
    sudo apt-get install -y --no-install-recommends g++-$GCC_VER gcc-$GCC_VER gdb
    sudo apt-get autoremove -y
    sudo apt-get clean -y
    sudo rm -rf /var/lib/apt/lists/*
    sudo update-alternatives --install /usr/local/bin/g++ g++ /usr/bin/g++-$GCC_VER 1
    sudo update-alternatives --install /usr/local/bin/gcc gcc /usr/bin/gcc-$GCC_VER 1
EOF

ARG LLVM_URL="https://apt.llvm.org/llvm.sh"
ARG LLVM_VER="16"

RUN <<EOF
    curl -L $LLVM_URL | sudo bash -s $LLVM_VER all
    echo "update-alternatives --install /usr/local/bin/clang       clang       /usr/bin/clang-$LLVM_VER       1 $(find -L "/usr/lib/llvm-$LLVM_VER/bin" -type f -executable -not -name "clang"       -not -name "llvm*" -printf "--slave /usr/local/bin/%f %f /usr/bin/%f-$LLVM_VER ")" | sudo sh
    echo "update-alternatives --install /usr/local/bin/llvm-config llvm-config /usr/bin/llvm-config-$LLVM_VER 1 $(find -L "/usr/lib/llvm-$LLVM_VER/bin" -type f -executable -not -name "llvm-config"      -name "llvm*" -printf "--slave /usr/local/bin/%f %f /usr/bin/%f-$LLVM_VER ")" | sudo sh
EOF

RUN <<EOF
    python3 -m pip install --user cmakelang cpplint
EOF

ARG RUSTUP_URL="https://sh.rustup.rs"

RUN <<EOF
    curl -L $RUSTUP_URL | sh -s -- -y --default-toolchain nightly
    fish_add_path /home/user/.cargo/bin
    rustup component add miri rust-analyzer rust-src
    cargo install sccache
EOF

COPY <<EOF /home/$USERNAME/.cargo/config.toml
[build]
rustc-wrapper = "sccache"
EOF

ARG TEXLIVE_URL="https://github.com/TeX-Live/installer/archive/refs/heads/master.zip"
ARG TEXLIVE_SCHEME="infraonly"

COPY <<EOF /tmp/texlive.profile
# https://tug.org/texlive/doc/install-tl.html
binary_x86_64-linux 1
selected_scheme   scheme-$TEXLIVE_SCHEME
TEXDIR            /usr/local/texlive/texdir
TEXMFLOCAL        /usr/local/texlive/texmf-local
TEXMFSYSCONFIG    /usr/local/texlive/texdir/texmf-config
TEXMFSYSVAR       /usr/local/texlive/texdir/texmf-var
TEXMFCONFIG       /home/$USERNAME/texlive/texmf-config
TEXMFVAR          /home/$USERNAME/texlive/texmf-var
TEXMFHOME         /home/$USERNAME/texmf
tlpdbopt_sys_bin  /usr/local/bin
tlpdbopt_sys_info /usr/local/share/info
tlpdbopt_sys_man  /usr/local/share/man
EOF

RUN <<EOF
    curl -L $TEXLIVE_URL -o /tmp/texlive.zip
    unzip                   /tmp/texlive.zip -d /tmp
    sudo perl               /tmp/installer-master/install-tl --no-interaction --profile /tmp/texlive.profile
    rm -rf                  /tmp/installer-master
    sudo chown -R $USERNAME:$USERNAME /usr/local/texlive
    fish_add_path                     /usr/local/texlive/texdir/bin/x86_64-linux
EOF

ARG TEXLIVEONFLY_URL="https://raw.githubusercontent.com/maphy-psd/texliveonfly/master/texliveonfly.py"

RUN <<EOF
    curl -L $TEXLIVEONFLY_URL -o /home/$USERNAME/texliveonfly.py
    tlmgr install biber biblatex chktex epstopdf-pkg infwarerr latex-bin latexindent latexmk tools xkeyval
    tlmgr install babel babel-ukrainian collection-fontsrecommended collection-fontutils fontaxes fontspec roboto ukrhyph
    tlmgr install amsmath booktabs geometry graphics hyperref mathtools microtype minted multirow parskip
    sudo ln -s /usr/local/texlive/texdir/texmf-var/fonts/conf/texlive-fontconfig.conf /etc/fonts/conf.d/09-texlive.conf
    fc-cache -fv
    sudo apt-get update
    sudo apt-get install -y --no-install-recommends cpanminus
    sudo apt-get autoremove -y
    sudo apt-get clean -y
    sudo rm -rf /var/lib/apt/lists/*
    sudo cpanm install File::HomeDir YAML::Tiny
EOF

ARG GITLFS_URL="https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh"

RUN <<EOF
    curl -L $GITLFS_URL | sudo bash
    sudo apt-get update
    sudo apt-get install -y --no-install-recommends cpanminus
    sudo apt-get autoremove -y
    sudo apt-get clean -y
    sudo rm -rf /var/lib/apt/lists/*
EOF

ARG GIT_EMAIL=""
ARG GIT_USERNAME=""

RUN <<EOF
    sudo mkdir -p                            /workspaces
    sudo chown -R $USERNAME:$USERNAME        /workspaces
EOF

COPY <<EOF /home/$USERNAME/.gitconfig
[safe]
    directory = /workspaces
[user]
    email = $GIT_EMAIL
    name = $GIT_USERNAME
EOF

WORKDIR /workspaces

EXPOSE $SSHD_PORT

CMD sudo service ssh start -D
