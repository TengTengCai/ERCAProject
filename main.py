# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from paddlenlp import Taskflow

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    # senta = Taskflow("sentiment_analysis", model="skep_ernie_1.0_large_ch")
    schema = [{"评价维度": ["观点词", "情感倾向[正向,负向,未提及]"]}]
    senta1 = Taskflow("sentiment_analysis", model="uie-senta-base", schema=schema)
    senta2 = Taskflow("sentiment_analysis", model="skep_ernie_1.0_large_ch")
    result1 = senta1("这东西甚至很有磁性，所以你可以把它放在冰箱上，而不是埋在抽屉里。超级实用和出色的设计。 值得所有的便士。")
    result2 = senta2("这东西甚至很有磁性，所以你可以把它放在冰箱上，而不是埋在抽屉里。超级实用和出色的设计。 值得所有的便士。")
    print(result1)
    print(result2)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
