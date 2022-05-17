# Task 1
# Create python syntax to make a dataframe with the data that has been given
data = (
    pd
    .DataFrame({
        'no': [1, 2, 3, 4, 5],
        'nama_siswa': ['Adi',
                       'Budi', 
                       'Carli',
                       'Dadan',
                       'Endang'],
        'umur': [15, 16, 14, None, 16],
        'email': ['andi@gmail.com',
                  'budi@gmail.com',
                  'carli@rakamin.com',
                  'dadan@rakamin.com',
                  'endang@gmail.com'],
        'score_matematika': [80, 90, 100, 95, 97],
        'score_ekonomi': [90, 95, 100, 86, None],
        'score_olahraga': [97, 95, 96, 100, 94]
    })
)
data

# Task 2
# Urutkan data frame berdasarkan kolom score_matematika dari nilai
# terbesar hingga nilai terkecil.
# Simpan hasilnya dengan nama “data_sorted”.
# Dari “data_sorted” tersebut, ambil baris pada siswa dengan
# score_matematika terkecil.
# Simpan hasilnya dengan nama “data_lowest_score”.
# Siapa nama siswa dengan score_matematika terkecil tersebut?
data_sorted = (
    data
    .sort_values('score_matematika', 
                 ascending=False)
)
display(data_sorted)

data_lowest_score = (
    data_sorted[data_sorted
                .score_matematika == data_sorted
                .score_matematika
                .min()]
)
display(data_lowest_score)
print('Siswa dengan score_matematika terkecil yaitu Adi.')

# Task 3
# Filter siswa yang memiliki email ber-domain gmail DAN memiliki 
# score_ekomomi tidak null.
# Simpan hasilnya dengan nama “data_siswa_gmail”.
# Berapa umur rata-rata dari siswa di “data_siswa_gmail” tersebut?
data_siswa_gmail = (
    data[data['email']
    .str
    .contains('gmail.com') & data['score_ekonomi']
    .notnull()]
)
display(data_siswa_gmail)

umur_rata2 = (
    data_siswa_gmail['umur']
    .mean()
)
print('Umur rata-rata siswa pada data_siswa_gmail yaitu:', umur_rata2)

# Task 4
# Membuat dataframe baru dengan data yang tersedia.
# Kemudian append “additional_data” tersebut dengan data frame “data”.
# Simpan dengan nama “new_data”.
# Berapa median umur mereka sekarang? (setelah append dilakukan).
additional_data = (
    pd
    .DataFrame({
        'no': [6, 7],
        'nama_siswa': ['Fauzan',
                       'Guntur'],
        'umur': [15, 16],
        'email': ['fauzan@gmail.com',
                  'guntur@gmail.com'],
        'score_matematika': [80, 90],
        'score_ekonomi': [90, 95],
        'score_olahraga': [97, 95]
    })
)

new_data = (
    data
    .append(additional_data)
)
display(new_data)

median_umur = (
    new_data['umur']
    .median()
)

print('Median umur seluruh siswa yaitu:', median_umur)

# Task 5
# Membuat dataframe baru dengan data yang tersedia dengan nama data_address
# Lakukanlah merge data frame “new_data” pada no.4 di atas dengan “data_address”
# Bandingkan umur rata-rata siswa per alamat mereka berasal
# Pada alamat yang mana, umur rata-rata mereka yang paling kecil?
# Masukan syntax jawaban di sini
data_address = (
    pd
    .DataFrame({
        'nama'  : ['Adi',
                   'Budi',
                   'Dadan',
                   'Endang',
                   'Guntur',
                   'Halim'],
        'alamat': ['DKI Jakarta', 
                   'DKI Jakarta', 
                   'Banten', 
                   'Banten', 
                   'Jawa Barat', 
                   'Aceh']
    })
)
# Merge new_data dgn data_address
merge_data = (
    new_data
    .merge(data_address,
           left_on = 'nama_siswa',
           right_on = 'nama',
           how = 'outer'
    )
)
display(merge_data)

# Membandingkan umur rata-rata per alamat
umur_per_alamat = (
    merge_data
    .groupby('alamat')
    .agg({'umur': 'mean'})
    .sort_values('umur')
    .reset_index()
)
display(umur_per_alamat)

# Melihat alamat dgn umur rata2 terkecil
result = (
    umur_per_alamat[umur_per_alamat[
        'umur'] == umur_per_alamat[
        'umur']
        .min()]
)
display(result)
print('Seperti terlihat pada tabel, umur rata-rata terkecil yaitu berasal dari DKI Jakarta.')

