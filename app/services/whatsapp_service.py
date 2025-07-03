import requests
import json
from typing import Dict, Any
from config.settings import settings
import logging

logger = logging.getLogger(__name__)

class WhatsAppService:
    def __init__(self):
        self.token = settings.WHATSAPP_TOKEN
        self.phone_number_id = settings.WHATSAPP_PHONE_NUMBER_ID
        self.base_url = f"https://graph.facebook.com/v18.0/{self.phone_number_id}/messages"
        
    def send_message(self, to: str, message: str, language: str = "en") -> bool:
        """Send a text message via WhatsApp Business API"""
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {"body": message}
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, json=data)
            response.raise_for_status()
            logger.info(f"Message sent successfully to {to}")
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send message to {to}: {e}")
            return False
    
    def send_template_message(self, to: str, template_name: str, language: str = "en") -> bool:
        """Send a template message via WhatsApp Business API"""
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {"code": language}
            }
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, json=data)
            response.raise_for_status()
            logger.info(f"Template message sent successfully to {to}")
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send template message to {to}: {e}")
            return False
    
    def verify_webhook(self, mode: str, token: str, challenge: str) -> str:
        """Verify WhatsApp webhook"""
        if mode == "subscribe" and token == settings.WEBHOOK_VERIFY_TOKEN:
            return challenge
        return None