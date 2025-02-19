SPACECRAFT_DB = {
    "Rocket Lab Photon": 10000,
    "SpaceX Falcon 9": 5000,
    "Blue Origin New Shepard": 8000
}


def SPACECRAFT_COST():
    """获取用户选择的航天器型号"""
    while True:
        print("\n请选择航天器型号：")
        # 显示可选型号（自动适应数据库变化）
        for idx, name in enumerate(SPACECRAFT_DB.keys(), 1):
            print(f"{idx}. {name} (${SPACECRAFT_DB[name]}/天)")

        choice = input("输入编号或完整名称: ").strip()

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(SPACECRAFT_DB):
                return list(SPACECRAFT_DB.keys())[idx]

        # 处理名称输入（不区分大小写和空格）
        normalized_choice = choice.lower().replace(" ", "")
        for name in SPACECRAFT_DB:
            if normalized_choice == name.lower().replace(" ", ""):
                return name

        print("⚠️ 错误：无效的航天器型号，请重新输入！")


def get_hire_days():
    """获取租赁天数（1-30天）"""
    while True:
        try:
            days = int(input("\n请输入租赁天数 (1-30): "))
            if 1 <= days <= 30:
                return days
            print("⚠️ 错误：天数必须在1到30之间！")
        except ValueError:
            print("⚠️ 错误：请输入有效数字！")


def get_passenger_count():
    """获取乘客数量（0-10人）"""
    while True:
        try:
            count = int(input("\n请输入乘客数量 (0-10): "))
            if 0 <= count <= 10:
                return count
            print("⚠️ 错误：乘客数必须在0到10之间！")
        except ValueError:
            print("⚠️ 错误：请输入有效数字！")


def calculate_cost(model, days, has_pilot, passengers):
    """费用计算核心函数"""
    daily_rate = SPACECRAFT_DB[model]
    pilot_cost = 500 * days if has_pilot else 0
    passenger_cost = 500 * passengers * days
    total = (daily_rate * days) + pilot_cost + passenger_cost
    return total


def main():
    print("=" * 40)
    print("太空探险租赁计算器".center(40))
    print("=" * 40)

    spacecraft = SPACECRAFT_COST()

    #
    days = get_hire_days()

    pilot = input("\n是否需要飞行员？(Y/N): ").strip().lower()
    while pilot not in ["y", "n", "是", "否"]:
        print("⚠️ 错误：请输入 Y/N 或 是/否")
        pilot = input("是否需要飞行员？(Y/N): ").strip().lower()
    has_pilot = pilot in ["y", "是"]

    passengers = get_passenger_count()

    # 计算总费用
    total = calculate_cost(spacecraft, days, has_pilot, passengers)

    #
    print("\n" + "=" * 40)
    print("租赁收据".center(40))
    print("-" * 40)
    print(f"航天器型号: {spacecraft}")
    print(f"租赁天数: {days}天")
    print(f"乘客数量: {passengers}人")
    print(f"雇佣飞行员: {'是' if has_pilot else '否'}")
    print("-" * 40)
    print(f"总费用: ${total:,}")
    print("=" * 40)


if __name__ == "__main__":
    main()