# execute sway automatically
if [ -z "${WAYLAND_DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
  exec sway
fi

# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Launch Tmux
if command -v tmux &> /dev/null && [ -n "$PS1" ] && [[ ! "$TERM" =~ screen ]] && [[ ! "$TERM" =~ tmux ]] && [ -z "$TMUX" ]; then
  exec tmux
fi

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Path to Nvim, local/bin and cargo
export PATH="$PATH:/opt/nvim-linux64/bin:$HOME/.local/bin:$HOME/.cargo/bin"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="powerlevel10k/powerlevel10k"

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
  colored-man-pages
  gitfast
  zsh-autosuggestions
  zsh-fzf-history-search
  zsh-syntax-highlighting
)

# zsh-fzf-history-search flags (see https://github.com/joshskidmore/zsh-fzf-history-search)
ZSH_FZF_HISTORY_SEARCH_FZF_EXTRA_ARGS="--height 40% --reverse"
ZSH_FZF_HISTORY_SEARCH_END_OF_LINE="true"
ZSH_FZF_HISTORY_SEARCH_EVENT_NUMBERS=0
ZSH_FZF_HISTORY_SEARCH_DATES_IN_SEARCH=0
ZSH_FZF_HISTORY_SEARCH_REMOVE_DUPLICATES="true"

source $ZSH/oh-my-zsh.sh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

eval "$(zoxide init zsh)"
