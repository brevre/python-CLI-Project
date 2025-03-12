from lib.models.model_1 import Session, init_db, User, PasswordEntry
from lib.helpers import encrypt_password, decrypt_password

init_db()  # Ensure database exists
session = Session()

# Example debugging function
def debug():
    users = session.query(User).all()
    print("\n=== Debugging Data ===")
    for user in users:
        print(f"User: {user.username}, ID: {user.id}")
        for p in user.passwords:
            print(f"  - {p.website}: {decrypt_password(p.password)}")

if __name__ == "__main__":
    debug()
