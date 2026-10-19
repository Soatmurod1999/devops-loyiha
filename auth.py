# GitHub-ni tekshirish uchun oddiy kirish (Authentication) kodi

# Tizimda saqlangan to'g'ri login va parol
HAQIQIY_LOGIN = "admin"
HAQIQIY_PAROL = "devops2026"

print("--- TIZIMGA KIRISH OYNASI ---")

# Foydalanuvchidan ma'lumotlarni so'rash
user_login = input("Loginingizni kiriting: ")
user_password = input("Parolingizni kiriting: ")

# Kiritilgan ma'lumotlarni tekshirish
if user_login == HAQIQIY_LOGIN and user_password == HAQIQIY_PAROL:
    print("\n[MUVAFFAQIYAT]: Tizimga muvaffaqiyatli kirdingiz! DevOps dunyosiga xush kelibsiz.")
else:
    print("\n[XATOLIK]: Login yoki parol noto'g'ri! Qaytadan urinib ko'ring.")
