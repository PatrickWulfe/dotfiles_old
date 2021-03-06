(setq user-full-name "Patrick Wulfe"
      user-mail-address "wulfep@gmail.com")

(setq doom-font (font-spec :family "Fira Code" :size 16 :weight 'medium)
      doom-variable-pitch-font (font-spec :family "Open Sans" :size 13)
      doom-big-font (font-spec :family "Open Sans")
      doom-serif-font (font-spec :family "Fira Code" :weigth 'light)
      )

(setq doom-theme 'my-doom-horizon)

(defface font-lock-operator-face
  '((t (:foreground "#21BFC2"))) "Basic face for operator." :group 'basic-faces)
;; C-Like
(dolist (mode-iter '(c-mode c++-mode dart-mode glsl-mode java-mode javascript-mode rust-mode))
  (font-lock-add-keywords mode-iter
   '(("\\([~^&\|!<>=,.\\+*/%-;:?]\\)" 0 'font-lock-operator-face keep))))
;; Scripting
(dolist (mode-iter '(python-mode lua-mode))
  (font-lock-add-keywords mode-iter
   '(("\\([@~^&\|!<>:=,.\\+*/%-]\\)" 0 'font-lock-operator-face keep))))

(use-package! nyan-mode
  :after doom-modeline
  :init
  (setq nyan-bar-length 40)
   (nyan-mode)
  )

(add-hook 'prog-mode-hook 'rainbow-delimiters-mode)

(setq display-line-numbers-type 'relative)

(setq
 scroll-conservatively 10
 scroll-step 1
 scroll-margin 10)

(scroll-bar-mode -1)

(setq confirm-kill-emacs nil)

(setq centaur-tabs-height 32
      centaur-tabs-style "bar")

;; (when IS-LINUX
;;   (set-frame-parameter (selected-frame) 'alpha '(99 . 99))
;;   (add-to-list 'default-frame-alist '(alpha . (99 . 99)))
;;   (add-to-list 'default-frame-alist '(inhibit-double-buffering . t)))

(setq undo-limit 80000000
      evil-want-fine-undo t)

(setq org-directory "~/org/")

(setq +lsp-company-backends '(:separate company-yasnippet company-capf))

;; (use-package! evil-motion-trainer
;;   :init
;;   (global-evil-motion-trainer-mode 1))
;;   ;; :config
;;   ;; (setq evil-motion-trainer-threshold 3))
;; ;; (setq evil-motion-trainer-super-annoying-mode t)
;; (map!
;;  :leader
;;  (:prefix-map ("t" . "toggle")
;;   :desc "Evil motion trainer" "t" #'evil-motion-trainer-mode))

(setq evil-snipe-scope 'visible
      evil-snipe-spillover-scope 'buffer)

(setq leetcode-prefer-language "cpp"
 leetcode-prefer-sql "mysql"
 leetcode-save-solutions t
 leetcode-directory "~/dev/src/leetcode"
)

(use-package mixed-pitch
  :hook
  (text-mode . mixed-pitch-mode))

(setq projectile-project-search-path '("~/dev/src/"))

(setq projectile-create-missing-test-files t)

;; (require 'sublimity-attractive)
;; (sublimity-mode 1)
;; (setq sublimity-attractive-centering-width 170)

(setq doom-themes-treemacs-theme "doom-colors")

(use-package doom-snippets
  :load-path "~/.config/doom/snippets"
  :after yasnippet)

(map! :leader
        (:prefix ("f ." . "open dotfile")
         :desc "Edit doom config.org" "d" #'(lambda () (interactive) (find-file "~/.config/doom/config.org"))
         :desc "Open qtile README.org" "q" #'(lambda () (interactive) (find-file "~/.config/qtile/README.org"))
         :desc "Edit alacritty.yml" "a" #'(lambda () (interactive) (find-file "~/.config/alacritty/alacritty.yml"))
         :desc "Open fish README.org" "f" #'(lambda () (interactive) (find-file "~/.config/fish/README.org"))
         ))

(map! (:after evil-easymotion :leader "j" evilem-map))
(map! :leader :prefix ("j" . "jump"))

(map! :leader
      :desc "M-x" "SPC" #'execute-extended-command
      :desc "Find file in project" ":" #'projectile-find-file)

(setq doom-leader-key "SPC"
      doom-localleader-key ",")

(map! :leader
      :desc "Comment operator" ";" #'evilnc-comment-operator)

(after! org (map! :localleader
                  :map org-mode-map
                  :desc "Org babel tangle" "B" #'org-babel-tangle))

(map! :leader
      :desc "Go to test/implimentation file" "p j"
      #'projectile-toggle-between-implementation-and-test)

(map! :leader
      :desc "Tabs" "t T" #'centaur-tabs-mode)

(map! :leader
      (:prefix ("y" . "snippets")
       :desc "Insert" "i" #'yas-insert-snippet
       :desc "New" "n" #'yas-new-snippet
       :desc "Tryout" "t" #'yas-tryout-snippet
      ))

(add-hook 'c-mode-hook 'lsp)
(add-hook 'c++-mode-hook 'lsp)

(use-package lsp-dart
  :init
  (setq lsp-dart-flutter-sdk-dir "~/dev/sdks/flutter")
  (map! :map dart-mode-map
        (:localleader
        (:prefix ("p" . "pub")
         "g" #'lsp-dart-pub-get ))))
(use-package flutter
  :after dart-mode
  :custom
  (flutter-sdk-path "~/dev/sdks/flutter"))

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

(require 'dap-node)

(use-package rjsx-mode
  :init
  (map! :map rjsx-mode-map
        (:localleader
         (:prefix ("n" . "node")
                    "b" #'nodejs-repl-send-buffer)
         (:prefix ("t" . "tide")
                    "f" #'tide-format
                    "r" #'tide-restart-server)
                   ))
  :config
  (setq js2-mode-show-strict-warnings t))

(setq prettier-js-args '(
                         "--trailing-comma" "all"
                         "--single-quote" "true"
                         "--jsx-single-quote" "true"
                         "--jsx-bracket-same-line" "false"
                         ))
