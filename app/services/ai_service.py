import openai
from typing import Dict, Any, List
from config.settings import settings
import logging
import json

logger = logging.getLogger(__name__)

class AIService:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY
        
    async def process_health_assessment(self, user_message: str, conversation_history: List[Dict]) -> Dict[str, Any]:
        """Process user message and generate health assessment response"""
        
        system_prompt = """
        You are a professional health concierge for The Wellness London clinic. 
        Your role is to:
        1. Conduct initial health assessments
        2. Qualify leads for appropriate treatments (blood testing, PRP, weight management)
        3. Provide helpful wellness information
        4. Schedule appointments when appropriate
        
        Be professional, empathetic, and informative. Always recommend consulting with healthcare professionals for medical advice.
        """
        
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(conversation_history)
        messages.append({"role": "user", "content": user_message})
        
        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            
            # Analyze the conversation for lead qualification
            qualification = await self._analyze_lead_qualification(user_message, conversation_history)
            
            return {
                "response": ai_response,
                "qualification": qualification
            }
            
        except Exception as e:
            logger.error(f"AI service error: {e}")
            return {
                "response": "I apologize, but I'm experiencing technical difficulties. Please try again later or contact us directly.",
                "qualification": None
            }
    
    async def _analyze_lead_qualification(self, message: str, history: List[Dict]) -> Dict[str, Any]:
        """Analyze conversation to qualify the lead"""
        
        qualification_prompt = """
        Analyze this conversation and provide lead qualification in JSON format:
        {
            "treatment_type": "blood_testing|prp|weight_management|general_wellness",
            "urgency_level": "low|medium|high|urgent",
            "qualification_score": 1-10,
            "ready_for_appointment": true/false,
            "key_concerns": ["concern1", "concern2"]
        }
        """
        
        try: