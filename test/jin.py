# import time
#
# start = time.time()
# for i in range(0, 5 * 10000 * 1000 + 1):
#     # print("\r2123323")
#     print("2123323\r", 100 * i / (5 * 10000 * 1000), "%", int(10 * i / (5 * 10000 * 1000)) * "==>>",
#           end="")
#
#     # print("\n", i, end="\n\n")
# end = time.time()
# print("\n用时", end - start)

import time

for i in range(100):
    time.sleep(0.5)
    slist = ["\\", "|", "/", "-"]
    print('\r' + '程序正在运行：' + slist[i % 4], end="")
