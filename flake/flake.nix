{

    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
        flake-utils.url = "github:numtide/flake-utils";
        essentials.url = "path:/mnt/hdmenezess42/GitProjects/flakeEssentials";
    };

    outputs = { self, nixpkgs, flake-utils, essentials }:
        flake-utils.lib.eachDefaultSystem (system:
                let
                pkgs = import nixpkgs { inherit system; };
#python = pkgs.python311;

                pythonPkgs = pkgs.python311Packages;
                baseShell = essentials.devShells.${system}.python;
                in {

                devShell = pkgs.mkShell rec {
                name = "impurePythonEnv-flake";
                venvDir = "./.venv";
                buildInputs = [
                pythonPkgs.python
                pythonPkgs.venvShellHook
                pythonPkgs.setuptools
                pythonPkgs.pip
                pkgs.git
                pythonPkgs.ipython
                pythonPkgs.notebook
                pythonPkgs.ipykernel
                pythonPkgs.jupyter_client
                pythonPkgs.jupyter-core
                pythonPkgs.traitlets
                pythonPkgs.jupytext
                pythonPkgs.pynvim
                pythonPkgs.pyperclip

                pythonPkgs.graphviz

                pythonPkgs.pytest
                ] ++ baseShell.buildInputs;

                dontUsePytestCheck = true;
                doCheck = false;
# Install pip dependencies into the venv
                postVenvCreation = ''
                    unset SOURCE_DATE_EPOCH
                    pip install -r requirements.txt
                    '';

# Allow pip install wheels
                postShellHook = ''
                    unset SOURCE_DATE_EPOCH

                    HASH_FILE=".venv/.requirements_hash"
                    NEW_HASH=$(sha256sum requirements.txt | cut -d ' ' -f 1)

                    if [ ! -f $HASH_FILE ] || [ "$NEW_HASH" != "$(cat $HASH_FILE)" ]; then
                        echo "Installing Python deps from requirements.txt..."
                            pip install -r requirements.txt
                            echo $NEW_HASH > $HASH_FILE
                            fi
                            '';
                };
                }
                );
}
