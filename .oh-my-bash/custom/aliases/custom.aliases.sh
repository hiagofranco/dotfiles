
# Add your own custom alias in the custom/aliases directory. Aliases placed
# here will override ones with the same name in the main alias directory.

alias ll='exa --icons -l -g -B'
alias la='exa --icons -l -g -B -a'
alias ls='exa --icons'
alias tree='exa --icons -T'
alias fd='fdfind'
alias vim='nvim'
alias vi='nvim'
alias vpn_br="sudo openfortivpn brvpn.int.toradex.com:10443 --username=hiago.franco"
alias vpn_ch="sudo openfortivpn chvpn.int.toradex.com:10443 --username=hiago.franco"
alias :q="exit"

bind -x '"\C-r":fuzzy_search_cmd'
bind -x '"\C-f":fuzzy_cd'

writecmd () { 
	perl -e 'ioctl STDOUT, 0x5412, $_ for split //, do{ chomp($_ = <>); $_ }'
}

fuzzy_search_cmd() {
	rg -v "^#" ~/.bash_history | fzf --reverse --height 40% +m --tac --no-sort -e | writecmd
}

fuzzy_cd() {
	local dir
	dir=$(fd --type d . | fzf --reverse --height 40% +m --tac)
	cd "$dir"
}

docker_yocto() {

	if ! mount | grep -q /media/hiago/data; then
		echo "ERROR: /media/hiago/data is not mounted."
		exit
	fi

	echo "Please select an option:"
	select d in $(find /media/hiago/data_ssd/yocto/ -maxdepth 1 -type d -iregex '.*bsp.*\|.*tc.*' -printf '%f\n')
	do
		test -n "$d" && break 
		echo ">>> Invalid Selection"
	done

	if [[ "$d" == *"2.8"* ]]; then
		docker run --rm -it --privileged -v /media/hiago/data_ssd/yocto/${d}/:/home/yocto/${d}/ -v /tmp:/tmp -v /etc/localtime:/etc/localtime --name yocto -e DISPLAY=$DISPLAY hiagofranco/yocto-builder-ubu16:latest
	else
		docker run --rm -it --privileged -v /media/hiago/data_ssd/yocto/${d}/:/home/yocto/${d}/ -v /tmp:/tmp -v /etc/localtime:/etc/localtime --name yocto -e DISPLAY=$DISPLAY hiagofranco/yocto-builder:latest
	fi

}

docker_android() {

	if ! mount | grep -q /media/hiago/data; then
		echo "ERROR: /media/hiago/data is not mounted."
		exit
	fi

	docker run --rm -it --privileged -v /media/hiago/data_ssd/android_nxp/:/home/android/android_nxp/ -v /tmp:/tmp -v /etc/localtime:/etc/localtime --name yocto -e DISPLAY=$DISPLAY hiagofranco/android-builder:latest

}

compiler64() {
	bat ~/workdir/toolchain/export_compiler64
	source ~/workdir/toolchain/export_compiler64
}

compiler32() {
	bat ~/workdir/toolchain/export_compiler32
	source ~/workdir/toolchain/export_compiler32
}

# Requires https://github.com/caarlos0/timer to be installed.
pomodoro() {
	declare -A pomo_options=( ["work"]="45" ["break"]="10" )

	if [ -n "$1" -a -n "${pomo_options["$1"]}" ]; then
		val=$1;
		echo $val | lolcat
		timer "${pomo_options["$val"]}m"
		notify-send "🍅 '$val' session done"
	fi
}

alias wo="pomodoro 'work'"
alias br="pomodoro 'break'"
