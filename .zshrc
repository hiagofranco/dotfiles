# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

### THEME ### Commented because of starship theme
#ZSH_THEME="robbyrussell"

### PLUGINS ###
plugins=(git colored-man-pages command-not-found docker pip python ubuntu zsh-autosuggestions)

source $ZSH/oh-my-zsh.sh

### Aliases ###
alias aptinstall="sudo apt install"
alias aptupdate="sudo apt-get update"
alias aptupgrade="sudo apt-get upgrade"
alias aptautoremove="sudo apt-get autoremove"
alias aptautoclean="sudo apt-get autoclean"
alias vi="nvim"
alias vim="nvim"

### Enable ZSH syntaz highlighting ###
source /home/hiago/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

### Enable starship theme ###
eval "$(starship init zsh)"
