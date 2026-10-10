#!/usr/bin/env bash
# Installs and starts Paperclip (github.com/paperclipai/paperclip) from source.
# Usage: scripts/setup-paperclip.sh [install-dir] [data-dir]
set -euo pipefail

SRC_DIR="${1:-$HOME/paperclip}"
DATA_DIR="${2:-$HOME/paperclip-data}"
NODE_DIR="/opt/node24"

# 1. Node >= 24.11 (repo requirement)
if ! command -v node >/dev/null || [ "$(node -p 'process.versions.node.split(".")[0]')" -lt 24 ]; then
  if [ ! -x "$NODE_DIR/bin/node" ]; then
    V=$(curl -fsSL https://nodejs.org/dist/index.json \
      | python3 -c "import json,sys;print([r['version'] for r in json.load(sys.stdin) if r['version'].startswith('v24.')][0])")
    mkdir -p "$NODE_DIR"
    curl -fsSL "https://nodejs.org/dist/$V/node-$V-linux-x64.tar.xz" | tar -xJ -C "$NODE_DIR" --strip-components=1
  fi
  export PATH="$NODE_DIR/bin:$PATH"
fi
corepack enable --install-directory "$(dirname "$(command -v node)")"

# 2. Source + dependencies + build
[ -d "$SRC_DIR/.git" ] || git clone --depth 50 https://github.com/paperclipai/paperclip.git "$SRC_DIR"
cd "$SRC_DIR"
COREPACK_ENABLE_DOWNLOAD_PROMPT=0 pnpm install --frozen-lockfile
pnpm build

# 3. Embedded Postgres refuses to run as root and drops to the "postgres" user,
#    so its data directory must be owned by that user.
DB_DIR="$DATA_DIR/instances/default/db"
mkdir -p "$DB_DIR"
if [ "$(id -u)" = 0 ] && id postgres >/dev/null 2>&1; then
  chown postgres "$DB_DIR"
  chmod 700 "$DB_DIR"
fi

# 4. Start (local_trusted, loopback :3100). Telemetry is opt-out upstream; disable it.
export PAPERCLIP_TELEMETRY_DISABLED=1 DO_NOT_TRACK=1
exec pnpm dev:once --data-dir "$DATA_DIR"
