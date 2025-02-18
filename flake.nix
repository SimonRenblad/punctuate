{
  description = "punctuate - a simple script to randomly capitalize, quote and punctuate words";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
  let 
    pkgs = import nixpkgs { system = "x86_64-linux"; };
    punctuate = pkgs.stdenv.mkDerivation {
      name = "punctuate";
      propagatedBuildInputs = [
        pkgs.python3
      ];
      dontUnpack = true;
      installPhase = "install -Dm755 ${./punctuate.py} $out/bin/punctuate";
    };
  in
  {
      packages.x86_64-linux.default = punctuate;
  };
}
