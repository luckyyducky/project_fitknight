# ~/blog_curator/shell.nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  # These are the packages that will be available in your shell
  buildInputs = [
    # The Python interpreter itself
    pkgs.python3

    # Any Python packages you need.
    # You find them under pkgs.python3.pkgs.*
    pkgs.python3.pkgs.pip
    pkgs.python3.pkgs.requests
    pkgs.python3.pkgs.django 
    pkgs.python3.pkgs.djangorestframework
    # Add other packages here, e.g., pkgs.python3.pkgs.flask, etc.
  ];

  shellHook = ''
    unset PROMPT_COMMAND
  '';
}