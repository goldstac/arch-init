#!/bin/bash

echo "updating system"

sudo pacman -Syu

echo "installing git vs code base-devel and fastfetch"

sudo pacman -S git code base-devel fastfetch

echo "installing yay"

git clone https://github.com/Jguer/yay.git

cd yay

makepkg -si

echo "installing cursor"

yay -S cursor-bin
