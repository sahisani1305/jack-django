from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

# Predefined key-pair values for responses
KEY_PAIR_RESPONSES = {
    "hey": "Hello!| How can I help you today?",
    "how are you": "I'm just a bot, but I'm doing great, thank you!",
    "what can you do": "I'm here to help you with any questions you have. Just ask me anything!",
    "who are you": "I'm a bot created by Mohammed Shaik Sahil. Nice to meet you!",
    "bye": "Goodbye! Have a great day!",
    "what is your name": "I'm a bot, you can call me Jack.",
    "help": "I'm here to help you! Just ask me anything."
}

# Secret key for admin mode
SECRET_KEY = "admin123"  # You can change this to your desired key.

# Store user session info (this should be persisted in a session or a database in production)
user_admin_state = {}  # User state for tracking admin mode and attempts

@csrf_exempt
@require_POST
def get_bot_response(request):
    try:
        data = json.loads(request.body)
        user_message = data.get('message')
        user_id = data.get('user_id')  # Assuming you send a user_id for each session

        # Initialize user state if it doesn't exist
        if user_id not in user_admin_state:
            user_admin_state[user_id] = {
                'is_admin': False,
                'attempts': 0
            }

        # Handle the /admin and /end functionality
        if user_message.startswith("/admin"):
            # If user is already in admin mode, do not ask for the key again
            if user_admin_state[user_id]['is_admin']:
                return JsonResponse({'response': "You are already in admin mode."})
            # Set user to admin mode and ask for the secret key
            user_admin_state[user_id]['is_admin'] = True
            user_admin_state[user_id]['attempts'] = 0
            return JsonResponse({'response': "Please enter the secret key to enter admin mode."})

        elif user_message.startswith("/end") and user_admin_state[user_id]['is_admin']:
            # If user is in admin mode and types /end, exit admin mode
            user_admin_state[user_id]['is_admin'] = False
            return JsonResponse({'response': "You have exited admin mode."})

        # If in admin mode but not yet confirmed
        if user_admin_state[user_id]['is_admin'] and user_admin_state[user_id]['is_admin'] != "confirmed":
            if user_message == SECRET_KEY:
                user_admin_state[user_id]['is_admin'] = "confirmed"
                return JsonResponse({'response': "Hey admin, nice to meet you!"})
            else:
                user_admin_state[user_id]['attempts'] += 1
                # If user fails 3 times, exit admin mode
                if user_admin_state[user_id]['attempts'] >= 3:
                    user_admin_state[user_id]['is_admin'] = False
                    return JsonResponse({'response': "Admin mode failed. You have been logged out."})
                return JsonResponse({'response': f"Incorrect secret key. You have {3 - user_admin_state[user_id]['attempts']} attempts left."})
        
        # If admin mode is confirmed, handle inputs separately
        if user_admin_state[user_id]['is_admin'] == "confirmed":
            return JsonResponse({'response': f"Admin mode: {user_message}"})

        # Normal bot functionality (non-admin mode)
        user_message = user_message.strip().lower()
        bot_response = KEY_PAIR_RESPONSES.get(user_message, "Sorry, I couldn't understand that. Could you please rephrase?")
        return JsonResponse({'response': bot_response})

    except Exception as e:
        return JsonResponse({'error': 'An error occurred while processing your request. Please try again later.'}, status=500)


def index(request):
    return render(request, 'index.html')

def message(request):
    return render(request, 'message.html')
