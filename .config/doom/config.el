(setq user-full-name "Patrick Wulfe"
      user-mail-address "wulfep@gmail.com")

(setq doom-font (font-spec :family "Fira Code" :size 16 :weight 'medium)
      doom-variable-pitch-font (font-spec :family "Noto Sans" :size 13)
      doom-big-font (font-spec :family "Literation Sans")
      )

(setq doom-theme 'my-doom-horizon)

(setq display-line-numbers-type 'relative)

(setq centaur-tabs-height 32
      centaur-tabs-style "wave")

(setq scroll-margin 10)

(setq confirm-kill-emacs nil)

(setq undo-limit 80000000
      evil-want-fine-undo t)

(setq auto-save-default t
      make-backup-files t)

(setq org-directory "~/org/")

(when (and (featurep! :tools lsp) (not (featurep! :tools lsp +eglot)))
  (use-package! lsp-mode :defer t :config
    (add-hook! lsp-after-open
      (setq company-backends '((:separate company-yasnippet company-capf) company-yasnippet)))))

(setq evil-snipe-scope 'visible
      evil-snipe-spillover-scope 'buffer)

(setq projectile-project-search-path '("~/dev/src/"))

(map! :leader
      :desc "M-x" "SPC" #'execute-extended-command
      :desc "Find file in project" ":" #'projectile-find-file)

(setq doom-leader-key "SPC"
      doom-localleader-key ",")

(map! :leader
      :desc "Comment operator" ";" #'evilnc-comment-operator
      :desc "Open vterm" "v" #'vterm
      :desc "Open snippets" "y" #'yas-insert-snippet)

(map! :leader
      :desc "Go to test/implimentation file" "p j"
      #'projectile-toggle-between-implementation-and-test)

(map! :leader
      :desc "Tabs" "t T" #'centaur-tabs-mode)

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

(setq lsp-dart-main-code-lens nil
      lsp-dart-test-code-lens nil)

(use-package flutter-l10n-flycheck
  :after flutter
  :config
  (flutter-l10n-flycheck-setup))

(with-eval-after-load 'projectile
  (add-to-list 'projectile-project-root-files-bottom-up "pubspec.yaml")
  (add-to-list 'projectile-project-root-files-bottom-up "BUILD"))
(projectile-register-project-type 'flutter '("pubspec.yaml")
                                  :project-file "pubspec.yaml"
                                  :src-dir "lib/"
                                  :test "flutter test"
                                  :test-dir "test/"
                                  :test-suffix "_test")
