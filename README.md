![screenshot](https://github.com/hiagofranco/dotfiles/blob/master/images/screenshot.png?raw=true)
# Hiago's dotfiles for Neovim and ZSH.
*Note: Install NeoVIM from its [Github](https://github.com/neovim/neovim/wiki/Installing-Neovim) page. Don't use APT or it will install an outdated version. Use this dotfile at your own risk!*

## Contents:
* VIM ([NeoVIM](https://neovim.io/))
    + Plugins are managed with [vim-plug](https://github.com/junegunn/vim-plug)
* ZSH
    + Using [oh-my-zsh](https://ohmyz.sh/)

## Plugins Used by NeoVIM:
* [Vim-Rainbown](https://github.com/frazrepo/vim-rainbow)
* [Lightline](https://github.com/itchyny/lightline.vim)
* [Barbar](https://github.com/romgrk/barbar.nvim)
* [FZF](https://github.com/junegunn/fzf.vim)
* [Python-syntax](https://github.com/vim-python/python-syntax)
* [COC](https://github.com/neoclide/coc.nvim)

## Dependencies:
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
curl -sL install-node.vercel.app/lts | bash 
```
