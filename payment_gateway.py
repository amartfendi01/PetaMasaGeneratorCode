# payment_gateway.py - PetaMasa.my ToyyibPay FPX API Integration Router
import requests
import os

def create_fpx_payment_bill(client_name: str, client_email: str, collection_amount_myr: float) -> str:
    """
    Communicates with ToyyibPay's gateway servers to launch an official FPX 
    Online Banking bill statement link under the PetaMasa.my brand architecture.
    """
    amount_in_cents = int(collection_amount_myr * 100)
    toyyibpay_production_api_url = "https://toyyibpay.com"
    
    # Secure environment variable ingestion layer
    secret_token = os.getenv('TOYYIBPAY_SECRET_KEY', 'FALLBACK_MOCK_DEV_KEY')
    category_token = os.getenv('TOYYIBPAY_CATEGORY_CODE', 'FALLBACK_MOCK_CAT_CODE')
    
    transaction_configuration_payload = {
        'userSecretKey': secret_token, 
        'categoryCode': category_token,        
        'billName': 'PetaMasa.my - UPU Academic Appeal Letter Generator',
        'billDescription': f'Automated PDF Letter Compilation Processing Fee for {client_name}',
        'billPriceSetting': 1, 
        'billPayorInfo': 1,    
        'billAmount': amount_in_cents,
        'billReturnUrl': 'https://render.com',
        'billCallbackUrl': 'https://render.com',
        'billTo': client_name,
        'billEmail': client_email,
        'billPhone': '0123456789' 
    }
    
    try:
        network_response = requests.post(toyyibpay_production_api_url, data=transaction_configuration_payload, timeout=12)
        if network_response.status_code == 200:
            response_json_data = network_response.json()
            unique_bill_code = response_json_data['BillCode']
            return f"https://toyyibpay.com{unique_bill_code}"
        else:
            return "https://toyyibpay.com"
    except Exception:
        return "https://toyyibpay.com"
