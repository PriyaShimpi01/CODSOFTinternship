📇 Contact Management System (CSV Version)
A simple web-based contact manager built with Python Flask, storing data in a CSV file. Easily add, view, search, update, and delete contacts through a clean web interface.

✨ Features
✅ Add new contacts with store name, phone, email, and address
✅ View a list of all saved contacts
✅ Search contacts by store name or phone number
✅ Update contact details
✅ Delete contacts
✅ Simple Bootstrap-based responsive user interface
✅ Data stored in a CSV file (no database needed)

🗂️ Project Structure
contactbk_flask/
  app.py
  contacts.csv   (auto-created on first run)
  templates/
    index.html
    update.html

🚀 Installation & Running
1.Clone the repository
2.Install dependencies
pip install flask
3.Run the server
python app.py
4.Open in browser
Visit http://127.0.0.1:5000

🛠️ Tech Stack
Python 3
Flask
HTML / Bootstrap 5
CSV file for persistent storage

⚙️ Features in Detail
Add Contact: fill a simple form, store contact in CSV
View Contacts: list contacts in a table
Search: find contacts by store name or phone number
Update: edit contact details in-place
Delete: remove a contact with confirmation
CSV Storage: no SQL skills needed