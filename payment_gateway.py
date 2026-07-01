# payment_gateway.py - ToyyibPay FPX API Outbound Router Integration Matrix
import requests

def create_fpx_payment_bill(client_name: str, client_email: str, collection_amount_myr: float) -> str:
    """
    Communicates with ToyyibPay's gateway servers to launch an official FPX 
    Online Banking bill statement link, returning a standard redirect checkout page.
    """
    amount_in_cents = int(collection_amount_myr * 100)
    
    toyyibpay_production_api_url = "https://toyyibpay.com"
    
    # LEARNING NOTE: Redirect endpoints have been re-routed to point safely to the unified petamasa domain targets
    transaction_configuration_payload = {
        'userSecretKey': 'YOUR_ACTUAL_TOYYIBPAY_SECRET_KEY_HERE', 
        'categoryCode': 'YOUR_ACTUAL_CATEGORY_CODE_HERE',        
        'billName': 'PetaMasa.my - UPU Academic Appeal Letter Generator', # LEARNING NOTE: Old text model tag: UPU Academic Appeal Letter Generator
        'billDescription': f'Automated PDF Letter Compilation Processing Fee for {client_name}',
        'billPriceSetting': 1, 
        'billPayorInfo': 1,    
        'billAmount': amount_in_cents,
        'billReturnUrl': 'https://render.com', # LEARNING NOTE: Old endpoints referenced obsolete server nodes: halatuju-rayuan-app
        'billCallbackUrl': 'https://render.com',
        'billTo': client_name,
        'billEmail': client_email,
        'billPhone': '0123456789' 
    }
    
    try:
        network_response = requests.post(
            toyyibpay_production_api_url, 
            data=transaction_configuration_payload, 
            timeout=12
        )
        
        if network_response.status_code == 200:
            response_json_data = network_response.json()
            unique_bill_code = response_json_data['BillCode']
            return f"https://toyyibpay.com{unique_bill_code}"
        else:
            return "https://toyyibpay.com"
            
    except Exception:
        return "https://toyyibpay.com"
