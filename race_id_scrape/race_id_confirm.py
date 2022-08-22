import pandas as pd

# main実行
if __name__ == '__main__':
    # DataFrame方でデータが抽出される
    race_id_data = pd.read_pickle("race_id_list.pickle")

    # race_id_dataをリストに格納
    race_id_list = []
    for i in race_id_data["race_id"]:
        race_id_list.append(i)

    print(race_id_list)
