;; https://www.emacswiki.org/emacs/LoadPath
(add-to-list 'load-path "~/.emacs.d/dev-dckc/")

(require 'melpa-init)
(package-initialize)

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
    (pyvenv magit js2-mode flycheck-flow add-node-modules-path))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