# Task 6
# Import ke-3 file Excel yang telah disediakan di sini.
# Simpan data frame dengan nama airlines, airports dan flights
# Case:
# Department of Transportation sedang melakukan audit data
# sepanjang tahun 2015, mereka membutuhkan data-data berikut:
# a. Total penerbangan per bulan selama 2015.
# b. Total penerbangan yang CANCELLED per bulan.
# c. Rata-rata, Minimum dan Maksimum ELAPSED_TIME per bulan.
import pandas as pd
airlines = pd.read_excel('data_airlines.xlsx')
airports = pd.read_excel('data_airports.xlsx')
flights = pd.read_excel('data_flights.xlsx')
# a. Total penerbangan per bulan selama 2015
terbang_perbulan = (
    flights
    .groupby(['YEAR', 
              'MONTH'])
    .agg({'FLIGHT_NUMBER':
          'count'})
    .reset_index()
) 
display(terbang_perbulan)
# b. Total penerbangan yang CENCELLED per bulan 
cancelled_perbulan = (
    flights
    .groupby(['MONTH'])
    .agg({'CANCELLED': 
          'sum'})
    .reset_index()
) 
display(cancelled_perbulan) 
# c. Rata-rata, Minimum, dan Maksimum ELAPSED_TIME per bulan
elapsed_perbulan = (
    flights
    .groupby('MONTH')
    .agg({'ELAPSED_TIME': ['mean', 
                           'min', 
                           'max']
         })
    .reset_index()
)
display(elapsed_perbulan)

# Task 7
# Case:
# Department of Transportation sedang melakukan analisis data
# untuk seluruh penerbangan dari airport: john f. kennedy dan
# northwest florida.
# Mereka ingin mengetahui total penerbangan per masing-masing
# destinasi airports dan rata-rata distance dari kedua airports tersebut
# ke setiap destinasi yang ada.
# question:
# Destinasi airport** mana yang paling banyak jumlah
# penerbangannya?
# ** sebutkan dalam bentuk nama airport (bukan code airport).
result = (
    airports[airports['AIRPORT']
    .str
    .lower()
    .str
    .contains('john f. kennedy|northwest florida')]
)
result
'''
Pada result di atas terlihat bahwa kode
airport john f kennedy yaitu JFK dan
northwest florida yaitu ECP.
'''
df_origin = (
    flights[
        flights['ORIGIN_AIRPORT']
        .isin(['JFK','ECP'])
    ]
)
df_origin
df_new = (
    df_origin
    .groupby('DESTINATION_AIRPORT')
    .agg({'FLIGHT_NUMBER' : ['count'],
          'DISTANCE' : ['mean']})
    .reset_index()
)
df_new
df_new.columns = (
    ['Destination_Airport',
     'Flight_Number', 
     'Distance']
)
df_new
result = (
    airports[
        airports['IATA_CODE'] == 'SFO']
)
result['AIRPORT']

# Task 8
# Buatlah 2 dataframe mengikuti petunjuk berikut:
# df_1 : Filter dataset 01 telecom_revenue.csv dengan multiple kondisi
# a. MonthlyRevenue > 10
# b. Occupation terdiri dari Professional, Student, and Crafts.
# df_2 : Filter dataset 02 telecom_usage.csv dengan multiple kondisi
# a. CustomerCareCalls diawali digit genap (2, 4, 6 atau 8)
# b. Nilai UnansweredCalls > BlockedCalls.
# Hitunglah total CustomerID dan rata-rata DroppedCalls untuk
# masing-masing occupation.
# Pada occupation apa, rata-rata DroppedCalls paling besar?
import pandas as pd 

df_1 = pd.read_csv('01 telecom_revenue.csv')
df_2 = pd.read_csv('02 telecom_usage.csv')

# Filter MonthlyRevenue > 10
# dan Occupation terdiri dari Professional,
# Student, and Crafts.
df_1 = (
    df_1[(
        df_1['MonthlyRevenue'] > 10) 
        & (df_1['Occupation']
        .isin(['Professional', 
               'Student',
               'Crafts'])
          )]
)
display(df_1)

# Filter CustomerCareCalls diawali digit genap 
# (2, 4, 6 atau 8)
# dan nilai UnansweredCalls > .BlockedCalls
df_2 = (
    df_2[( 
        df_2['CustomerCareCalls']
        .astype('str')
        .str
        .contains('^2|^4|^6|^8'))
        & (df_2['UnansweredCalls']
        > df_2['BlockedCalls'])
    ]
)
display(df_2)
# Merge data hasil filtering
data_merge = (
    df_1
    .merge(df_2,
           on = 'CustomerID',
           how = 'inner'
          )
)
data_merge
# Total CustomerID dan rata2 DroppedCalls
# utk tiap Occupation
result = (
    data_merge
    .groupby('Occupation')
    .agg({'CustomerID' : ['count'],
          'DroppedCalls' : ['mean']})
    .reset_index()
)
result
# Melihat occupation dgn rata2 
# DroppedCalls terbesar
result.columns = (
    ['Occupation', 
     'CustomerID', 
     'DroppedCalls']
)
result = (
    result[result[
        'DroppedCalls'] == result[
        'DroppedCalls']
           .max()]
)
result
