{
  description = "Minimal OCaml XDG desktop notifier";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          ocaml
          ocamlPackages.findlib
          ocamlPackages.dune_3
          ocamlPackages.utop
        ];
      };
    };
}
