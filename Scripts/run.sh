#!/bin/sh
t=dirus/linter-node:latest && docker run -it --rm --name linter-node -v "$1":/usr/src/test:ro $t
