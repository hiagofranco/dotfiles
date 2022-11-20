
# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Use tmux as the default terminal
[[ -z "$TMUX" ]] && exec tmux

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Add .local to PATH
export PATH="$PATH:/home/hiago/.local/bin"

ZSH_THEME="aussiegeek-custom"

plugins=(git colored-man-pages zsh-autosuggestions zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

alias vi="nvim"
alias vim="nvim"
alias cat="bat"

# Enable colors for vim theme
source "$HOME/.vim/plugged/gruvbox/gruvbox_256palette.sh"
