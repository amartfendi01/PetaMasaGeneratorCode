# ai_engine.py - Core Backend Intelligence Mapping Code Matrix
import requests
import os
import json

def compile_appeal_text(student_data: dict) -> str:
    """
    Takes plain text input form weights from the Streamlit web screen,
    injects them behind the scenes into a rigid system prompt template,
    and returns a professionally formatted letter layout.
    """
    # LEARNING NOTE: System prompts have been rebranded from old experimental parameters to PetaMasa.my
    system_instruction = (
        "You are an expert Malaysian Academic Admissions Counselor and Chief Registrar. "
        "Your task is to write a formal, high-impact UPU Academic Appeal Letter in perfect, formal Bahasa Melayu. "
        "You must strictly follow the traditional 'Surat Kiriman Rasmi' structural parameters.\n\n"
        "REQUIRED LAYOUT FORMATTING STIPULATIONS:\n"
        "1. SENDER DETAILS: Place the sender name, address, and contact markers cleanly at the top-left margin layout boundary.\n"
        "2. RECIPIENT BLOCK: Place the institutional selection board address layout lines underneath the sender, separated by a clean spacer.\n"
        "3. FORMAL HEADLINE: Include a clear capitalized bolded headline section matching standard civil service formats, starting exactly with: 'RAYUAN KEMASUKAN BAGI PROGRAM...'\n"
        "4. INTRODUCTORY LINE: Start the paragraph body layout using formal administrative syntax, specifically: 'Merujuk kepada perkara di atas, saya...'\n"
        "5. SELECTION VALUES: Highlight the applicant's core motivation scores, co-curricular highlights, and passion without inventing data attributes.\n"
        "6. CLOSING PROVISIONS: Conclude with formal operational phrases like 'Sekian, terima kasih' and 'Yang benar,' followed by space for a signature block."
    )
    
    # Packaged user parameters extraction matrix mapping variables safely
    user_payload = f"""
    APPLICANT FULL NAME: {student_data.get('name', 'N/A')}
    EXAM MARKS RESULTS: {student_data.get('grades', 'N/A')}
    TARGETED UNIVERSITY: {student_data.get('university', 'N/A')}
    TARGETED COURSE MAJOR: {student_data.get('course', 'N/A')}
    EXTRA-CURRICULAR HIGHLIGHTS: {student_data.get('activities', 'N/A')}
    CORE RATIONALE REASONING: {student_data.get('reason', 'N/A')}
    """
    
    api_url = "https://openai.com"
    
    # Read the secret token key variable loaded inside cloud system profiles
    api_token = os.getenv("OPENAI_API_KEY", "MOCK_KEY_PROVISION_FALLBACK")
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    payload_data = {
        "model": "gpt-4o-mini", # Cost-effective, high-speed production model optimized for Python 3.14 json formatting
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
            return result_json['choices']['message']['content']
        else:
            return f"System Connection Error: Status {response.status_code}. Please check API configurations."
            
    except Exception as network_error:
        return f"Operational Communication Error occurred during execution: {str(network_error)}"
