## My configuration for Neovim, ZSH and Starship.   
Note: Don't foget to run PlugInstall to install ao NeoVim Plugins described on init.vim .
#### Dependencies:
* Oh-my-zsh:
```
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
* Install Plug for Neovim:
```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```
* zsh-autosuggestions  
* zsh-syntax-highlighting  
* Nerd Font (Choose whatever you like)  
* Nodejs >= 12.12 (used by COC inside Neovim):  
```
curl -sL install-node.vercel.app/lts | bash 
```
