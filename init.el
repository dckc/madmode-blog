;; Added by Package.el.
(package-initialize)

;; https://www.emacswiki.org/emacs/LoadPath
(add-to-list 'load-path "~/.emacs.d/dev-dckc/")

(require 'tabs-are-evil)

(require 'js-dev-flow)

; (load-file "scala-dev-ensime.el")
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages
   (quote
    (yaml-mode use-package tuareg systemd pyvenv php-mode markdown-mode magit lsp-ocaml json-mode js2-mode iedit helm-idris flymake-php flycheck-pyflakes flycheck-ocaml flycheck-mypy flycheck-flow ensime csv-mode calfw-org calfw-ical calfw-gcal calfw auto-complete add-node-modules-path))))
(put 'narrow-to-region 'disabled nil)


;;; https://stackoverflow.com/a/750933/7963
(defun remove-dos-eol ()
  "Do not show ^M in files containing mixed UNIX and DOS line endings."
  (interactive)
  (setq buffer-display-table (make-display-table))
  (aset buffer-display-table ?\^M []))
