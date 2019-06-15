;; https://www.emacswiki.org/emacs/AutoModeAlist
(add-to-list 'auto-mode-alist '("\\.rho\\'" . scala-mode))

;; alternative:
;; https://github.com/rchain-community/rholang-syntax-highlighting


(require 'flycheck)

(flycheck-define-checker rholang-cli
  "Syntax checking for Rholang"
  ;; TODO: un-hard-code jar path
  :command ("java"
            "--add-opens=java.base/java.nio=ALL-UNNAMED"
            "-Dlogback.configurationFile=logback-rholang_cli.xml"
            "-jar" "/home/connolly/projects/rchain/rholang-cli/target/scala-2.12/rholangCLI-assembly-0.1.0-SNAPSHOT.jar"
            "--quiet" source-original)
  :standard-input t
  :modes (scala-mode java-mode)
  :error-patterns ((error (message (*? print)) " at " line ":" column))
  )

(add-to-list 'flycheck-checkers 'rholang-cli)
