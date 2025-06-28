from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

CONTACTS_FILE = 'contacts.csv'

# Ensure CSV exists
if not os.path.exists(CONTACTS_FILE):
    with open(CONTACTS_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Store Name', 'Phone Number', 'Email', 'Address'])


def read_contacts():
    contacts = []
    with open(CONTACTS_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        contacts = list(reader)
    return contacts


def write_contacts(contacts):
    with open(CONTACTS_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Store Name', 'Phone Number', 'Email', 'Address'])
        writer.writerows(contacts)


@app.route('/', methods=['GET', 'POST'])
def index():
    contacts = read_contacts()

    if request.method == 'POST':
        store = request.form['store']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        contacts.append([store, phone, email, address])
        write_contacts(contacts)
        return redirect(url_for('index'))

    query = request.args.get('query', '').lower()
    if query:
        contacts = [c for c in contacts if query in c[0].lower() or query in c[1]]
    return render_template('index.html', contacts=contacts, query=query)


@app.route('/delete/<int:index>')
def delete_contact(index):
    contacts = read_contacts()
    if 0 <= index < len(contacts):
        contacts.pop(index)
        write_contacts(contacts)
    return redirect(url_for('index'))


@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update_contact(index):
    contacts = read_contacts()
    if request.method == 'POST':
        store = request.form['store']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        contacts[index] = [store, phone, email, address]
        write_contacts(contacts)
        return redirect(url_for('index'))
    return render_template('update.html', contact=contacts[index], index=index)


if __name__ == '__main__':
    app.run(debug=True)
