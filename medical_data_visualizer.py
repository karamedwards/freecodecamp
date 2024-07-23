import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = 0
df.loc[(df['weight']/np.square(df['height']/100))>25,'overweight'] = 1

# 3
#normalize choloesterol and glucose values: if value = 1 set to 0. if value > 1 set to 1
df.loc[df['cholesterol']==1, 'cholesterol'] = 0
df.loc[df['gluc']==1, 'gluc'] = 0

df.loc[df['cholesterol']>1, 'cholesterol'] = 1
df.loc[df['gluc']>1, 'gluc'] = 1

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    

    # 7
    df_cat = df_cat.rename(columns={0: 'total'})

    # 8
    fig = sns.catplot(data=df_cat,
            kind="bar",
            x="variable",
            y="total",
            hue="value",
            col="cardio")


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo']<=df['ap_hi']) &
                     (df['height']>=df['height'].quantile(0.025)) &
                     (df['height']<=df['height'].quantile(0.975)) &
                     (df['weight']>=df['weight'].quantile(0.025)) &
                     (df['weight']<=df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True


    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, annot=True, fmt=".1f", mask=mask)


    # 16
    fig.savefig('heatmap.png')
    return fig
