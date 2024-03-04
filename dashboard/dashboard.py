import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def plot_pm25(full_data):
    pm25 = full_data.groupby(by='station').agg({"PM2.5":'mean'}).sort_values(by='PM2.5', ascending=False).reset_index()
    colors = ["#408ABF", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#408ABF"]

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='PM2.5', y='station', data=pm25, palette=colors, ax=ax)
    ax.set_title("Rata-rata tingkat polutan PM2.5", loc="center", fontsize=15)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=12)
    st.pyplot(fig)

def plot_correlation(tab, full_data):
    fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(30,15))
    colors = ["#408ABF", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#408ABF"]

    if tab == "NO2":
        sns.scatterplot(x='NO2', y='PM2.5', data=full_data, palette=colors, ax=ax[0][0], s=10)
        ax[0][0].set_title("Polutan PM2.5", loc="center", fontsize=15)

        sns.scatterplot(x='NO2', y='PM10', data=full_data, palette=colors, ax=ax[0][1], s=10)
        ax[0][1].set_title("Polutan PM10", loc="center", fontsize=15)
        
        sns.scatterplot(x='NO2', y='SO2', data=full_data, palette=colors, ax=ax[0][2], s=10)
        ax[0][2].set_title("Polutan SO2", loc="center", fontsize=15)
        
        sns.scatterplot(x='NO2', y='NO2', data=full_data, palette=colors, ax=ax[1][0], s=10)
        ax[1][0].set_title("Polutan NO2", loc="center", fontsize=15)
        
        sns.scatterplot(x='NO2', y='O3', data=full_data, palette=colors, ax=ax[1][1], s=10)
        ax[1][1].set_title("Polutan O3", loc="center", fontsize=15)

        sns.scatterplot(x='NO2', y='CO', data=full_data, palette=colors, ax=ax[1][2], s=10)
        ax[1][2].set_title("Polutan CO", loc="center", fontsize=15)

        plt.suptitle("Korelasi Polutan NO2 Dengan Polutan Lain", fontsize=30)

    elif tab == "CO":
        sns.scatterplot(x='CO', y='PM2.5', data=full_data, palette=colors, ax=ax[0][0], s=10)
        ax[0][0].set_title("Polutan PM2.5", loc="center", fontsize=15)

        sns.scatterplot(x='CO', y='PM10', data=full_data, palette=colors, ax=ax[0][1], s=10)
        ax[0][1].set_title("Polutan PM10", loc="center", fontsize=15)
        
        sns.scatterplot(x='CO', y='SO2', data=full_data, palette=colors, ax=ax[0][2], s=10)
        ax[0][2].set_title("Polutan SO2", loc="center", fontsize=15)
        
        sns.scatterplot(x='CO', y='NO2', data=full_data, palette=colors, ax=ax[1][0], s=10)
        ax[1][0].set_title("Polutan NO2", loc="center", fontsize=15)
        
        sns.scatterplot(x='CO', y='O3', data=full_data, palette=colors, ax=ax[1][1], s=10)
        ax[1][1].set_title("Polutan O3", loc="center", fontsize=15)

        sns.scatterplot(x='CO', y='CO', data=full_data, palette=colors, ax=ax[1][2], s=10)
        ax[1][2].set_title("Polutan CO", loc="center", fontsize=15)

        plt.suptitle("Korelasi Polutan CO Dengan Polutan Lain", fontsize=30)

    elif tab == "PM10":
        sns.scatterplot(x='PM10', y='PM2.5', data=full_data, palette=colors, ax=ax[0][0], s=10)
        ax[0][0].set_title("Polutan PM2.5", loc="center", fontsize=15)

        sns.scatterplot(x='PM10', y='PM10', data=full_data, palette=colors, ax=ax[0][1], s=10)
        ax[0][1].set_title("Polutan PM10", loc="center", fontsize=15)
        
        sns.scatterplot(x='PM10', y='SO2', data=full_data, palette=colors, ax=ax[0][2], s=10)
        ax[0][2].set_title("Polutan SO2", loc="center", fontsize=15)
        
        sns.scatterplot(x='PM10', y='NO2', data=full_data, palette=colors, ax=ax[1][0], s=10)
        ax[1][0].set_title("Polutan NO2", loc="center", fontsize=15)
        
        sns.scatterplot(x='PM10', y='O3', data=full_data, palette=colors, ax=ax[1][1], s=10)
        ax[1][1].set_title("Polutan O3", loc="center", fontsize=15)

        sns.scatterplot(x='PM10', y='CO', data=full_data, palette=colors, ax=ax[1][2], s=10)
        ax[1][2].set_title("Polutan CO", loc="center", fontsize=15)

        plt.suptitle("Korelasi Polutan PM10 Dengan Polutan Lain", fontsize=30)

    return fig

data = pd.read_csv("https://raw.githubusercontent.com/ArmFriiz/Dicoding-Analisis_Data/main/dashboard/Full_data.csv")

st.title('Proyek Analisis Data | Dataset Air Quality')
st.caption("Muhammad Faris Akbar | m179d4ky3291@bangkit.academy")

# Menampilakn tingkat polutan tertinggi dan terendah
st.title("Rata-Rata Tingkat Polutan PM2.5 Yang Tertinggi Dan Terendah")
plot_pm25(data)
st.write("Berdasarkan hasil visualisasi tersebut didapatkan hasil Kota Dongsi merupakan Kota yang memiliki rata-rata polutan PM2.5 paling tinggi dan Kota Dingling merupakan kota yang memiliki rata-rata polutan PM2.5 paling rendah")

# Menampilkan korelasi polutan
st.title('Korelasi Polutan NO2 Dan CO Dengan Polutan Lain')

tabs = ["NO2", "CO", "PM10"]
selected_tab = st.radio("Pilih Polutan:", tabs)

fig = plot_correlation(selected_tab, data)
st.pyplot(fig)

if selected_tab == "NO2":
    st.write("Berdasarkan hasil korelasi dan visualisasi data tersebut didapatkan hasil bahwa polutan NO2 memiliki korelasi yang kuat dengan polutan CO dan PM2.5")
    st.write("Dengan urutan korelasi nya adalah :")
    st.write("1.CO")
    st.write("2.PM2.5")
    st.write("3.PM10")
    st.write("4.SO2")
    st.write("5.O3")
elif selected_tab == "CO":
    st.write("Berdasarkan hasil korelasi dan visualisasi data tersebut didapatkan hasil bahwa polutan CO memiliki korelasi yang kuat dengan polutan PM2.5 dan PM10")
    st.write("Dengan urutan korelasi nya adalah :")
    st.write("1.PM2.5")
    st.write("2.PM10")
    st.write("3.NO2")
    st.write("4.SO2")
    st.write("5.O3")
elif selected_tab == "PM10":
    st.write("Berdasarkan hasil korelasi dan visualisasi data tersebut didapatkan hasil bahwa polutan PM10 memiliki korelasi yang kuat dengan polutan PM2.5 dan CO")
    st.write("Dengan urutan korelasi nya adalah :")
    st.write("1.PM2.5")
    st.write("2.CO")
    st.write("3.NO2")
    st.write("4.SO2")
    st.write("5.O3")