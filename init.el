;; Added by Package.el.
(package-initialize)

;; https://www.emacswiki.org/emacs/LoadPath
(add-to-list 'load-path "~/.emacs.d/dev-dckc/")

(require 'tabs-are-evil)

(require 'js-dev-flow)

; (load-file "scala-dev-ensime.el")
;;; https://stackoverflow.com/a/750933/7963
(defun remove-dos-eol ()
  "Do not show ^M in files containing mixed UNIX and DOS line endings."
  (interactive)
  (setq buffer-display-table (make-display-table))
  (aset buffer-display-table ?\^M []))
