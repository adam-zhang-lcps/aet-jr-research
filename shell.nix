{pkgs ? import <nixpkgs> {}}:
with pkgs;
  mkShell {
    buildInputs = [(python3.withPackages (ps: with ps; [numpy matplotlib])) python3Packages.python-lsp-server];
  }
