import subprocess
import os
import sys


def rmtree(path):
    try:
        hdfs = os.environ['HADOOP_HOME'] + '/bin/hdfs'
        subprocess.call([hdfs, "dfs", "-rm", "-R", "-f", "-skipTrash", path])
    except:
        print("Unexpected error:", sys.exc_info()[0])
        pass


def isdir(path):
    try:
        hdfs = os.environ['HADOOP_HOME'] + '/bin/hdfs'
        r = subprocess.call([hdfs, "dfs", "-test", "-d", path])
        return r == 0
    except:
        print("Unexpected error:", sys.exc_info()[0])
        pass