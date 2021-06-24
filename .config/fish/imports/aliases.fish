alias vim emacs
alias nvim emacs
alias vi emacs

# edit fish configs
alias efshc "$EDITOR $HOME/.config/fish/config.fish"
alias efsha "$EDITOR $IMPORT_LOC/aliases.fish"

# edit other configs
alias envmc "$EDITOR $HOME/.config/nvim/init.vim"

# cd aliases
alias cdt "cd /tmp"
alias cdc "cd $HOME/.config"
alias cdd "cd $HOME/dev/"
alias cds "cd $HOME/dev/src"
alias cdfi "cd $IMPORT_LOC"
alias doom "~/.emacs.d/bin/doom"

# for dotfiles
alias dfg "/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME"

# Utility stuff
alias uwu "sudo apt update && sudo apt upgrade"
alias e. "nautilus ."
alias c. "code ."
alias studio "~/.local/android-studio/bin/studio.sh"
