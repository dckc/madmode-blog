with import <nixpkgs> {};

stdenv.mkDerivation rec {
  name = "env";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = [
    # 10.16.0 is current LTS as of Jul 1, 2019
    nodejs-10_x
  ];
}
