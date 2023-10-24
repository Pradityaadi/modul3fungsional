# Fungsi pertama untuk mengkonversi minggu ke hari
def weeks_to_days(weeks):
    return weeks * 7

# Fungsi kedua untuk mengkonversi hari ke jam
def days_to_hours(days):
    return days * 24

# Fungsi ketiga untuk mengkonversi jam ke menit
def hours_to_minutes(hours):
    return hours * 60

# Fungsi utama untuk mengkonversi format "minggu hari jam menit" ke menit
def convert_to_minutes(data):
    # Memisahkan input menjadi komponen-komponennya
    components = data.split()
    weeks = int(components[0])
    days = int(components[2])
    hours = int(components[4])
    minutes = int(components[6])

    # Menghitung jumlah total menit
    total_minutes = weeks_to_days(weeks) + days_to_hours(days) + hours_to_minutes(hours) + minutes
    return total_minutes

# Data input
data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

# Mengkonversi data input menjadi jumlah total menit
output_data = [convert_to_minutes(d) for d in data]

print(output_data)