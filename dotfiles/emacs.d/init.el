;; https://www.emacswiki.org/emacs/LoadPath
(add-to-list 'load-path "~/.emacs.d/lisp")

(require 'use-package)

(require 'tabs-are-evil)

;; file-attribute-size was added in Emacs 26.1.
;; https://github.com/alphapapa/org-web-tools/commit/e7abbfbd3ea7f277302656249b239eda3de40c94
(defun file-attribute-size (attrs)
  (nth 7 attrs))

(use-package direnv
 :config
 (direnv-mode))

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(flycheck-python-flake8-executable "/usr/bin/flake8")
 '(indent-tabs-mode nil)
 '(safe-local-variable-values
   '((eval setq flycheck-clang-include-path
           (list
            (expand-file-name "~/projects/moddable/xs/includes/")
            (expand-file-name "~/projects/moddable/xs/sources/")))
     (eval setq flycheck-clang-include-path
           (list
            (expand-file-name "~/projects/moddable/xs/includes/")))
     (js2-basic-offset . 2)
     (js2-indent-switch-body . true))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
(put 'narrow-to-region 'disabled nil)
