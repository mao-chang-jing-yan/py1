# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time

def decrator(*dargs, **dkargs):
  def wrapper(func):
    def _wrapper(*args, **kargs):
      print ("装饰器参数:", dargs, dkargs)
      print ("函数参数:", args, kargs)
      return func(*args, **kargs)
    return _wrapper
  return wrapper

def decrator_1(func):
  def wrap(*args, **kwargs):
    start_time = time.time()
    res = func(*args, **kwargs)
    end_time = time.time()
    print('运行时间为', end_time-start_time)
    return res
  return wrap


@decrator_1
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

