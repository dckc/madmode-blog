# not sure how to make this work as a .nix file, but this works:
#
# $ nix-shell -p "haskellPackages.ghcWithPackages (pkgs: [pkgs.hakyll])"

with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "madmode-site";

  buildInputs = [
    haskellPackages.ghcWithPackages (
      pkgs: [pkgs.hakyll pkgs.cabal-install]
    ) ];
}
