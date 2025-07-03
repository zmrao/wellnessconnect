# WellnessConnect - AI-Powered Health Concierge Platform

A WhatsApp-based AI health concierge that pre-qualifies leads, schedules appointments, and provides personalized wellness recommendations for The Wellness London.

## Features

- **AI Chatbot Integration**: WhatsApp Business API integration with intelligent health assessments
- **Smart Lead Qualification**: Automatic categorization by treatment type and urgency
- **Personalized Content Delivery**: Targeted wellness content in English/Arabic
- **Automated Follow-up**: Post-treatment care reminders and wellness plan delivery
- **Multi-language Support**: English and Arabic content delivery
- **White-label Ready**: Scalable platform for other wellness clinics

## Project Structure

```
wellnessconnect/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── models/              # Data models
│   ├── services/            # Business logic services
│   ├── api/                 # API endpoints
│   └── utils/               # Utility functions
├── config/
│   └── settings.py          # Configuration settings
├── data/
│   ├── content/             # Wellness content templates
│   └── responses/           # AI response templates
├── tests/
└── requirements.txt
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd wellnessconnect
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```
   WHATSAPP_TOKEN=your_whatsapp_business_token
   WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id
   OPENAI_API_KEY=your_openai_api_key
   DATABASE_URL=sqlite:///./wellnessconnect.db
   SECRET_KEY=your_secret_key
   ```

5. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

## Implementation Phases

### Phase 1 (Month 1)
- Basic appointment booking
- FAQ bot functionality
- WhatsApp webhook integration

### Phase 2 (Months 2-3)
- AI health assessment
- Content personalization
- Lead qualification system

### Phase 3 (Month 4+)
- White-label licensing
- Multi-clinic support
- Advanced analytics

## API Endpoints

- `POST /webhook/whatsapp` - WhatsApp webhook handler
- `GET /health` - Health check endpoint
- `POST /api/appointments` - Appointment management
- `GET /api/leads` - Lead qualification data

## Expected ROI

- Reduce ad cost per lead from £30+ to sub-£1
- Increase conversion rates by 40%
- Generate £5K-10K MRR through platform licensing