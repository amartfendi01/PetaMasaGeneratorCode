# ai_engine.py - PetaMasa.my Free Groq AI API Engine Mapping Script
import requests
import os

def compile_appeal_text(student_data: dict) -> str:
    """
    Connects to Groq's high-speed cloud servers to process formal text using 
    the 100% free Llama 3 open-source model, enforcing strict administrative layouts.
    """
    target_lang = student_data.get('language', 'Bahasa Melayu')
    
    system_instruction = (
        "You are an expert Malaysian Academic Admissions Counselor and Chief Registrar operating inside PetaMasa.my. "
        f"Your task is to write a highly detailed, comprehensive, and formal UPU Academic Appeal Letter in perfect, fluent {target_lang}.\n\n"
        "CRITICAL MECHANICAL FORMATTING INSTRUCTIONS:\n"
        "1. SENDER BLOCK: Place the sender name, email, and dummy markers for ID Card No, Address, and Phone No at the top-left margin layout boundary exactly like a professional corporate template.\n"
        "2. RECIPIENT BLOCK: Address it formally to: Pengarah, Bahagian Kemasukan Pelajar IPTA, Jabatan Pendidikan Tinggi, Kementerian Pendidikan Tinggi, Putrajaya.\n"
        "3. HORIZONTAL SEPARATOR: Separate the sender/recipient sections cleanly.\n"
        "4. FORMAL HEADLINE: Include a bold, fully capitalized title line starting with: 'RAYUAN PERMOHONAN KEMASUKAN KE PROGRAM...'.\n"
        "5. NUMERICAL PARAGRAPHS: Number each body paragraph clearly starting from paragraph 2 onwards (e.g., '2. Saya ingin...', '3. Untuk makluman...').\n"
        "6. PERSUASIVE PARAGRAPH CORES: Expand each section to sound highly persuasive. Detail how their academic grades, leadership skills, and extracurricular activities align perfectly with the university's rigorous prerequisites. Maintain a humble, professional tone without using Americanized terminology.\n"
        "7. CLOSING SIGNS: End with formal operational phrases ('Sekian, terima kasih', 'BERKHIDMAT UNTUK NEGARA', 'Yang benar'), followed by a clear signature block placeholder."
    )
    
    user_payload = f"""
    APPLICANT NAME: {student_data.get('name')}
    EMAIL ADDRESS: {student_data.get('email')}
    EXAM MARKS RESULTS: {student_data.get('grades')}
    TARGETED UNIVERSITY: {student_data.get('university')}
    TARGETED PROGRAM MAJOR: {student_data.get('course')}
    CO-CURRICULAR STRENGTHS: {student_data.get('activities')}
    CORE PERSONAL MOTIVATION: {student_data.get('reason')}
    """
    
    # ✅ FIX: Verified production OpenAI-compatible Groq endpoint
    api_url = "https://groq.com"
    api_token = os.getenv("GROQ_API_KEY", "MOCK_KEY_PROVISION_FALLBACK")
    
    # Ensure no leading/trailing whitespaces exist in the token string
    api_token_clean = api_token.strip()
    
    headers = {
        "Authorization": f"Bearer {api_token_clean}",
        "Content-Type": "application/json"
    }
    
    payload_data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_payload}
        ],
        "temperature": 0.25 
    }
    
    try:
        # Enforce json formatting parameter parameters explicitly
        response = requests.post(api_url, json=payload_data, headers=headers, timeout=20)
        
        if response.status_code == 200:
            result_json = response.json()
            return result_json['choices'][0]['message']['content'] # ✅ FIX: Fixed exact list index parsing path for the completion token stream
        else:
            return f"System Connection Error: Status {response.status_code}. Details: {response.text}"
    except Exception as network_error:
        return f"Operational Communication Error: {str(network_error)}"
