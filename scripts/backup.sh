#!/usr/bin/env bash
# Timestamped directory backup with retention (demo)
set -euo pipefail

SRC="${1:?Usage: backup.sh <source_dir> <dest_dir> [retention_days]}"
DEST="${2:?Usage: backup.sh <source_dir> <dest_dir> [retention_days]}"
RETENTION_DAYS="${3:-7}"

TS="$(date +%Y%m%d-%H%M%S)"
ARCHIVE="${DEST}/backup-${TS}.tar.gz"

mkdir -p "$DEST"
echo "[*] Backing up ${SRC} -> ${ARCHIVE}"
tar -czf "$ARCHIVE" -C "$(dirname "$SRC")" "$(basename "$SRC")"

echo "[*] Pruning backups older than ${RETENTION_DAYS} days"
find "$DEST" -name 'backup-*.tar.gz' -mtime "+${RETENTION_DAYS}" -delete

echo "[+] Done: ${ARCHIVE}"
