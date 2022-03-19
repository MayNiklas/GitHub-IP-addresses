{
  description = "Generate nginx allow lists from GitHub API";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:

    {
      checks."x86_64-linux".example =
        self.packages."x86_64-linux".github_ip_addresses;
    } //

    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system};

      in rec {
        packages = flake-utils.lib.flattenTree rec {

          github_ip_addresses = with pkgs.python39Packages;
            pkgs.python39Packages.buildPythonPackage rec {

              pname = "github_ip_addresses";
              version = "1.0.0";

              propagatedBuildInputs = [ requests ];

              src = self;
            };

        };
        defaultPackage = packages.github_ip_addresses;
      });
}
