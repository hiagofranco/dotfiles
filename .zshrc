
# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Add PIP3 to PATH
export PATH="$PATH:/home/hiago/.local/bin"

### THEME ### Commented because of starship theme
ZSH_THEME="aussiegeek-custom"

### PLUGINS ###
plugins=(git colored-man-pages zsh-autosuggestions)

source $ZSH/oh-my-zsh.sh

### Aliases ###
alias aptinstall="sudo apt install"
alias aptremove="sudo apt remove"
alias aptupdate="sudo apt update"
alias aptupgrade="sudo apt upgrade"
alias aptautoremove="sudo apt autoremove"
alias aptautoclean="sudo apt autoclean"
alias vi="nvim"
alias vim="nvim"

### Enable ZSH syntaz highlighting ###
source /home/hiago/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

### Enable colors for vim theme
source "$HOME/.vim/plugged/gruvbox/gruvbox_256palette.sh"
