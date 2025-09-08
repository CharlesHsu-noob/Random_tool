import math
import psutil

def get_user_input(prompt, error_message, condition=lambda x: True):
    """取得使用者輸入，並確保符合條件"""
    while True:
        try:
            value = int(input(prompt))
            if condition(value):
                return value
            else:
                print("輸入值不符合條件！請重新輸入")
        except ValueError:
            print(error_message)

def generate_numbers(count, range_):
    """
    根據指定數量和範圍生成隨機數字
    參數:
        count (int): 生成數字的數量
        range_ (int): 數字範圍上限
    返回:
        list: 生成的數字列表
    """
    displayprint = []
    n = 0
    putintoans = 0
    for k in range(count):
        s1, s2, s3, s4 = psutil.cpu_stats()
        part = math.floor(s4 / 10) * 10
        d = s4 - part
        part = math.floor(s4 / 100) * 100
        c = (s4 - part - d) / 10
        part = math.floor(s4 / 1000) * 1000
        b = (s4 - part - 10 * c - d) / 100
        part = math.floor(s4 / 10000) * 10000
        a = (s4 - part - 100 * b - 10 * c - d) / 1000

        random_factor = d * c
        mode = (random_factor * 1000) % 10000

        if mode >= 100:
            mode = 0
        if d != 0:
            if mode % 4 == 0:
                mode += d
            elif mode % 4 == 1:
                mode += c
            elif mode % 4 == 2:
                mode += b
            elif mode % 4 == 3:
                mode += a
        else:
            if mode % 4 == 0:
                mode += 1
            elif mode % 4 == 1:
                mode += c
            elif mode % 4 == 2:
                mode += b
            elif mode % 4 == 3:
                mode += a

        # 計算 ans 的值
        if mode % 4 == 0:
            ans = 1000 * d + 100 * b + 10 * c + a
        elif mode % 4 == 2:
            ans = 1000 * a + 100 * d + 10 * b + c
        elif mode % 4 == 1:
            ans = 1000 * c + 100 * a + 10 * d + b
        elif mode % 4 == 3:
            ans = 1000 * b + 100 * c + 10 * a + d

        ans = round(ans % range_)
        putintoans += 1

        if n > 500:
            n = 0
        n += d
        if putintoans % 2 == 1:  # 奇數次的時候插入
            if n % 2 == 1:
                displayprint.insert(1, ans)
            else:
                displayprint.insert(n, ans)
    return displayprint

def display_numbers(numbers, mode):
    """
    根據指定的顯示模式輸出數字
    參數:
        numbers (list): 要顯示的數字列表
        mode (int): 顯示模式，1 為列表顯示，2 為逐行顯示
    """
    if mode == 1:
        print(numbers)
    elif mode == 2:
        for num in numbers:
            print(num)

def main():
    print("按 Ctrl+C 結束程式\n亂輸入會 crash")

    # 輸入生成數字的個數
    count = get_user_input('請問要生成幾個數: ', '輸入的不是整數！請重新輸入', lambda x: x > 0) * 2

    # 輸入範圍
    range_ = get_user_input('範圍(最大9999)= ', '輸入的不是整數！請重新輸入')
    if range_ >= 10000:
        print("範圍過大！自動設為9999")
        range_ = 9999

    # 輸入顯示模式
    print("1:[a,b,c,d...]\n2:a\n  b\n  c\n  d...")
    display_mode = get_user_input('請輸入顯示模式: ', '輸入的不是整數！請重新輸入', lambda x: x in [1, 2])

    # 生成數字
    numbers = generate_numbers(count, range_)

    # 顯示結果
    display_numbers(numbers, display_mode)

# 如果是主程式才執行 main()，被 import 時不會執行
if __name__ == "__main__":
    main()
