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

(setq projectile-project-search-path '("~/dev/src/"))

(map! :leader
      (:desc "Go to test/implimentation file" "p ," #'projectile-toggle-between-implimentation-and-test))

(map! :leader
      :desc "Org babel tangle" "m B" #'org-babel-tangle)

(map! :leader
        (:prefix ("f ." . "open dotfile")
         :desc "Edit doom config.org" "d" #'(lambda () (interactive) (find-file "~/.config/doom/config.org"))
         :desc "Open qtile README.org" "q" #'(lambda () (interactive) (find-file "~/.config/qtile/README.org"))
         :desc "Edit alacritty alacritty.yml" "a" #'(lambda () (interactive) (find-file "~/.config/alacritty/alacritty.yml"))
         :desc "Open fish README.org" "f" #'(lambda () (interactive) (find-file "~/.config/fish/README.org"))
         ))

(use-package lsp-dart
  :init
  (map! :map dart-mode-map
        (:localleader
        (:prefix ("p" . "pub")
         "g" #'lsp-dart-pub-get ))))
(with-eval-after-load 'projectile
  (add-to-list 'projectile-project-root-files-bottom-up "pubspec.yaml")
  (add-to-list 'projectile-project-root-files-bottom-up "BUILD"))
;; (use-package dart-mode
;;   :hook (dart-mode . (lambda ()
;;                        (add-hook 'after-save-hook #'flutter-run-or-hot-reload nil t))))
(use-package flutter-l10n-flycheck
  :after flutter
  :config
  (flutter-l10n-flycheck-setup))
