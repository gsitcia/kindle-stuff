wget -O a.tar.gz https://s3.amazonaws.com/kindledownloads/Kindle_src_5.8.9_3164600017.tar.gz
tar -xf a.tar.gz
mkdir toolchain
mv gplrelease/build_* toolchain/b.tar.gz
cd toolchain
tar -xvf b.tar.gz
rm b.tar.gz
cd ..
rm -rf gplrelease
rm a.tar.gz
