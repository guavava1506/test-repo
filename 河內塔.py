def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"將盤子 1 從 {source} 移到 {target}")
        return
    hanoi(n - 1, source, target, auxiliary)
    print(f"將盤子 {n} 從 {source} 移到 {target}")
    hanoi(n - 1, auxiliary, source, target)


if __name__ == "__main__":
    n = int(input("請輸入盤子數量: "))
    hanoi(n, "A", "B", "C")
