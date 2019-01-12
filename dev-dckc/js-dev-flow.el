(require 'js2-mode)
(add-to-list 'auto-mode-alist '("\\.js\\'" . js2-mode))
(require 'flycheck-flow)
(add-hook 'js2-mode-hook 'flycheck-mode)

;; https://github.com/codesuki/add-node-modules-path
(require 'add-node-modules-path)
(eval-after-load 'js2-mode
  '(add-hook 'js2-mode-hook #'add-node-modules-path))

(add-to-list 'safe-local-variable-values '(js2-indent-switch-body . true))
(add-to-list 'safe-local-variable-values '(js2-basic-offset . 2))

;; (load-file "~/.emacs.d/flow-for-emacs/flow.el")
;; (setq flow_binary "/home/connolly/projects/finquick/node_modules/.bin/flow") ;; KLUDGE

;; (custom-set-variables
;;  ;; custom-set-variables was added by Custom.
;;  ;; If you edit it by hand, you could mess it up, so be careful.
;;  ;; Your init file should contain only one such instance.
;;  ;; If there is more than one, they won't work right.
;;  '(flycheck-javascript-eslint-executable nil)
;;  '(js2-basic-offset 2)
;;  '(safe-local-variable-values
;;    (quote
;;     ((eval progn
;;            (add-to-list
;;             (quote exec-path)
;;             (concat
;;              (locate-dominating-file default-directory ".dir-locals.el")
;;              "node_modules/.bin/")))
;;      (js2-basic-offset . 2)
;;      (js2-indent-switch-body . true)))))

(provide 'js-dev-flow)
