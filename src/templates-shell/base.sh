#!/bin/bash

echo "updating system"

sudo pacman -Syu --noconfirm

echo "installing git vs code base-devel and fastfetch"

sudo pacman -S git code base-devel fastfetch --noconfirm

echo "installing yay"

git clone https://aur.archlinux.org/yay.git

cd yay

makepkg -si --noconfirm
cd ..
