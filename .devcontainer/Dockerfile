# syntax=docker/dockerfile:1.5-labs

ARG VARIANT="jammy"

FROM ubuntu:${VARIANT}

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked <<EOF
    apt-get update
    apt-get -y install --no-install-recommends wget
EOF

RUN <<EOF
    echo "hello"
EOF

RUN <<EOF
    idonotexist
EOF

CMD sleep infinity
