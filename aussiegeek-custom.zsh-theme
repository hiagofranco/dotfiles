
PROMPT='$fg_bold[green][$FG[161]%t$fg_bold[green] ]$fg_bold[green][$FG[161]%n@%m:$fg_bold[blue]%~$(git_prompt_info)$fg[yellow]$(ruby_prompt_info)$fg_bold[green]]$reset_color
> '
# git theming
ZSH_THEME_GIT_PROMPT_PREFIX="$fg_bold[yellow] <"
ZSH_THEME_GIT_PROMPT_SUFFIX="$fg_bold[yellow]>"
ZSH_THEME_GIT_PROMPT_CLEAN="$fg_bold[green]✔"
ZSH_THEME_GIT_PROMPT_DIRTY="$fg_bold[red]✗"
