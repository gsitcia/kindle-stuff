mkdir -p ~/opt
git lfs pull
tar -C ~/opt -xf cross.tar.gz
tar -C ~/opt/cross-gcc-linaro/arm-linux-gnueabi/ -xf khdrs.tar.gz
touch ~/.bash_aliases
echo "alias kindle-gcc=~/opt/cross-gcc-linaro/bin/arm-linux-gnueabi-gcc" >> ~/.bash_aliases
source ~/.bashrc
# test