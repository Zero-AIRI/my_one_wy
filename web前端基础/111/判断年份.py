def is_leap_year(year):
    # 判断是否为闰年
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        # 输入年份
        year = int(input("请输入一个年份: "))
        
        # 判断并输出结果
        if is_leap_year(year):
            print(f"{year} 是闰年")
        else:
            print(f"{year} 不是闰年")
    except ValueError:
        print("输入无效，请输入一个有效的年份")

if __name__ == "__main__":
    main()
