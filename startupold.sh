wget -O a.tar.gz https://kindle.s3.amazonaws.com/Kindle_src_5.8.1.0.1_2990510001.tar.gz
tar -xf a.tar.gz
mkdir toolchain
mv gplrelease/build_* toolchain/b.tar.gz
cd toolchain
tar -xvf b.tar.gz
rm b.tar.gz
cd ..
rm a.tar.gz