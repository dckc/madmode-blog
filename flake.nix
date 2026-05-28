{
  description = "A tiny Zig environment for writing minimal D-Bus notifications";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux"; # Adjust if you're on aarch64-linux, etc.
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          zig
          gnumake
        ];
      };
    };
}
  
