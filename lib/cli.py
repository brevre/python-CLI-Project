import sys
import csv
from lib.models.model_1 import Session, init_db, User, PasswordEntry
from lib.helpers import encrypt_password, decrypt_password
from lib.helpers import validate_name, validate_url, check_password_strength, generate_password

init_db()
session = Session()

MASTER_PASSWORD = "MySecureMaster123"  # Can be stored securely later

def verify_master_password():
    master = input("Enter the master password: ")
    return master == MASTER_PASSWORD

def add_user():
    username = input("Enter username: ").strip()
    if not validate_name(username):
        print("Invalid username! Only letters and spaces are allowed.")
        return
    if session.query(User).filter_by(username=username).first():
        print("User already exists!")
        return
    new_user = User(username=username)
    session.add(new_user)
    session.commit()
    print(f"User {username} added successfully!")

def add_password():
    if not verify_master_password():
        print("Incorrect master password!")
        return
    
    username = input("Enter your username: ").strip()
    user = session.query(User).filter_by(username=username).first()
    if not user:
        print("User not found! Please add a user first.")
        return
    
    website = input("Enter website: ").strip()
    if not validate_url(website):
        print("Invalid website URL!")
        return

    site_username = input("Enter site username: ").strip()
    site_password = input("Enter site password (or type 'generate' for a secure password): ").strip()

    if site_password.lower() == "generate":
        site_password = generate_password()
        print(f"Generated Secure Password: {site_password}")

    strength = check_password_strength(site_password)
    print(f"Password Strength: {strength}")
    if "Weak" in strength:
        print("Consider using a stronger password.")

    encrypted_password = encrypt_password(site_password)

    new_entry = PasswordEntry(website=website, username=site_username, password=encrypted_password, user=user)
    session.add(new_entry)
    session.commit()
    print("Password added successfully!")

def view_passwords():
    if not verify_master_password():
        print("Incorrect master password!")
        return
    
    username = input("Enter your username: ").strip()
    user = session.query(User).filter_by(username=username).first()
    if not user:
        print("User not found!")
        return
    
    passwords = user.passwords
    if not passwords:
        print("No saved passwords.")
        return
    
    print("\nSaved Passwords:")
    for p in passwords:
        decrypted_pass = decrypt_password(p.password)
        print(f"Website: {p.website}, Username: {p.username}, Password: {decrypted_pass}")

def update_password():
    if not verify_master_password():
        print("Incorrect master password!")
        return
    
    username = input("Enter your username: ").strip()
    user = session.query(User).filter_by(username=username).first()
    if not user:
        print("User not found!")
        return
    
    website = input("Enter the website to update: ").strip()
    password_entry = session.query(PasswordEntry).filter_by(user=user, website=website).first()
    
    if not password_entry:
        print("No password found for this website!")
        return

    new_password = input("Enter new password (or type 'generate' for a secure password): ").strip()
    if new_password.lower() == "generate":
        new_password = generate_password()
        print(f"Generated Secure Password: {new_password}")

    strength = check_password_strength(new_password)
    print(f"Password Strength: {strength}")
    if "Weak" in strength:
        print("Consider using a stronger password.")

    password_entry.password = encrypt_password(new_password)
    session.commit()
    print(f"Password for {website} updated successfully!")

def delete_password():
    if not verify_master_password():
        print("Incorrect master password!")
        return
    
    username = input("Enter your username: ").strip()
    user = session.query(User).filter_by(username=username).first()
    if not user:
        print("User not found!")
        return
    
    website = input("Enter the website to delete: ").strip()
    password_entry = session.query(PasswordEntry).filter_by(user=user, website=website).first()
    
    if not password_entry:
        print("No password found for this website!")
        return
    
    session.delete(password_entry)
    session.commit()
    print(f"Password for {website} deleted successfully!")

def export_passwords():
    if not verify_master_password():
        print("Incorrect master password!")
        return
    
    username = input("Enter your username: ").strip()
    user = session.query(User).filter_by(username=username).first()
    if not user:
        print("User not found!")
        return
    
    passwords = user.passwords
    if not passwords:
        print("No saved passwords.")
        return

    filename = f"{username}_passwords.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Website", "Username", "Password"])
        for p in passwords:
            writer.writerow([p.website, p.username, decrypt_password(p.password)])

    print(f"Passwords exported successfully to {filename}")

def main_menu():
    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Add User")
        print("2. Add Password")
        print("3. View Passwords")
        print("4. Update Password")
        print("5. Delete Password")
        print("6. Export Passwords")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            add_password()
        elif choice == "3":
            view_passwords()
        elif choice == "4":
            update_password()
        elif choice == "5":
            delete_password()
        elif choice == "6":
            export_passwords()
        elif choice == "7":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
