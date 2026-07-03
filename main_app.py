# main_app.py - PetaMasa.my Master User Interface Presentation Layer
import streamlit as st
from ai_engine import compile_appeal_text
from pdf_engine import generate_submission_pdf
from payment_gateway import create_fpx_payment_bill

st.set_page_config(
    page_title="PetaMasa.my - Rayuan UPU Generator",
    page_icon="🇲🇾",
    layout="centered"
)

# 🌐 UNIVERSAL REGIONAL UNIVERSITY DICTIONARY MAPPING
university_data = {
    "Wilayah Persekutuan / Kuala Lumpur": [
        "Universiti Malaya (UM)",
        "Universiti Pertahanan Nasional Malaysia (UPNM)",
        "Universiti Teknologi Malaysia (UTM KL Campus)"
    ],
    "Selangor": [
        "Universiti Kebangsaan Malaysia (UKM)",
        "Universiti Putra Malaysia (UPM)",
        "Universiti Teknologi MARA (UiTM Shah Alam)"
    ],
    "Johor": [
        "Universiti Teknologi Malaysia (UTM Skudai)",
        "Universiti Tun Hussein Onn Malaysia (UTHM)"
    ],
    "Penang / Perak": [
        "Universiti Sains Malaysia (USM)",
        "Universiti Pendidikan Sultan Idris (UPSI)"
    ],
    "Pahang / Terengganu / Kelantan": [
        "Universiti Malaysia Pahang Al-Sultan Abdullah (UMPSA)",
        "Universiti Malaysia Terengganu (UMT)",
        "Universiti Sultan Zainal Abidin (UniSZA)",
        "Universiti Malaysia Kelantan (UMK)"
    ],
    "Kedah / Perlis": [
        "Universiti Utara Malaysia (UUM)",
        "Universiti Malaysia Perlis (UniMAP)"
    ],
    "Melaka / Negeri Sembilan": [
        "Universiti Teknikal Malaysia Melaka (UTeM)",
        "Universiti Sains Islam Malaysia (USIM)"
    ],
    "Sabah / Sarawak": [
        "Universiti Malaysia Sabah (UMS)",
        "Universiti Malaysia Sarawak (UNIMAS)"
    ]
}

app_language = st.radio("Select Language / Pilihan Bahasa:", ("Bahasa Melayu", "English"), horizontal=True)

if app_language == "Bahasa Melayu":
    title_text = "📝 PetaMasa.my - Penjana Surat Rayuan UPU & Resume Akademik"
    desc_text = "Bina surat rayuan rasmi (Surat Kiriman Rasmi) berformat penuh yang mematuhi syarat kemasukan universiti awam tempatan secara automatik."
    sec1_text = "👤 Langkah 1: Profil Peribadi & Hubungan"
    name_label = "Nama Penuh (seperti dalam MyKad):"
    email_label = "Alamat Emel Aktif:"
    sec2_text = "📊 Langkah 2: Keputusan Peperiksaan Asas"
    grades_label = "Sila masukkan keputusan SPM atau Percubaan secara terperinci:"
    sec3_text = "🏛️ Langkah 3: Institusi Sasaran & Program Pilihan"
    state_label = "Pilih Lokasi / Negeri Universiti:"
    uni_label = "Pilih Universiti Sasaran:"
    major_label = "Nama Program / Jurusan yang Dipohon:"
    sec4_text = "🏆 Langkah 4: Pencapaian Kokurikulum & Impak Kepimpinan"
    activity_label = "Senaraikan jawatan kepimpinan, kelab, atau kejayaan sukan/STEM:"
    sec5_text = "🎯 Langkah 5: Justifikasi Rayuan & Motivasi Diri"
    reason_label = "Nyatakan sebab kukuh mengapa jawatankuasa pemilihan perlu meluluskan rayuan anda:"
    btn_label = "🚀 Bina Draf Surat Rayuan Rasmi"
    error_text = "⚠️ Maklumat penting tidak lengkap. Sila isi medan Nama, Emel, Keputusan, dan Nama Program."
    spinner_text = "Mengira kriteria akademik melalui Enjin AI PetaMasa..."
    lock_text = "🔒 SEKATAN KESELAMATAN: Pakej dokumen rayuan premium anda telah berjaya dijana dan disimpan."
    payment_desc = "Untuk membuka kunci dan memuat turun PDF rasmi tanpa tera air yang sedia dihantar ke sistem UPU, sila selesaikan transaksi FPX di bawah:"
    preview_title = "📄 Previu Visual Dokumen Masa Nyata (Draf Tera Air):"
