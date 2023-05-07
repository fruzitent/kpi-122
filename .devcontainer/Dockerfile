# syntax=docker/dockerfile:1.5-labs

ARG VARIANT="jammy"

FROM ubuntu:${VARIANT}

RUN <<EOF
    echo "hello"
EOF

RUN <<EOF
    idonotexist2
EOF

CMD sleep infinity
