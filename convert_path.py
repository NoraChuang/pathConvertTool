def main():
    # 1. 輸入路徑字串
    ori_path = input("請輸入欲轉換的Mac資料夾路徑：\n")

    # 2. 將/轉換成\
    converted_path = ori_path.replace("/", "\\")

    # 3. 輸出轉換後的路徑
    print("\n<new>轉換後的Windows路徑：")
    print(converted_path)


if __name__ == "__main__":
    main()