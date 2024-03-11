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
# Path to Nvim, local/bin and cargo/bin
export PATH="$PATH:/opt/nvim-linux64/bin:$HOME/.local/bin:$HOME/.cargo/bin"

ZSH_THEME="powerlevel10k/powerlevel10k"

# Add wisely, as too many plugins slow down shell startup.
plugins=(
  colored-man-pages
  gitfast
  zsh-autosuggestions
  zsh-fzf-history-search
  z
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
