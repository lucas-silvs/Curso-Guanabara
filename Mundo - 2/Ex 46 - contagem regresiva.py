from time import sleep
for i in range(10,-1,-1):

    print(f"\033[0;34m{i}\033[m")
    sleep(1)

print('\033[0;33mBOOM!!!\033[0;33m')