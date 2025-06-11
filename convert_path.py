def main():
    # 1. 輸入轉換模式
    mode_choice = input("請選擇轉換模式：\n1. Mac路徑轉Windows路徑\n2. Windows路徑轉Mac路徑\n請輸入1或2：")
    # Mac to Windows
    if mode_choice == '1': 
        ori_path = input("請輸入欲轉換的Mac資料夾路徑：\n")
        # 2. 將/轉換成\
        converted_path = ori_path.replace("/", "\\")
        print("\n<new>轉換後的 Windows 路徑：")
        print(converted_path)
    # Windows to Mac
    else:
        ori_path = input("請輸入欲轉換的Windows資料夾路徑：\n")
        # 2. 將\轉換成/
        converted_path = ori_path.replace("\\", "/")
        print("\n<new>轉換後的 Mac 路徑：")
        print(converted_path)    

if __name__ == "__main__":
    main()