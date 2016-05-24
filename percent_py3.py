#用于显示百分比的进度条
import sys
from time import sleep
def view_bar(i):
    output = sys.stdout
    for count in range(0, i+1):
        second = 0.1
        sleep(second)
        output.write('\rcomplete percent:%.0f%%' % count)
    output.flush()

view_bar(100)
