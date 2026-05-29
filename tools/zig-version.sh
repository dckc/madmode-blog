#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 Dan Connolly
# SPDX-License-Identifier: Apache-2.0
set -eu

FLAKE_NIXPKGS="github:nixos/nixpkgs/$(jq -r '.nodes.nixpkgs.locked.rev' flake.lock)"

echo "=== Zig version pinned by flake.lock ==="
nix eval "$FLAKE_NIXPKGS#zig.version"
echo "release notes:"
nix eval "$FLAKE_NIXPKGS#zig.meta.changelog" --raw
echo ""

printf "repo:            codeberg.org/ziglang/zig\n"
tag=$(nix eval "$FLAKE_NIXPKGS#zig" --apply 'x: x.src.drvAttrs.rev' --raw)
printf "git tag:         %s\n" "$tag"

resp=$(curl -sS --max-time 5 "https://codeberg.org/api/v1/repos/ziglang/zig/tags/$tag" 2>/dev/null || true)
if [ -n "$resp" ]; then
    tag_hash=$(printf '%s' "$resp" | jq -r '.id // empty')
    commit_hash=$(printf '%s' "$resp" | jq -r '.commit.sha // empty')
    [ -n "$tag_hash" ]   && printf "tag object hash:  %s\n" "$tag_hash"
    [ -n "$commit_hash" ] && printf "commit hash:      %s\n" "$commit_hash"
    [ -n "$commit_hash" ] && printf "short:            %s\n" "${commit_hash:0:12}"
else
    echo "(Codeberg API unreachable -- install curl to resolve tag)"
fi
echo ""

echo "source tarball hash (SRI):"
nix eval "$FLAKE_NIXPKGS#zig" --apply 'x: x.src.drvAttrs.outputHash'
echo ""

printf "nixpkgs commit:    %s\n" "$(jq -r '.nodes.nixpkgs.locked.rev' flake.lock)"
ts=$(jq -r '.nodes.nixpkgs.locked.lastModified' flake.lock)
printf "nixpkgs timestamp: %s (%s)\n" "$ts" "$(date -d @"$ts" '+%Y-%m-%d')"
printf "nixpkgs narHash:   %s\n" "$(jq -r '.nodes.nixpkgs.locked.narHash' flake.lock)"
