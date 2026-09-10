# a2bot_learning




## Install SSH on your laptop first

Before you try to connect, make sure the SSH client is installed on your Ubuntu laptop.

```bash
sudo apt update
sudo apt install openssh-client
```

Once it is installed, confirm the client is available:

```bash
ssh -V
```

If that prints a version string, you're all set.

## Install and configure Cyclone DDS

ROS2 can run on several different DDS implementations underneath, and two machines must use the *same* one to discover each other reliably. Cyclone DDS is used here because it is what the robots themselves are already configured with — a mismatched RMW implementation between a laptop and a robot is a real, silent cause of "why can't I see any topics" that matches no error message.

### 💻 Laptop

Install:
```bash
sudo apt install ros-humble-rmw-cyclonedds-cpp
```

Set as the active RMW (added to `~/.bashrc` so it persists):
```bash
echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc
source ~/.bashrc
```

Verify it's active:
```bash
echo $RMW_IMPLEMENTATION
ros2 pkg list | grep cyclonedds
```

> ⚠️ **Must match the robot exactly**
> This has to be installed and set **identically** on both machines, or discovery between them can fail even when `ROS_DOMAIN_ID` matches. If you built the Pi yourself in Setup 1, you already did this there; if you're joining an existing robot, it's already done on the Pi's side.
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


