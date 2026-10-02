#!/usr/bin/env bash
# Builds the reference executable: gnuplot 5.4.9 (tag 5.4.9, commit a1bafa410d3c07d832f81884c5af61dee73fb1c5).
#   upstream/  unmodified source tree of the 5.4.9 release (git archive of the tag)
#   patches/   one build-only fix: post.trm fails to compile when no deflate (PNG) encoder is
#              configured; the patch only balances a brace under #ifdef. No behavioural change.
# Requirements: gcc, make, autoconf, automake, bison (all offline).  Output: ./bin/gnuplot (static, stripped)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT
cp -r "$HERE/upstream" "$WORK/src"
cd "$WORK/src"
for p in "$HERE"/patches/*.patch; do patch -s -p1 < "$p"; done
./prepare >/dev/null
mkdir build && cd build
../configure --without-x --without-qt --disable-wxwidgets --without-cairo --without-lua --without-libcerf \
  --without-latex --without-gd --without-caca --disable-plugins --without-readline \
  --without-bitmap-terminals --without-tektronix \
  CFLAGS="-O2" LDFLAGS="-static -Wl,--build-id=none" >/dev/null
make -j"$(nproc)" -C src >/dev/null 2>&1
mkdir -p "$HERE/bin"
cp src/gnuplot "$HERE/bin/gnuplot"
strip "$HERE/bin/gnuplot"
make -C docs gnuplot.gih >/dev/null 2>&1 && cp docs/gnuplot.gih "$HERE/bin/gnuplot.gih"
echo "built $HERE/bin/gnuplot ($(gcc --version | head -1))"
