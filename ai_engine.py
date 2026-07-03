# ai_engine.py - PetaMasa.my Groq AI API Engine Mapping Script
import requests
import os

def compile_appeal_text(student_data: dict) -> str:
    """
    Connects to Groq's high-speed cloud servers to process formal text.
    """
    target_lang = student_data.get('language', 'Bahasa Melayu')
    
    system_instruction = (
        f"You are an expert Malaysian Academic Admissions Counselor and Chief Registrar "
        f"operating inside PetaMasa.my. Your task is to write a highly detailed, comprehensive, "
        f"and formal UPU Academic Appeal Letter in perfect, fluent {target_lang}.\n\n"
        f"CRITICAL MECHANICAL FORMATTING INSTRUCTIONS:\n"
        f"1. SENDER BLOCK: Place the sender name, email, and dummy markers for ID Card No, "
        f"Address, and Phone No at the top-left margin layout boundary exactly like a professional corporate template.\n"
        f"2. RECIPIENT BLOCK: Address it formally to: Pengarah, Bahagian Kemasukan Pelajar IPTA, "
        f"Jabatan Pendidikan Tinggi, Kementerian Pendidikan Tinggi, Putrajaya.\n"
        f"3. HORIZONTAL SEPARATOR: Separate the sender/recipient sections cleanly.\n"
        f"4. FORMAL HEADLINE: Include a bold, fully capitalized title line starting with: RAYUAN PERMOHONAN KEMASUKAN KE PROGRAM... .\n"
        f"5. NUMERICAL PARAGRAPHS: Number each body paragraph clearly starting from paragraph 2 onwards (e.g., 2. Saya ingin... , 3. Untuk makluman... ).\n"
        f"6. PERSUASIVE PARAGRAPH CORES: Expand each section to sound highly persuasive. Detail how their academic grades, leadership skills, and extracurricular activities align perfectly with the university's rigorous prerequisites. Maintain a humble, professional tone without using Americanized terminology.\n"
        f"7. CLOSING SIGNS: End with formal operational phrases ( Sekian, terima kasih , BERKHIDMAT UNTUK NEGARA , Yang benar ), followed by a clear signature block placeholder."
    )

    user_payload = (
        f"APPLICANT NAME: {student_data.get('name')}\n"
        f"EMAIL ADDRESS: {student_data.get('email')}\n"
        f"EXAM MARKS RESULTS: {student_data.get('grades')}\n"
        f"TARGETED UNIVERSITY: {student_data.get('university')}\n"
        f"TARGETED PROGRAM MAJOR: {student_data.get('course')}\n"
        f"CO-CURRICULAR STRENGTHS: {student_data.get('activities')}\n"
        f"CORE PERSONAL MOTIVATION: {student_data.get('reason')}"
    )

    api_url = "https://api.groq.com/openai/v1/chat/completions"  # ✅ Corrected API endpoint
    api_token = os.getenv("GROQ_API_KEY", "").strip()

    if not api_token:
        return "⚠️ CRITICAL SYSTEM ERROR: GROQ_API_KEY environment variable is missing or empty inside your Render dashboard settings."

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    payload_data = {
        "model": "llama-3.1-8b-instant",  # ✅ Corrected/updated model tag
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_payload}
        ],
        "temperature": 0.25
    }

    try:
        response = requests.post(api_url, json=payload_data, headers=headers, timeout=20)
        
        if response.status_code == 200:
            result_json = response.json()
            return result_json['choices'][0]['message']['content']
        else:
            return f"System Connection Error: Status {response.status_code}. Details: {response.text}"
            
    except Exception as network_error:
        return f"Operational Communication Error: {str(network_error)}"
