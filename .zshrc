# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Add PIP3 to PATH
export PATH="$PATH:/home/hiago/.local/bin"

### THEME ### Commented because of starship theme
ZSH_THEME="powerlevel10k/powerlevel10k"

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

source ~/gruvbox_256pallete.sh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
