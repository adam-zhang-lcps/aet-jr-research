{pkgs ? import <nixpkgs> {}}:
with pkgs;
  mkShell {
    buildInputs = [(python3.withPackages (ps: with ps; [numpy matplotlib scikit-learn])) python3Packages.python-lsp-server];
  }
