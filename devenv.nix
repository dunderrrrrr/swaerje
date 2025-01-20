{
  pkgs,
  lib,
  config,
  inputs,
  ...
}: {
  packages = [
    pkgs.git
    pkgs.alejandra
  ];

  languages = {
    python = {
      enable = true;
      package = pkgs.python312;

      venv.enable = true;

      uv = {
        enable = true;
        sync.enable = true;
      };
    };
  };
}