else:
    title_text = "📝 PetaMasa.my - Automated UPU Appeal & Academic Resume Generator"
    desc_text = "Generate a professionally formatted Surat Kiriman Rasmi appeal letter tailored to official Malaysian university admission criteria instantly."
    sec1_text = "👤 Step 1: Personal & Academic Profile"
    name_label = "Full Name (as per MyKad Identification card):"
    email_label = "Your Active Email Address:"
    sec2_text = "📊 Step 2: Academic Metrics Log"
    grades_label = "List Core SPM or Trial Marks Results exactly:"
    sec3_text = "🏛️ Step 3: Targeted Institution & Strategic Direction"
    state_label = "Select University Location/State:"
    uni_label = "Select Target University:"
    major_label = "Proposed Course / Major Selection Program:"
    sec4_text = "🏆 Step 4: Holistic Co-Curricular & Extracurricular Highlights"
    activity_label = "List Leadership Roles, Sports, or Club/STEM Achievements:"
    sec5_text = "🎯 Step 5: Core Personal Motivation & Appeal Rationale"
    reason_label = "Explain why you must excel in this major and why the board should approve your intake layout:"
    btn_label = "🚀 Compile Premium Appeal Document Asset"
    error_text = "⚠️ Crucial data variables are missing. Please complete Name, Email, Grades, and Proposed Major fields."
    spinner_text = "Compiling academic criteria via PetaMasa AI Engine..."
    lock_text = "🔒 SECURITY BLOCKER: Your premium tailored document asset package has been successfully compiled."
    payment_desc = "To unlock and download the clean, official, non-watermarked PDF ready for UPU system submission, please complete the secure FPX transaction below:"
    preview_title = "📄 Real-Time Document Visual Preview (Watermarked Draft):"

st.title(title_text)
st.markdown("---")
st.write(desc_text)

# ✅ UX FIX: Create dynamic dropdowns OUTSIDE the form structure using a clear tracking key rule.
# This guarantees state switching occurs instantly without freezing or emptying inputs on submit.
st.markdown(f"### {sec3_text}")
selected_state = st.selectbox(state_label, list(university_data.keys()), key="user_selected_state_widget")
target_uni = st.selectbox(uni_label, university_data[selected_state], key="user_selected_uni_widget")

# All input variables are now safely, strictly grouped inside a singular unified form container.
with st.form("master_student_input_form", clear_on_submit=False):
    
    st.markdown(f"### {sec1_text}")
    student_name = st.text_input(name_label, placeholder="e.g., Rahmad Rajali")
    student_email = st.text_input(email_label, placeholder="e.g., chai004@yahoo.com")
    
    st.markdown(f"### {sec2_text}")
    examination_grades = st.text_area(grades_label, placeholder="e.g., BM: A, Math: A, English: C, SAINS: B, Fizik: B")
    
    st.markdown(f"### {major_label}")
    target_major = st.text_input("", placeholder="e.g., Cyber Security")
    
    st.markdown(f"### {sec4_text}")
    extracurricular_achievements = st.text_area(activity_label, placeholder="e.g., Pengawas sekolah, Ahli Aktif Kelab Robotik & STEM")
    
    st.markdown(f"### {sec5_text}")
    core_reason_statement = st.text_area(reason_label, placeholder="e.g., Minat mendalam dalam pertahanan digital, mempelajari asas Linux secara kendiri.")
    
    st.markdown("---")
    submit_execution_trigger = st.form_submit_button(label=btn_label)

if submit_execution_trigger:
    if not student_name or not student_email or not examination_grades or not target_major:
        st.error(error_text) # ✅ LOCALIZATION FIX: Dynamically updates validation text language based on selector
    else:
        with st.spinner(spinner_text):
            student_payload = {
                "name": student_name,
                "email": student_email,
                "grades": examination_grades,
                "university": target_uni,
                "course": target_major,
                "activities": extracurricular_achievements,
                "reason": core_reason_statement,
                "language": app_language
            }
            
            generated_appeal_letter = compile_appeal_text(student_payload)
            
            st.markdown("---")
            st.warning(lock_text)
            st.markdown("### Transaction Total: **RM 9.90**")
            st.write(payment_desc)
            
            checkout_redirect_url = create_fpx_payment_bill(student_name, student_email, 9.90)
            html_button_string = f'<a href="{checkout_redirect_url}" target="_blank"><button style="background-color:#E65100;color:white;padding:14px 28px;border:none;border-radius:6px;cursor:pointer;font-size:18px;font-weight:bold;width:100%;">💳 Pay Now via FPX Online Banking</button></a>'
            st.markdown(html_button_string, unsafe_allow_html=True)
            
            st.markdown(f"### {preview_title}")
            st.info(generated_appeal_letter)
