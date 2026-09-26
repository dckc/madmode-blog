{
  description = "Recover dm93.org/z2001 content from a 2004 Zope 2.7.7 Data.fs";

  inputs = {
    # gcc 13 rather than the newest: 2.3.5 predates C99 defaults and
    # implicit-function-declaration-is-an-error.
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        lib = pkgs.lib;

        # --- sources ---------------------------------------------------------
        # The Zope 2.7.7 README says "install python 2.3.5". Both tarballs
        # are still served (python.org, old.zope.org); hashes verified by
        # download on 2026-09-25.
        pythonSrc = pkgs.fetchurl {
          url = "https://www.python.org/ftp/python/2.3.5/Python-2.3.5.tgz";
          hash = "sha256-fBIt7/dwDwT7napbWzqIWxmnPaBcKiZEA2ZoF8djGXc=";
        };
        zopeSrc = pkgs.fetchurl {
          url = "https://old.zope.org/Products/Zope/2.7.7/Zope-2.7.7-final.tgz";
          hash = "sha256-lgUimHC1q5qGg9Upe0fu3Zu4T+oo7MCHdN99Q3kZKWo=";
        };

        # --- third-party products -------------------------------------------
        # The 2004 Data.fs uses two products that were never part of Zope.
        # AboutThisWiki.txt (in the wiki export) names both:
        #
        #   "On 23 Nov 2001, I upgraded dm93.org to zope 2.4 and installed
        #    this ZWiki product." ... "upgraded zwiki to ZWiki-0.34.0.tgz"
        #    (29 Sep 2004)
        #
        #   "unborked LocalFS ... Used LocalFS-1.3-andreas.tar.gz" (6 Nov 2004)
        #
        # ZWiki 0.34.0 is the 2004-09-02 release; without it ZWikiPage
        # unpickles as a non-importable placeholder, so zout2.py sees empty
        # pages. Its ZWikiPage is a DTMLDocument subclass, so the body is
        # the `raw` attribute zout2.py already reads.
        #
        # The product tarballs are archived, not served live: ZWiki from the
        # author's git history (simonmichael/zwiki, tag release-0-34-0),
        # LocalFS from the Wayback Machine copy of easyleading.org. Hashes
        # verified by download on 2026-09-25.
        zwikiSrc = pkgs.fetchurl {
          url = "https://codeload.github.com/simonmichael/zwiki/tar.gz/51398d99aa7beef86303c554ab6fa9883b78417a";
          hash = "sha256-fTumEUNwv2MaT1JzoYubCvwKwBSHxZY8OXfxVXElWV8=";
        };
        localfsSrc = pkgs.fetchurl {
          url = "http://web.archive.org/web/20070222171414id_/http://www.easyleading.org:80/Downloads/LocalFS-1.3-andreas.tar.gz";
          hash = "sha256-HBL7Tzup+y4N4HPF9MUWec27EPuBkU9Es6OgRH5fNZE=";
        };

        # Both tarballs unpack to a single top-level dir, so strip it.
        # Drop the CVS dirs the 2004 trees still carry.
        products = pkgs.runCommand "zope-products" { } ''
          mkdir -p $out/ZWiki $out/LocalFS
          tar xzf ${zwikiSrc} -C $out/ZWiki --strip-components=1
          tar xzf ${localfsSrc} -C $out/LocalFS --strip-components=1
          find $out -type d -name CVS -prune -exec rm -rf {} +
          chmod -R u+w $out
        '';

        # --- Python 2.3.5 ----------------------------------------------------
        python235 = pkgs.stdenv.mkDerivation {
          pname = "python";
          version = "2.3.5";
          src = pythonSrc;

          # `-U_FORTIFY_SOURCE`: Ubuntu's known fix for building 2.3.5 on a
          # modern toolchain (see 2013-migrate-old-zope.md).
          # `-fcommon`: 2004 code relies on tentative definitions.
          # `-std=gnu89`: don't let the compiler read the C sources as C23.
          preConfigure = ''
            export BASECFLAGS="-U_FORTIFY_SOURCE -fcommon"
            export CFLAGS="-std=gnu89 -Wno-implicit-function-declaration -Wno-error"
          '';

          # The plat-linux regen reads /usr/include/netinet/in.h, which
          # doesn't exist in the sandbox; use glibc's copy instead.
          # setup.py only searches /usr/include and /usr/lib, so point it at
          # the store paths of the optional modules we actually want.
          postPatch = ''
            substituteInPlace Lib/plat-generic/regen \
              --replace /usr/include/ ${lib.getDev pkgs.glibc}/include/
            substituteInPlace setup.py \
              --replace \
                "lib_dirs = self.compiler.library_dirs + ['/lib', '/usr/lib']" \
                "lib_dirs = self.compiler.library_dirs + ['/lib', '/usr/lib', '${lib.getLib pkgs.zlib}/lib', '${lib.getLib pkgs.bzip2}/lib', '${lib.getLib pkgs.readline}/lib', '${lib.getLib pkgs.ncurses}/lib']" \
              --replace \
                "inc_dirs = self.compiler.include_dirs + ['/usr/include']" \
                "inc_dirs = self.compiler.include_dirs + ['/usr/include', '${lib.getDev pkgs.zlib}/include', '${lib.getDev pkgs.bzip2}/include', '${lib.getDev pkgs.readline}/include', '${lib.getDev pkgs.ncurses}/include']"
            # readline >= 8 exports history_length; 2.3.5 declares its own
            # static of the same name. Rename every bare identifier (word
            # boundaries keep get_current_history_length intact).
            sed -i 's/\bhistory_length\b/py_history_length/g' Modules/readline.c
          '';

          # Nix's default hardening turns 2004 warnings into errors
          # (format-security here).
          hardeningDisable = [ "format" "fortify" "stackprotector" "pie" ];

          configureFlags = [
            "--prefix=${placeholder "out"}"
            "--without-cxx"
            "--with-threads"
          ];

          # 2004 test suite against a 2020s glibc: not worth the fight.
          doCheck = false;

          # zlib/bz2/readline are found by the patched setup.py; ncurses is
          # the fallback for readline and for _curses.
          buildInputs = with pkgs; [ zlib bzip2 readline ncurses ];

          # The interpreter is what we want; docs are noise.
          postInstall = ''
            rm -rf "$out/share"
          '';

          meta = with lib; {
            description = "Python 2.3.5, the interpreter Zope 2.7.7 expects";
            homepage = "https://www.python.org/downloads/release/python-235/";
            license = licenses.psfl;
            platforms = platforms.unix;
          };
        };

        # --- Zope 2.7.7 ------------------------------------------------------
        # Bundles the ZODB, Zope, ZPublisher, ZServer, Products etc. that
        # zout2.py imports. Installs to $out/lib/python, so $out/lib/python
        # goes on PYTHONPATH.
        zope277 = pkgs.stdenv.mkDerivation {
          pname = "zope";
          version = "2.7.7";
          src = zopeSrc;

          nativeBuildInputs = [ python235 ];
          buildInputs = [ python235 ];

          # The build compiles C extensions; it is not a pip project.
          preConfigure = ''
            export PATH="${python235}/bin:$PATH"
          '';

          configureFlags = [
            "--prefix=${placeholder "out"}"
            "--with-python=${python235}/bin/python"
          ];

          hardeningDisable = [ "format" "fortify" "stackprotector" "pie" ];

          # Zope's build leaves build-base/ and *.pyc behind; keep the tree
          # to what an instance needs.
          postInstall = ''
            rm -rf "$out/lib/python/test" "$out/doc"
            find "$out/lib/python" -name 'build' -type d -prune -exec rm -rf {} +
          '';

          meta = with lib; {
            description = "Zope 2.7.7 application server";
            homepage = "https://old.zope.org/Products/Zope/2.7.7/";
            license = licenses.zpl20;
            platforms = platforms.unix;
          };
        };
      in
      {
        packages = {
          default = zope277;
          inherit python235 zope277 products;
          sources = pkgs.linkFarm "zope-migrate-sources" [
            { name = "Python-2.3.5.tgz"; path = pythonSrc; }
            { name = "Zope-2.7.7-final.tgz"; path = zopeSrc; }
            { name = "ZWiki-0.34.0.tar.gz"; path = zwikiSrc; }
            { name = "LocalFS-1.3-andreas.tar.gz"; path = localfsSrc; }
          ];
        };

        devShells.default = pkgs.mkShell {
          packages = [ python235 zope277 pkgs.git pkgs.rsync ];
          # zout2.py does `from ZODB.FileStorage import ...` and
          # `from Zope import configure, app`; both come from Zope's lib.
          shellHook = ''
            export PYTHONPATH="${zope277}/lib/python''${PYTHONPATH:+:$PYTHONPATH}"
            echo "python: $(command -v python) ($(python -V 2>&1))"
            echo "zope:   ${zope277}"
          '';
        };
      });
}
