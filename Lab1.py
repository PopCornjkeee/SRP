# -*- coding: utf-8 -*-

import urllib2
import datetime
import pandas as pd
import os
import matplotlib.pyplot as plt
import json

def download(region):
    if 1 <= region <= 27:
        if 1 <= region <= 9:
            region = '0' + str(region)
        url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID="+str(region)+"&year1=1981&year2=2017&type=Mean"
        name = str(region) + '_' + str(datetime.datetime.now()).replace(':', '-').replace(' ', '_')
        name = name[:-10]
        out = open('vhi_r' + name + '.csv', 'wb')
        out.write(urllib2.urlopen(url).read())
		
        out.close()
        print("VHI is downloaded...")
    else:
        print("Wrong region number!")

def opn(path):
    all_files = []
    for file_name in os.listdir(path):
        df = pd.read_csv(path + '/' + file_name, index_col=False, header=1,skip_footer=0,names=['year1','week1','SMN1','SMT','VCI','TCI','VHI'])
        df['week']=df['year1'].str.split(' ').str.get(1)
        df['year']=df['year1'].str.split(' ').str.get(0)
        df['SMN']=df['year1'].str.split('  ').str.get(1)
        df['VHI']=df['VCI']
        df['TCI']=df['SMT']
        df['VCI']=df['SMN1']
        df['SMT']=df['week1']
        del df['year1']
        del df['week1']
        del df['SMN1']
        df.insert(0, 'region', file_name[5:7])
        all_files.append(df)
    df1 = pd.concat(all_files)
    df1.index = range(len(df1.index))
    print list(df1.columns.values)
    print df1[:7000]
    return df1

def change_reg(df1):
    n = 0
    for value in df1['region']:
        if value == '01': df1.set_value(n, 'region', 'Вінницька')
        if value == '02': df1.set_value(n, 'region', 'Волинська')
        if value == '03': df1.set_value(n, 'region', 'Дніпропетровська')
        if value == '04': df1.set_value(n, 'region', 'Донецька')
        if value == '05': df1.set_value(n, 'region', 'Житомирська')
        if value == '06': df1.set_value(n, 'region', 'Закарпатська')
        if value == '07': df1.set_value(n, 'region', 'Запорізька')
        if value == '08': df1.set_value(n, 'region', 'Івано-Франківська')
        if value == '09': df1.set_value(n, 'region', 'Київська')
        if value == '10': df1.set_value(n, 'region', 'Кіровоградська')
        if value == '11': df1.set_value(n, 'region', 'Луганська')
        if value == '12': df1.set_value(n, 'region', 'Львівська')
        if value == '13': df1.set_value(n, 'region', 'Миколаївська')
        if value == '14': df1.set_value(n, 'region', 'Одеська')
        if value == '15': df1.set_value(n, 'region', 'Полтавська')
        if value == '16': df1.set_value(n, 'region', 'Рівненська')
        if value == '17': df1.set_value(n, 'region', 'Сумська')
        if value == '18': df1.set_value(n, 'region', 'Тернопільська')
        if value == '19': df1.set_value(n, 'region', 'Харківська')
        if value == '20': df1.set_value(n, 'region', 'Херсонська')
        if value == '21': df1.set_value(n, 'region', 'Хмельницька')
        if value == '22': df1.set_value(n, 'region', 'Черкаська')
        if value == '23': df1.set_value(n, 'region', 'Чернівецька')
        if value == '24': df1.set_value(n, 'region', 'Чернігівська')
        if value == '25': df1.set_value(n, 'region', 'Республіка Крим')
        n += 1
    return df1

def get_vhi(df1,year,region):
    df2 = df1[(df1['year'] == year) & (df1['region'] == region)]
    print list(df2.columns.values)
    print df2[:2000]

def get_vhi15(df1,year):
    df2 = df1[(df1['year'] == year) & (df1['VHI']<15)]
    print list(df2.columns.values)
    print df2[:2000]

def save_df(df1):
	df1.to_csv('data.csv')

get_vhi15(change_reg(opn("E:\lab\Lab1\Data")),'2000')