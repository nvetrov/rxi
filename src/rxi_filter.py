import pandas
import json

with open('config.json', 'r') as conf:
    config = json.loads(conf.read())

df = pandas.read_excel(config['rxi_file'], sheet_name='01 счет',
                       usecols=['Категория актива', 'Расположение', 'Номер актива', 'Описание актива'])
filtered_df = df[(df['Категория актива'].isin(config['rxi_category'])) & (df['Расположение'].isin(config['mag_place']))]

mag_number = config['mag_place'][0][-10:-7]

writer = pandas.ExcelWriter(f"{mag_number}_rxi.xlsx", engine='xlsxwriter')
filtered_df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()
