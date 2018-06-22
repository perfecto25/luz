import os
def get_dir_size(path=os.getcwd()):
    
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):

        dirsize = 0
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                size = os.path.getsize(fp)
            except OSError:
                pass
            #print("{0} {1}").format(size, fp)
            #print(dirpath, dirnames, filenames,size)
            dirsize += size
            total_size += size
        print(dirsize, dirpath)
    print("{0} bytes".format(total_size))
    print("{:,} KB").format(total_size/1000)
    print("{:,} MB").format(total_size/1000000)
    print("{:,} GB").format(total_size/1000000000)
print get_dir_size('/home/mrx')