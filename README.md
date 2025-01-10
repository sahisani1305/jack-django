# Chatbot with Admin and Registration Features

This project is a Django-based chatbot with support for user registration and an admin panel to manage registrations. The bot responds to various user commands and handles registrations by collecting user details and saving them to an Excel file. Admin commands allow administrators to view and manage user registrations.

## Features

- **User Registration**: The bot can guide users through a step-by-step registration process and save their details to an Excel file.
- **Admin Mode**: Admin users can enter a secret key to access admin commands like viewing registrations, clearing data, and more.
- **Bot Responses**: The bot can answer predefined questions and suggest corrections for user commands.
- **Admin Commands**: Admins can use commands like `/show` to view registrations and `/clear` to clear the session.
  
## Prerequisites

- Python 3.x
- Django 3.x or above
- Openpyxl (for working with Excel files)

## How it Works

### 1. Bot Response Handling

The bot listens for user input in JSON format via POST requests. The user can send commands like `/register`, `/stop`, `/cmd`, and `/cmd-admin` for interacting with the bot. 

The bot also handles predefined responses to specific questions like:
- `hello`: Responds with "Hello! How can I help you today?"
- `how are you`: Responds with "I'm just a bot, but I'm doing great, thank you!"
- `help`: Responds with "I'm here to help you! Just ask me anything."

### 2. Registration Process

When the user sends the `/register` command, the bot prompts the user for their:
- Name (in uppercase)
- Mobile number (10 digits)
- Email address (Gmail)
- Course (either "BE" or "DIPLOMA")
- Class name (uppercase, no special characters)
- Roll number (starting with 1610)

Once all details are provided, the bot saves the registration data to an Excel file (`register.xlsx`). If the user tries to register again with the same name and mobile number, the bot will inform them that they are already registered.

### 3. Admin Mode

Admins can access special commands by entering the correct secret key. Admins can use the following commands:
- `/admin`: To enter admin mode (requires the secret key).
- `/show`: To view the list of registrations (in table format).
- `/end`: To exit admin mode.
- `/clear`: To clear the session data.

### 4. Command Suggestions

The bot can suggest commands if a user enters something similar to an admin command. This is only available to users in admin mode.

### 5. Excel File

The registration data is stored in an Excel file (`register.xlsx`). Each event has its own sheet, and the bot will create a new sheet for each event if it doesn't already exist. Data for each registration is stored with the following columns:
- Name
- Mobile
- Email
- Course
- Class Name
- Roll Number

### 6. Error Handling

If an error occurs during processing, the bot will return an error message: `"An error occurred while processing your request. Please try again later."`

## Admin Commands

- **/admin**: Enter admin mode with the correct secret key.
- **/show**: View the list of all registrations.
- **/end**: Exit admin mode.
- **/clear**: Clear the session data.

## Development

Feel free to fork this repository and contribute to the development. If you would like to add features, improve documentation, or fix bugs, create a pull request.

### Example Commands

- **User registration**:
    1. `/register` - Start registration.
    2. Provide details as prompted.
    3. `/stop` - Stop the registration process.
  
- **Admin mode**:
    1. `/admin` - Enter admin mode.
    2. Provide the secret key.
    3. `/show` - View registrations.
    4. `/end` - Exit admin mode.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
