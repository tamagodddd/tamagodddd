import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
all_df = pd.read_csv('https://raw.githubusercontent.com/tamagodddd/tamagodddd/blob/e214c727d491e047909f2f6cd6df5884a8f33a92/dashboard/all_data.csv')

# Judul dashboard
st.title('Proyek Analisis Data Bike Sharing')    

# Data Wrangling
st.header('Data Wrangling')
st.write("""
Data wrangling merupakan sebuah proses atau kumpulan kegiatan yang meliputi pengumpulan data (Gathering data),
penilaian data (Assessing data), serta pembersihan data (Cleaning data) sebelum data digunakan dalam proses analisis data.
""")

st.subheader('Gathering Data')
st.write("""
Tahap pertama dalam Data Wrangling adalah mengumpulkan data dari sumbernya. 
Dalam proyek ini, kita mengumpulkan data dari file CSV hour.csv dan day.csv.
""")

st.subheader('Assessing Data')
st.write("""
Setelah data dikumpulkan, langkah selanjutnya adalah menilai kualitas dan integritas data. 
Pada tahap ini, kita melihat keberadaan nilai yang hilang, kesalahan penulisan, atau duplikat dalam data.
""")

st.subheader('Cleaning Data')
st.write("""
Setelah menilai data, langkah terakhir adalah membersihkan data dengan menangani nilai yang hilang, kesalahan penulisan, atau duplikat, 
sehingga data siap untuk analisis.
""")

# EDA
st.header('Exploratory Data Analysis (EDA)')
st.write("""
EDA merupakan tahap eksplorasi data yang telah dibersihkan guna memperoleh insight dan menjawab pertanyaan analisis.
Pada prosesnya, kita akan sering menggunakan berbagai teknik dan parameter dalam descriptive statistics yang bertujuan untuk menemukan pola, hubungan, serta membangun intuisi terkait data yang diolah.
""")

st.subheader('Explore hour_df')
st.write("""
Di tahap ini, kita akan melakukan analisis terhadap dataset hour_df. 
Berbagai macam analisis seperti univariate, bivariate, dan multivariate akan dilakukan untuk memahami pola dan hubungan antar variabel.
""")

st.subheader('Explore day_df')
st.write("""
Selanjutnya, kita akan melakukan analisis terhadap dataset day_df. 
Sama seperti sebelumnya, berbagai macam analisis akan dilakukan untuk mendapatkan insight dari data.
""")

st.write("""
Langkah terakhir dalam tahapan EDA adalah menggabungkan kedua dataframe hour_df dan day_df menjadi all_df untuk persiapan visualisasi.
""")

# Visualisasi
st.header('Visualization & Explanatory Analysis')
st.write("""
Visualisasi data merupakan cara kita dalam menyajikan data dalam bentuk visual. Hal ini dilakukan untuk mempermudah kita dan orang lain dalam memahami data tersebut.
Selain itu, visualisasi data yang baik juga akan sangat membantu kita dalam menyampaikan story dan pesan dari sebuah data.
""")

visualization_option = st.radio('Pilih Visualisasi', ('Total Rental Bikes by Working Day', 'Total Rental Bikes by Season'))
st.set_option('deprecation.showPyplotGlobalUse', False)

if visualization_option == 'Total Rental Bikes by Working Day':
    st.subheader('Total Rental Bikes by Working Day')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='workingday_x', y='cnt_x', data=all_df)
    plt.title('Total Rental Bikes by Working Day')
    plt.xlabel('Working Day')
    plt.ylabel('Count')
    plt.ylim(0, all_df['cnt_x'].max() * 1.1)
    plt.xticks(ticks=[0, 1], labels=['Holiday', 'Working Day'])
    st.pyplot()
elif visualization_option == 'Total Rental Bikes by Season':
    st.subheader('Total Rental Bikes by Season')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='season_x', y='cnt_x', data=all_df)
    plt.title('Total Rental Bikes by Season')
    plt.xlabel('Season')
    plt.ylabel('Count')
    plt.ylim(0, all_df['cnt_x'].max() * 1.1)
    st.pyplot()

# Conclusion
st.header('Conclusion')

# Conclusion Pertanyaan 1: Perbedaan Peminjaman Sepeda Antara Hari Kerja dan Hari Libur
st.subheader('Perbedaan Peminjaman Sepeda Antara Hari Kerja dan Hari Libur')
conclusion_1 = """
Dari boxplot pertama (“Total Rental Bikes by Workingday”), kita bisa melihat bahwa jumlah penyewaan sepeda pada hari kerja dan hari non-kerja memiliki distribusi yang serupa. Namun, terdapat lebih banyak outlier pada hari kerja, yang mungkin menunjukkan hari-hari tertentu di mana jumlah penyewaan sepeda sangat tinggi dibandingkan hari-hari biasanya. Ini mungkin menunjukkan bahwa meskipun secara umum, peminjaman sepeda tidak berbeda banyak antara hari kerja dan hari libur, ada beberapa hari kerja di mana peminjaman sepeda meningkat secara signifikan.
"""
st.write(conclusion_1)

# Conclusion Pertanyaan 2: Tren Peminjaman Sepeda Seiring Waktu Berjalan
st.subheader('Tren Peminjaman Sepeda Seiring Waktu Berjalan')
conclusion_2 = """
Dari boxplot kedua (“Total Rental Bikes by Season”), kita bisa melihat bahwa jumlah penyewaan sepeda cenderung lebih tinggi pada musim 2 dan 3 dibandingkan musim lainnya. Ini mungkin menunjukkan bahwa seiring berjalannya waktu (dari musim ke musim), tren peminjaman sepeda mengalami fluktuasi. Mungkin ada faktor-faktor tertentu yang mempengaruhi ini, seperti cuaca, liburan, atau acara khusus.
"""
st.write(conclusion_2)
