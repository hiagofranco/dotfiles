# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias dir='dir --color=auto'
    alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

alias ll='exa --icons -l -g -B'
alias la='exa --icons -l -g -B -a'
alias ls='exa --icons'
alias tree='exa --icons -T'
alias fd='fdfind'
alias vim='nvim'
alias vi='nvim'
