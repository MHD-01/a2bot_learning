# a2bot_learning





### Installing Terminator
 
```bash
sudo apt install terminator
```


### Installing VS Code
 
```bash
sudo apt update
sudo apt install software-properties-common apt-transport-https wget -y
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code -y
```
 



### Installing the Remote-SSH extension
 
Open VS Code, go to the Extensions panel (`Ctrl+Shift+X`), search **"Remote
- SSH"**, and click Install — or from a terminal:
```bash
code --install-extension ms-vscode-remote.remote-ssh
```


