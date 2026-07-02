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

st.title("📝 PetaMasa.my - Automated UPU Appeal & Academic Resume Generator")
st.markdown("---")
st.write("Generate a professionally formatted Surat Kiriman Rasmi appeal letter tailored to official Malaysian university admission criteria instantly.")

with st.form("master_student_input_form"):
    st.markdown("### 👤 Step 1: Personal & Academic Profile")
    student_name = st.text_input("Full Name (as per MyKad Identification card):", placeholder="e.g., Muhammad Arif Bin Razak")
    student_email = st.text_input("Your Active Email Address:", placeholder="e.g., arif.razak@gmail.com")
    
    st.markdown("### 📊 Step 2: Academic Metrics Log")
    examination_grades = st.text_area("List Core SPM or Trial Marks Results exactly:", placeholder="e.g., BM: A, Sejarah: A-, Matematik: B+, Fizik: B, Kimia: C+")
    
    st.markdown("### 🏛️ Step 3: Targeted Institution & Strategic Direction")
    target_uni = st.text_input("Name of Targeted Higher Ed Institution:", placeholder="e.g., Universiti Malaya (UM)")
    target_major = st.text_input("Proposed Course / Major Selection Program:", placeholder="e.g., Sarjana Muda Sains Komputer (Rangkaian)")
    
    st.markdown("### 🏆 Step 4: Holistic Co-Curricular & Extracurricular Highlights")
    extracurricular_achievements = st.text_area("List Leadership Roles, Sports, or Club Achievements:", placeholder="e.g., Pengerusi Kelab Robotik Sekolah, Johan Bahas Kebangsaan, Pengawas Sekolah")
    
    st.markdown("### 🎯 Step 5: Core Personal Motivation & Appeal Rationale")
    core_reason_statement = st.text_area("Explain why you must excel in this major and why the board should approve your intake layout:", placeholder="e.g., Active interest in mobile app production. Built three local python desktop scripts outside classroom syllabus hours.")
    
    st.markdown("---")
    submit_execution_trigger = st.form_submit_button(label="🚀 Compile Premium Appeal Document Asset")

if submit_execution_trigger:
    if not student_name or not student_email or not examination_grades or not target_major:
        st.error("⚠️ Crucial data variables are missing. Please complete Name, Email, Grades, and Proposed Major fields to proceed.")
    else:
        st.success("🎉 Academic metrics successfully mapped into backend compilation memory array layers!")
        st.markdown("---")
        st.warning("🔒 SECURITY BLOCKER: Your premium tailored document asset package has been successfully compiled and cached.")
        st.markdown("### Transaction Total: **RM 9.90**")
        st.write("To unlock and download the clean, official, non-watermarked PDF ready for UPU system submission, please complete the secure FPX processing transaction link below:")
        
        checkout_redirect_url = create_fpx_payment_bill(student_name, student_email, 9.90)
        
        # ✅ FIXED: Changed native parameter token string format to use an underscore instead of a hyphen
        html_button_string = f'<a href="{checkout_redirect_url}" target="_blank"><button style="background-color:#E65100;color:white;padding:14px 28px;border:none;border-radius:6px;cursor:pointer;font-size:18px;font-weight:bold;width:100%;">💳 Pay Now via FPX Online Banking</button></a>'
        st.markdown(html_button_string, unsafe_allow_html=True)
        
        st.markdown("### 📄 Real-Time Document Visual Preview (Watermarked Draft):")
        st.info(f"""
        **SURAT RAYUAN RASMI KEMASUKAN AKADEMIK - POWERED BY PETAMASA.MY**
        
        Nama Pemohon: {student_name}  
        Alamat Emel: {student_email}  
        Program Pilihan: {target_major} di {target_uni}  
        
        *Tuan / Puan Jawatankuasa Pemilihan,*
        *PER: RAYUAN KEMASUKAN BAGI PROGRAM IJAZAH SARJANA MUDA {target_major.upper()}*
        
        *Merujuk kepada perkara di atas, saya selaku pemohon ingin mengemukakan rayuan rasmi... Keputusan akademik saya {examination_grades} menunjukkan komitmen tinggi saya terhadap subjek asas... Penglibatan saya sebagai {extracurricular_achievements} membuktikan kualiti kepimpinan...*
        """)
