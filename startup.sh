wget -O a.tar.gz https://kindle.s3.amazonaws.com/Kindle_src_5.8.1_2974910023.tar.gz
tar -xf a.tar.gz
mkdir toolchain
mv gplrelease/build_* toolchain/b.tar.gz
cd toolchain
tar -xf b.tar.gz
rm b.tar.g
cd ..
rm -rf gplrelease
rm a.tar.gz


