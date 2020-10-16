import pandas as pd

print ("启动程序")
print ("-"*30)

game_store = pd.read_excel(r'gsc.xlsx')
edo = pd.read_excel(r'jianghu.xlsx')
dct = pd.read_excel(r'Dreamcity.xlsx')
ct_master = pd.read_excel(r'city_master.xlsx')
street = pd.read_excel(r'street.xlsx')
b_a = pd.read_excel(r"Basketball_architecture.xlsx")
b_p = pd.read_excel(r"Basketball_player.xlsx")


print ("载入数据成功")
print ("-"*30)

while True:
    game_type = input(" 选择正在玩的开罗游戏 (输入前面的数字） \n"
                      "1. 游戏城物语 \n"
                      "2. 大江户物语 \n"
                      "3. 箱庭都市 \n"
                      "4. 都市大亨物语 \n"
                      "5. 商店街物语 \n"
                      "6. 篮球热潮物语 \n")

    if game_type == "1":
        dataset = game_store
    elif game_type == "2":
        dataset = edo
    elif game_type == '3':
        dataset = dct
    elif game_type == "4":
        dataset = ct_master
    elif game_type == "5":
    	dataset = street
    elif game_type == '6':

        basketball_database_selection = input(" 选择要搜索的数据 (数字) \n"
            "1. 建筑组合 \n"
            "2. 球员训练相性 \n")

        if basketball_database_selection == "1":
            dataset = b_a
        else:
            dataset = b_p

    df = pd.DataFrame(dataset).astype(str)

    shape = df.shape
    indexes = shape[1]

    zone = str(input("搜索关键词 \n"
                     "1.切换游戏 \n"))

    if zone == str("1"):
        continue

    for index in range(indexes):

        sb1 = (df[df.iloc[:, index].str.match(zone, na=False)])
        index += 1

        print(sb1)
