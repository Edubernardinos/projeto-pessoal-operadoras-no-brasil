import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import scipy.stats as st
from matplotlib.patches import Rectangle
import math
import seaborn as sns




df = pd.read_csv('Anatel.csv',encoding='utf-8-sig',on_bad_lines='skip',sep=';')


df['SERVICO'].value_counts()
'''
Celular Pós-Pago     2665441
Banda Larga Fixa     1823744
Telefone Fixo        1219286
Celular Pré-Pago     1115677
TV por Assinatura     615994
'''


df['PRESTADORA'].value_counts().head()
df = df.query('PRESTADORA == "CLARO" | PRESTADORA == "VIVO" ')



del df['TIPO_ATENDIMENTO']

df = df.sort_values(by='DATA_ABERTURA')


df['DATA_ABERTURA'].dtypes
df['DATA_ABERTURA'] = pd.to_datetime(df['DATA_ABERTURA'])
df['ANO'] = pd.DatetimeIndex(df['DATA_ABERTURA']).year
df['MES'] = pd.DatetimeIndex(df['DATA_ABERTURA']).month
df = df[(df['ANO'] > 2019) & (df['ANO'] < 2023)]

df_vivo = df[df['PRESTADORA'] == 'VIVO']
df_claro = df[df['PRESTADORA'] == 'CLARO']


df_vivo = df_vivo.groupby('ANO')['PRESTADORA'].value_counts()
df_claro = df_claro.groupby('ANO')['PRESTADORA'].value_counts()

df_claro = pd.DataFrame(df_claro)
df_vivo = pd.DataFrame(df_vivo)

df_claro = df_claro.rename(columns={'PRESTADORA':'CONTAGEM'})
df_vivo = df_vivo.rename(columns={'PRESTADORA':'CONTAGEM'})


df_claro.reset_index(inplace=True)
df_vivo.reset_index(inplace=True)




del df_claro['PRESTADORA']
del df_vivo['PRESTADORA']

df_claro
df_vivo

#PLOT

yticks = pd.Series([0,300000,600000,800000])
# criar figura e eixos

fig, ax = plt.subplots(figsize =(10,6))
# plotar gráfico para a operadora Vivo
ax.bar(df_vivo['ANO'] - 0.2, df_vivo['CONTAGEM'], width=0.4, align='center',color='#FFDAB9',label='Vivo')
sns.set_style('whitegrid')
# plotar gráfico para a operadora Claro
ax.bar(df_claro['ANO'] + 0.2, df_claro['CONTAGEM'], width=0.4, align='center', label='Claro',color='#FA8072')
# definir rótulos e título do gráfico
ax.set_xticks(df_vivo['ANO'])
ax.set_xticklabels(df_vivo['ANO'])
ax.set_xlabel('Ano')
ax.set_ylabel('')
ax.set_title('ANNUAL COMPLAINTS  BY TELECOMMUNICATIONS COMPANIES IN BRAZIL\n FROM 2020 TO 2022')

ax.set_yticks(yticks)
yticks2 = (yticks/1000).astype(int)
ax.set_yticklabels(pd.Series(yticks2).astype(str) + 'K')
yticks_temp = ax.get_yticklabels()
yticks_temp[0].set_text('0')
ax.set_yticklabels(yticks_temp)
ax.set_xlabel('')
# adicionar legenda
ax.legend()









