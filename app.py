import streamlit as st
import random

# Sayfa Başlığı ve Tasarımı
st.set_page_config(page_title="Password Generator", page_icon="🔒")
st.title("🔒 Özel Şifre Oluşturucu")
st.write("Kendine özel, aşırı güvenli şifreni tek tıkla üret.")

# Kullanıcı Girişleri (Slider ve Checkbox)
password_length = st.slider("Şifre Uzunluğu Seç:", min_value=4, max_value=32, value=12)

col1, col2 = st.columns(2)
with col1:
    inc_numbers = st.checkbox("Sayılar (0-9)", value=True)
    inc_upper = st.checkbox("Büyük Harfler (A-Z)", value=True)
with col2:
    inc_lower = st.checkbox("Küçük Harfler (a-z)", value=True)
    inc_special = st.checkbox("Özel Semboller (!@#$)", value=True)

# Karakter Havuzları
nums = "0123456789"
lows = "abcdefghijklmnopqrstuvwxyz"
ups = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
specs = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# Buton
if st.button("Şifre Üret ✨"):
    pool = ""
    temp_password = []
    counter = 0

    # Havuz ve Garanti Karakter Motoru
    if inc_numbers:
        pool += nums
        temp_password.append(random.choice(nums))
        counter += 1
    if inc_upper:
        pool += ups
        temp_password.append(random.choice(ups))
        counter += 1
    if inc_lower:
        pool += lows
        temp_password.append(random.choice(lows))
        counter += 1
    if inc_special:
        pool += specs
        temp_password.append(random.choice(specs))
        counter += 1

    # Uç Durum Kontrolleri
    if counter == 0:
        st.error("En az bir karakter türü seçmelisin!")
    elif counter > password_length:
        st.error(f"{counter} farklı tür seçtin ama uzunluğu {password_length} yaptın. İmkansız!")
    else:
        # Kalanı Doldurma
        while len(temp_password) < password_length:
            temp_password.append(random.choice(pool))

        # Karıştırma
        random.shuffle(temp_password)
        final_password = "".join(temp_password)

        # Şifreyi Ekrana Basma
        st.success("İşte Şifren:")
        st.code(final_password, language="")
