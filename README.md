![screenshot](https://github.com/hiagofranco/dotfiles/blob/master/images/screenshot.png?raw=true)
# Hiago's dotfiles for Neovim and ZSH #

*Note: Install NeoVIM from its [Github](https://github.com/neovim/neovim/wiki/Installing-Neovim) page. Don't use APT or it will install an outdated version. Use this dotfile at your own risk!*

## Contents ##

* VIM ([NeoVIM](https://neovim.io/))
    + Plugins are managed with [vim-plug](https://github.com/junegunn/vim-plug)
* ZSH
    + Using [oh-my-zsh](https://ohmyz.sh/)
* ZSH custom theme
    + Place the custom theme under `~/.oh_my_zsh/custom/theme`
* Gnome Terminal backgroud color:
    + #282828
## Dependencies ##

* ZSH:
```
sudo apt install zsh
```
* [Oh-my-zsh](https://ohmyz.sh/):
```
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
* Install [Vim-Plug](https://github.com/junegunn/vim-plug) for Neovim:
```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```
* [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
* [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
* [Nerd Font](https://www.nerdfonts.com/) (I recommend RobotoMono Nerd Font)  
* Nodejs >= 12.12 (used by COC inside NeoVIM):  
```
sudo su
curl -sL install-node.vercel.app/lts | bash 
```
* [Clang](https://clangd.llvm.org/) (Coc language server)
* Tmux
* Tmux Plugin Manager ([TPM](https://github.com/tmux-plugins/tpm))
* Tmux theme [Dracula](https://draculatheme.com/tmux)

## Install ##
* Copy custom aussiegeek theme:
```
cp aussiegeek-custom.zsh-theme ~/.oh-my-zsh/themes/aussiegeek-custom.zsh-theme
```
* Install tmux theme:
```
tmux source ~/.tmux.conf
Then press "Ctrl-a + I" (capital i)
```
