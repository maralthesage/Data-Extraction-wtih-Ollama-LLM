
import pandas as pd
from values import *
import re
from glob import glob

val = Values()
warengr = val.wr_gr
file = val.wr_name
parent_dir = ''

_grosse_codes = pd.read_excel(val.groesse_codes)
_farbe_codes = pd.read_excel(val.farbe_codes)

grosse_codes = _grosse_codes[['SIZE_KEY','SIZE_NAME']].astype(str).set_index('SIZE_KEY').to_dict()
farbe_codes = _farbe_codes[['FARBE_KEY','FARBE_NAME']].astype(str).set_index('FARBE_KEY').to_dict()
grosse_codes = grosse_codes['SIZE_NAME']
farbe_codes = farbe_codes['FARBE_NAME']
farbe_codes['NA'] = 'Navy'
farbe_codes['nan'] = ''

marlon_dir = ''
for i in range(1300,1316):

    file = glob(f'{parent_dir}{i}/*_{i}.csv')
    endlist = glob(f'{parent_dir}{i}/{i}_*_endlist.csv')
    print(file[0])
    exported_csv = pd.read_csv(file[0],delimiter=';',encoding='utf-8')
    ma_list = pd.read_csv(val.marketing_artikel,delimiter=';',encoding='latin-1')


    ma_list = ma_list[ma_list['WM'].isna()]
    ma_list = ma_list[['WM','NUMMER','GROESSE','FARBE']]
    ma_list = ma_list.drop_duplicates()


    wr_list = pd.merge(ma_list,exported_csv,how='right',on='NUMMER')

    wr_list['FARBENWERT'] = wr_list['FARBE'].astype(str).map(farbe_codes)
    # wr_list = wr_list.rename(columns={"FARBE_x":"FARBE"})
    wr_list['GROESSENWERT'] = wr_list['GROESSE'].astype(str).map(grosse_codes)


    wr_list = wr_list.drop_duplicates(subset=['NUMMER','GROESSE','FARBE'])

    wr_list = wr_list.replace(r'\[|\]|\"|\{|\}',"",regex=True)
    wr_list = wr_list.replace(r"\'","",regex=True)
    wr_list = wr_list.replace("<Keine Größen>","")


    wr_list.drop_duplicates(subset='NUMMER')
    wr_list = wr_list.replace(r'Unbekannt|keine Angabe|Nicht angegeben|N/A|Nicht explizit erwähnt|Ohne Angabe','',regex=True)

    wr_list.to_csv(endlist[0],index=False,encoding='utf-8',sep=';')
    filename = endlist[0].split('/')[-1]
    wr_list.to_csv(f'{marlon_dir}{filename}',index=False,encoding='utf-8',sep=';')
