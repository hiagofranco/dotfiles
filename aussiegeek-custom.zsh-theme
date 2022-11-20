
PROMPT='$fg_bold[red][$fg_bold[yellow]%n$fg_bold[green]@$fg[blue]%m $fg_bold[red]%~$(git_prompt_info)$fg[yellow]$(ruby_prompt_info)$fg_bold[red]]$reset_color
$ '
# git theming
ZSH_THEME_GIT_PROMPT_PREFIX="$fg_bold[yellow] <"
ZSH_THEME_GIT_PROMPT_SUFFIX="$fg_bold[yellow]>"
ZSH_THEME_GIT_PROMPT_CLEAN="$fg_bold[green]✔"
ZSH_THEME_GIT_PROMPT_DIRTY="$fg_bold[red]\u00b1"
