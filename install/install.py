# Install packages
def install():
    !pip3 install findspark
    !pip3 install py4j
    !pip3 install pyspark
    !pip3 install pyarrow
    !pip3 install fastparquet
    return print('installed')

install()