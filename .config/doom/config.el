(setq user-full-name "Patrick Wulfe"
      user-mail-address "wulfep@gmail.com")

(setq doom-font (font-spec :family "Fira Code" :size 16 :weight 'medium)
      doom-variable-pitch-font (font-spec :family "Noto Sans" :size 13)
      doom-big-font (font-spec :family "Literation Sans")
      )

(setq doom-theme 'my-doom-horizon)

(setq display-line-numbers-type 'relative)

(setq scroll-margin 10)

(setq confirm-kill-emacs nil)

(setq auto-save-default t
      make-backup-files t)

(setq org-directory "~/org/")

(map! :leader
      (:desc "Go to test/implimentation file" "f t" #'projectile-toggle-between-implimentation-and-test))

(map! :leader
      :desc "Org babel tangle" "m B" #'org-babel-tangle)

(map! :leader
        (:prefix ("f ." . "open dotfile")
         :desc "Edit doom config.org" "d" #'(lambda () (interactive) (find-file "~/.config/doom/config.org"))
         :desc "Edit qtile README.org" "q" #'(lambda () (interactive) (find-file "~/.config/qtile/README.org"))
         :desc "Edit alacritty alacritty.yml" "a" #'(lambda () (interactive) (find-file "~/.config/doom/config.org"))
         :desc "Open fish folder" "f" #'(lambda () (interactive) (find-file "~/.config/fish"))
         ))

(use-package lsp-mode :ensure t)
(use-package lsp-dart
  :ensure t
  :hook (dart-mode . lsp))
(use-package hover :ensure t)
