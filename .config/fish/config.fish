function fish_greeting
  neofetch
end

starship init fish | source

set -x ANDROID_HOME $HOME/Android/Sdk
set -x DOCKER_HOST unix:///run/user/1000/docker.sock
set -x CHROME_EXECUTABLE google-chrome-stable
set -Ux JAVA_OPTS '' #'-XX:+IgnoreUnrecognizedVMOptions --add-modules java.se.ee'
set -Ux JAVA_HOME /usr/lib/jvm/java-16-jdk
set -Ux ANDROID_SDK_ROOT /opt/android-sdk

set EDITOR emacs

alias vim emacs
alias nvim emacs
alias vi emacs

alias efshc "$EDITOR $HOME/.config/fish/config.fish"
alias efsha "$EDITOR $IMPORT_LOC/aliases.fish"

alias envmc "$EDITOR $HOME/.config/nvim/init.vim"

alias cdt "cd /tmp"
alias cdc "cd $HOME/.config"
alias cdd "cd $HOME/dev/"
alias cds "cd $HOME/dev/src"
alias cdfi "cd $IMPORT_LOC"

alias dfg "/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME"

alias uwu "sudo apt update && sudo apt upgrade"
alias e. "nautilus ."
alias c. "emacs ."
alias doom "~/.emacs.d/bin/doom"
