from datetime import datetime

def get_zodiac_sign(day, month):
    zodiac_signs = [
        (120, "Capricorn"), (218, "Aquarius"), (320, "Pisces"), (420, "Aries"), (521, "Taurus"),
        (621, "Gemini"), (722, "Cancer"), (823, "Leo"), (923, "Virgo"), (1023, "Libra"),
        (1122, "Scorpio"), (1222, "Sagittarius"), (1231, "Capricorn")
    ]
    date_number = month * 100 + day
    for z_sign in zodiac_signs:
        if date_number <= z_sign[0]:
            return z_sign[1]

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def get_zodiac_quote(zodiac_sign):
    # Membaca file teks zodiak dan kata-kata mutiara
    with open('zodiak_quotes.txt', 'r') as file:
        quotes = file.readlines()
    
    # Mencari kata-kata mutiara sesuai zodiak
    for line in quotes:
        if zodiac_sign in line:
            return line.split(": ")[1].strip()  # Mengambil bagian setelah tanda ":"
    return "Tidak ada kata-kata mutiara untuk zodiak ini."

def main():
    # Input nama dan tanggal lahir
    name = input("Masukkan nama Anda: ")
    birthdate_str = input("Masukkan tanggal lahir (DD-MM-YYYY): ")
    birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
    
    day = birthdate.day
    month = birthdate.month
    
    zodiac = get_zodiac_sign(day, month)
    age = calculate_age(birthdate)
    quote = get_zodiac_quote(zodiac)
    
    # Output dengan nama, zodiak, umur, tanggal lahir, dan kata-kata mutiara
    print(f"Halo, {name}!")
    print(f"Tanggal lahir Anda: {birthdate.strftime('%d-%m-%Y')}")
    print(f"Zodiak Anda: {zodiac}")
    print(f"Umur Anda: {age} tahun")
    print(f"Kata-kata mutiara untuk {zodiac}: {quote}")

if __name__ == "__main__":
    main()
