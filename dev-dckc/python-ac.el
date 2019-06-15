;;; python auto-complete
;;; http://tkf.github.io/emacs-jedi/latest/

;; ugh: Too many open files
;; https://github.com/palantir/python-language-server/issues/431

(require 'jedi)

(add-hook 'python-mode-hook 'jedi:setup)
(setq jedi:complete-on-dot t)                 ; optional
