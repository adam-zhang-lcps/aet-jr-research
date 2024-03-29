{pkgs ? import <nixpkgs> {}}:
with pkgs;
  mkShell {
    buildInputs = [
      (python3.withPackages (ps:
        with ps; [
          numpy
          matplotlib
          scikit-learn
          tensorflow
          keras
          pandas
          seaborn
        ]))
      pyright
      black

      nodejs
      nodePackages.typescript-language-server
      nodePackages.prettier
    ];
  }
