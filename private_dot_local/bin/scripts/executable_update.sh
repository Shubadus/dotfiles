#!/usr/bin/env bash
echo "Updating Arch Packages"
sudo pacman -Syu --noconfirm

echo "Updating Flatpak Packages"
flatpak update -y

echo "Updating AUR Packages"
yay -Syu --noconfirm
