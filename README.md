# Chatbot with Admin and Registration Features

This project is a Django-based chatbot with support for user registration and an admin panel to manage registrations. The bot responds to various user commands and handles registrations by collecting user details and saving them to an Excel file. Admin commands allow administrators to view and manage user registrations.

## Features

- **User Registration**: The bot can guide users through a step-by-step registration process and save their details to an Excel file.
- **Admin Mode**: Admin users can enter a secret key to access admin commands like viewing registrations, clearing data, and more.
- **Bot Responses**: The bot can answer predefined questions and suggest corrections for user commands.
- **Admin Commands**: Admins can use commands like `/show` to view registrations and `/clear` to clear the session.
- **User Commands**: Admins can use commands like `/register` to register and `/stop` to stop the registration session.


## Prerequisites

- Python 3.x
- Django 3.x or above
- Openpyxl (for working with Excel files)

## How it Works

### User Mode

In **User Mode**, users can interact with the bot to get responses to predefined questions, start the registration process, and execute user-related commands. Below are the available features and commands in **User Mode**:

#### 1. **Bot Responses**
The bot responds to several predefined messages. Some examples include:

- **hello**: Responds with "Hello! How can I help you today?"
- **how are you**: Responds with "I'm just a bot, but I'm doing great, thank you!"
- **what can you do**: Responds with "I'm here to help you with any questions you have. Just ask me anything!"
- **what is your name**: Responds with "I'm a bot, you can call me Jack."
- **bye**: Responds with "Goodbye! Have a great day!"
- **help**: Responds with "I'm here to help you! Just ask me anything."

#### 2. **User Commands**

Users can also use a few commands to interact with the bot:

- **/register**: Starts the registration process where users provide their details step-by-step.
- **/stop**: Stops the registration process and clears any data entered by the user.
- **/cmd**: Lists all available user-related commands.
- **/cmd-admin**: Lists admin-related commands (admin-only feature).
- **/clear**: To clear the session data.

#### 3. **Registration Process**

When a user starts the registration process with the `/register` command, the bot will guide them through the following steps:

1. **Enter your name**: The user is prompted to enter their name in uppercase letters.

   Example: `JOHN DOE`

2. **Enter your mobile number**: The user is asked to enter a 10-digit mobile number.

   Example: `9876543210`

3. **Enter your email**: The user is asked to provide their email, which must end with `@gmail.com`.

   Example: `john.doe@gmail.com`

4. **Enter your course name**: The user needs to specify their course as either `BE` or `DIPLOMA`.

   Example: `BE`

5. **Enter your class name**: The user needs to provide their class name, which should be in uppercase with at most one space.

   Example: `CS 1`

6. **Enter your roll number**: The user needs to enter their roll number, which should start with `1610`.

   Example: `1610123456`

Once the registration is completed, the bot will save the information to an Excel file. If the user is already registered, the bot will notify them of the duplication. The registration data is saved with the following columns:
- Name
- Mobile Number
- Email
- Course
- Class Name
- Roll Number

#### 4. **Error Handling During Registration**

The bot will validate the user input during each step:

- **Name**: The name must be in uppercase.
- **Mobile Number**: It must be exactly 10 digits long.
- **Email**: Must end with `@gmail.com`.
- **Course**: Must be either `BE` or `DIPLOMA` in uppercase.
- **Class Name**: Must contain only one space, no special characters, and be in uppercase.
- **Roll Number**: Must start with `1610`.

If the user enters invalid data, the bot will ask them to re-enter the correct format.

#### 5. **Commands Available for Users**

Users can use the following commands during their interaction with the bot:

- **/register**: Starts the user registration process.
- **/stop**: Stops the registration process and clears the data entered by the user. If no registration is ongoing, it will notify the user.
- **/cmd**: Lists all available user-related commands.

When the user types `/cmd`, the bot will return:

User-related commands:
- `/register`: To start the registration process and register user details.
- `/stop`: To stop the current registration process and clear entered data.
- `/cmd`: To show the list of user-related commands.
- `/clear`: To clear the session data.


#### 6. **Command Suggestions**

The bot can suggest commands if the user enters something similar to an admin or user command. For example:

- If the user types something close to `/register`, the bot will suggest the correct command by responding with: "Did you mean '/register'?"

### Admin Mode

In **Admin Mode**, administrators can use a set of special commands to manage registrations and perform administrative tasks. To access Admin Mode, the user needs to enter a valid secret key. Here are the available commands:

- **/admin**: To enter admin mode (requires a secret key).
- **/show**: To view the list of all registrations (in table format).
- **/end**: To exit admin mode.
- **/clear**: To clear the session data.

#### Example Admin Mode Flow:

1. **/admin**: The bot will ask for the secret key to enter admin mode.
2. **Enter Secret Key**: The administrator must provide the correct secret key to gain admin access.
3. **/show**: This will display the list of all registrations.
4. **/end**: This will exit admin mode.
5. **/clear**: Clears the session data for the current user.

### 7. **Excel File**

The registration data is stored in an Excel file (`register.xlsx`). Each event will have its own sheet, and the bot will create a new sheet for each event if it doesn't already exist. The data for each registration will be stored with the following columns:
- Name
- Mobile
- Email
- Course
- Class Name
- Roll Number

### 8. **Database Integration**

Instead of an Excel sheet you can use any database of your choice or any cloud cluster of you choice to store the data and show it as per your requirement. The database update will be added soon in the code. 

### 9. **Error Handling**

If an error occurs during processing, the bot will return an error message: "An error occurred while processing your request. Please try again later."

## Admin Commands

- **/admin**: Enter admin mode with the correct secret key.
- **/show**: View the list of all registrations.
- **/end**: Exit admin mode.
- **/clear**: Clear the session data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
