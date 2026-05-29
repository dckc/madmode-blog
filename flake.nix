{
  description = "D-Bus notification experiments with Jeepney";

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
          python3
          python3Packages.jeepney
          zig
          gnumake
          bloaty             # hierarchical ELF size profiler
          binutils           # objdump (function boundaries), strip
          typescript         # tsc for TypeScript type checking
        ];
      };
    };
}
  
