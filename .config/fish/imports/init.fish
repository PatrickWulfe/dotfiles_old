# Init pywal theme
#wal -Rq

# Set greeting
function fish_greeting
  neofetch
end

# Init theme
starship init fish | source

# Set defaults
set EDITOR nvim

# Init java
set -Ux JAVA_OPTS '' #'-XX:+IgnoreUnrecognizedVMOptions --add-modules java.se.ee'
set -Ux JAVA_HOME /usr/lib/jvm/java-16-jdk
set -Ux ANDROID_SDK_ROOT /opt/android-sdk


