
# Hiago's dotfiles for Neovim and ZSH #

![screenshot](https://github.com/hiagofranco/dotfiles/blob/master/images/screenshot.png?raw=true)

*Note: Install NeoVIM from its [Github](https://github.com/neovim/neovim/wiki/Installing-Neovim) page. Don't use APT or it will install an outdated version. Use this dotfile at your own risk!*

## Contents ##

* VIM ([NeoVIM](https://neovim.io/))
  * Plugins are managed with [vim-plug](https://github.com/junegunn/vim-plug)
* ZSH
  * Using [oh-my-zsh](https://ohmyz.sh/)
* ZSH custom theme
  * Place the custom theme under `~/.oh_my_zsh/custom/theme`
* Gnome Terminal backgroud color:
  * #282828

## Dependencies ##

* Papirus-icon-theme

* Rofi

* ZSH:

```text
sudo apt install zsh
```

* [Oh-my-zsh](https://ohmyz.sh/):

```text
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

* Install [Vim-Plug](https://github.com/junegunn/vim-plug) for Neovim:

```text
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

* [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
* [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
* [Nerd Font](https://www.nerdfonts.com/) (I recommend RobotoMono Nerd Font)  
* Nodejs >= 12.12 (used by COC inside NeoVIM):  

```text
sudo su
curl -sL install-node.vercel.app/lts | bash 
```

* [Clang](https://clangd.llvm.org/) (Coc language server)
* Tmux
* Tmux Plugin Manager ([TPM](https://github.com/tmux-plugins/tpm))
* Tmux theme [Dracula](https://draculatheme.com/tmux)
* Xclip and Xsel for tmux and vim:

```text
sudo apt-get install xclip xsel
```

## Install ##

* Copy custom aussiegeek theme:

```text
cp aussiegeek-custom.zsh-theme ~/.oh-my-zsh/themes/aussiegeek-custom.zsh-theme
```

* Install tmux theme:

```text
tmux source ~/.tmux.conf
Then press "Ctrl-a + I" (capital i)
```

## Some References ##

* [Copy and Paste in Tmux](https://www.seanh.cc/2020/12/27/copy-and-paste-in-tmux/#:~:text=Triple-click%20the%20Left%20Mouse,to%20paste%20from%20the%20clipboard)
