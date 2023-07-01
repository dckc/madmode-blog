;; http://ensime.github.io/editors/emacs/install/
;; The recommended way to install ENSIME is via MELPA stable and use-package:

(provide 'scala-dev-ensime)

;; http://ensime.github.io/editors/emacs/learning/
;; the package manager
(require 'package)
(setq
 package-archives '(("gnu" . "http://elpa.gnu.org/packages/")
                    ("org" . "http://orgmode.org/elpa/")
;                    ("melpa" . "http://melpa.org/packages/")
                    ("melpa-stable" . "http://stable.melpa.org/packages/"))
 package-archive-priorities '(("melpa-stable" . 1)))

(package-initialize)
(when (not package-archive-contents)
  (package-refresh-contents)
  (package-install 'use-package))
(require 'use-package)

(use-package ensime
  :ensure t
  :pin melpa-stable)
