
# Hiago's dotfiles #

![screenshot](https://github.com/hiagofranco/dotfiles/blob/master/images/screenshot.png?raw=true)

## Contents ##

* Neovim
  * Plugins are managed with [vim-plug](https://github.com/junegunn/vim-plug)
  *Note: Install NeoVIM from its [Github](https://github.com/neovim/neovim/wiki/Installing-Neovim) page. Don't use APT or it will install an outdated version.
* Zsh
* [Oh-my-zsh](https://ohmyz.sh/):
  * [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
  * [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
* [Nerd Font](https://www.nerdfonts.com/) (I recommend RobotoMono Nerd Font)  
* Nodejs >= 12.12 (used by COC inside NeoVIM):

```bash
sudo su
curl -sL install-node.vercel.app/lts | bash 
```

* Tmux
* Tmux Plugin Manager ([TPM](https://github.com/tmux-plugins/tpm))
* Rofi
* Ranger
* Picom
* Alacritty
  * `cargo install alacritty`
* [Qtile](http://docs.qtile.org/en/stable/)
* [Qtile Extras](https://qtile-extras.readthedocs.io/en/stable/)
* Betterscreenlock
* ZSH custom theme
  * Place the custom theme under `~/.oh_my_zsh/custom/theme`
* [Clang](https://clangd.llvm.org/) (Coc language server)
* Xclip and Xsel for tmux and vim
  * `sudo apt-get install xclip xsel`
* BAT
  * `cargo install bat`
* EXA
  * `sudo apt install exa`
* Qtile widget dependencies:
  * `pip install dbus-next`
  * `sudo apt install libghc-iwlib-dev`
  * `pip install iwlib`
  * `pip install psutil`
  * `sudo apt install brightnessctl`
  * `sudo apt install playerctl`
  * `sudo apt install shutter`
* xcp
  * `cargo install xcp`

## Install ##

* Copy custom aussiegeek theme:

```bash
cp aussiegeek-custom.zsh-theme ~/.oh-my-zsh/themes/aussiegeek-custom.zsh-theme
```

* Install tmux theme:

```bash
tmux source ~/.tmux.conf
Then press "Ctrl-a + I" (capital i)
```

## Some References ##

* [Copy and Paste in Tmux](https://www.seanh.cc/2020/12/27/copy-and-paste-in-tmux/#:~:text=Triple-click%20the%20Left%20Mouse,to%20paste%20from%20the%20clipboard)
