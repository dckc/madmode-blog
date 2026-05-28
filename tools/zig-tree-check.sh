#!/usr/bin/env bash
set -eu
die() { echo "$*" >&2; exit 1; }

tag=$(nix eval 'github:nixos/nixpkgs/'$(jq -r '.nodes.nixpkgs.locked.rev' flake.lock)'#zig.version' --raw)

echo "=== Source 1: nixpkgs (Codeberg via fetchzip) ==="
echo "fetching tag $tag from codeberg..."
url="https://codeberg.org/ziglang/zig/archive/$tag.tar.gz"
store_path=$(nix store prefetch-file --unpack "$url" 2>&1 \
  | sed -n "s/.*to '\([^']*\)'.*/\1/p")
echo "nix store path: $store_path"

expected_sri=$(nix eval 'github:nixos/nixpkgs/'$(jq -r '.nodes.nixpkgs.locked.rev' flake.lock)'#zig' --apply 'x: x.src.drvAttrs.outputHash' --raw)
computed_sri=$(nix hash path "$store_path" --sri 2>/dev/null || nix hash path "$store_path")
echo "expected SRI: $expected_sri"
echo "computed SRI: $computed_sri"

[ "$expected_sri" = "$computed_sri" ] || die "MISMATCH: nixpkgs SRI"

echo "MATCH: nixpkgs SRI"

tmp1=$(mktemp -d)
cp -r "$store_path/." "$tmp1"
chmod -R u+w "$tmp1"
git -C "$tmp1" init -q
git -C "$tmp1" add .
nix_tree=$(git -C "$tmp1" write-tree)
rm -rf "$tmp1"
echo ""

echo "=== Source 2: Codeberg git ==="
cb_tmp=$(mktemp -d)
git clone --depth 1 --branch "$tag" https://codeberg.org/ziglang/zig.git "$cb_tmp" 2>&1
codeberg_tree=$(git -C "$cb_tmp" rev-parse HEAD^{tree})
rm -rf "$cb_tmp"
echo "tree from nix:        $nix_tree"
echo "tree from codeberg:   $codeberg_tree"
[ "$nix_tree" = "$codeberg_tree" ] || die "MISMATCH: Codeberg tree"
echo "MATCH: Codeberg tree"
echo ""

echo "=== Source 3: ziglang.org release tarball ==="
echo "fetching index.json for shasum..."
json_url="https://ziglang.org/download/index.json"
shasum=$(curl -sS --max-time 10 "$json_url" | jq -r ".[\"$tag\"].src.shasum")
tarball_url=$(curl -sS --max-time 10 "$json_url" | jq -r ".[\"$tag\"].src.tarball")
echo "expected shasum: $shasum"
echo "tarball URL: $tarball_url"

tmp2=$(mktemp -d)
tarball_path="$tmp2/zig-source.tar.xz"
curl -sSL --max-time 60 -o "$tarball_path" "$tarball_url"
actual_shasum=$(sha256sum "$tarball_path" | cut -d' ' -f1)
echo "actual shasum:   $actual_shasum"
[ "$shasum" = "$actual_shasum" ] || die "MISMATCH: ziglang.org shasum"
echo "MATCH: ziglang.org shasum"

echo "extracting and computing tree..."
tar xf "$tarball_path" -C "$tmp2"
extracted_dir=$(find "$tmp2" -mindepth 1 -maxdepth 1 -type d)
git -C "$extracted_dir" init -q
git -C "$extracted_dir" add .
zl_tree=$(git -C "$extracted_dir" write-tree)
echo "tree from codeberg:    $codeberg_tree"
echo "tree from ziglang.org: $zl_tree"

if [ "$nix_tree" = "$zl_tree" ]; then
    echo "MATCH: trees are identical"
else
    echo "INFO: trees differ (expected — release tarball omits dev/CI infrastructure)"
    echo "files in codeberg tree not in release tarball:"
    diff <(cd "$store_path" && find . -type f | sort) \
         <(cd "$extracted_dir" && find . -type f | sort) \
    | grep '^<' | sed 's/^< /  /' || true
fi
rm -rf "$tmp2"
echo ""

echo "RESULTS:"
echo "  Source 1 (nixpkgs fetchzip): SRI match — nixpkgs pin matches Codeberg archive content"
echo "  Source 2 (Codeberg git):      tree match  — archive unpacks to same tree as git tag"
echo "  Source 3 (ziglang.org):        shasum match — tarball integrity verified"
