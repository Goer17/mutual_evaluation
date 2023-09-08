import pandas as pd
import os

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

def main():
    N = 30 # 班级人数
    dic = 'mt_list/' # 表格目录
    excel_files = [f for f in os.listdir(dic) if f.endswith('.xlsx') or f.endswith('.xls') or f.endswith('.csv')]

    all_dat = pd.DataFrame()
    for file in excel_files:
        dat = pd.read_excel(dic + file, skiprows = [0, 1], nrows = N, usecols = range(8))
        all_dat = pd.concat([all_dat, dat])

    all_avg = all_dat.groupby(['学号', '姓名']).mean().sort_values('总分', ascending = False)
    all_avg.to_excel('result.xlsx')

if __name__ == '__main__':
    main()