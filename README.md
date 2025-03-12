<<<<<<< HEAD
# python-CLI-Project
=======
📌 Password Manager
A command-line Password Manager with encryption, secure storage, and password retrieval.

🚀 Features
✅ Securely store passwords using AES encryption
✅ Add, view, and delete passwords for multiple websites
✅ Validate usernames and website URLs using Regex
✅ Command-line interface for ease of use

📦 Installation
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/your-username/password-manager.git
cd password-manager
2️⃣ Install Dependencies
sh
Copy
Edit
pip install cryptography sqlalchemy
3️⃣ Run the Program
sh
Copy
Edit
python main.py
🔧 Usage
📌 Add a User
sh
Copy
Edit
Enter username: JohnDoe
User JohnDoe added successfully!
📌 Add a Password
sh
Copy
Edit
Enter your username: JohnDoe
Enter website: example.com
Enter site username: johnd
Enter site password: ********
Password added successfully!
📌 View Stored Passwords
sh
Copy
Edit
Enter your username: JohnDoe
Saved Passwords:
Website: example.com, Username: johnd, Password: mySecretPass123
📌 Delete a Password
sh
Copy
Edit
Enter your username: JohnDoe
Enter the website to delete: example.com
Password for example.com deleted successfully!
🛠 Tech Stack
Python 🐍
SQLite (via SQLAlchemy) 🗄
Cryptography (AES Encryption) 🔒
👨‍💻 Contributing
Want to improve this project? Fork the repository and submit a Pull Request (PR).
>>>>>>> 74d1131 (Added funtionality)
