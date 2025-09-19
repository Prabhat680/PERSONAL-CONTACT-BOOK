import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries()
    view_contacts()

def view_contacts():
    contact_list.delete(0, tk.END)
    for i, contact in enumerate(contacts, start=1):
        contact_list.insert(tk.END, f"{i}. {contact['name']} - {contact['phone']}")


def search_contact():
    keyword = simpledialog.askstring("Search Contact", "Enter name or phone:")
    if not keyword:
        return
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact to update!")
        return
    index = selected[0]
    contact = contacts[index]

    name = simpledialog.askstring("Update Name", "Enter New Name:", initialvalue=contact['name'])
    phone = simpledialog.askstring("Update Phone", "Enter New Phone:", initialvalue=contact['phone'])
    email = simpledialog.askstring("Update Email", "Enter New Email:", initialvalue=contact['email'])
    address = simpledialog.askstring("Update Address", "Enter New Address:", initialvalue=contact['address'])

    contacts[index] = {
        "name": name or contact['name'],
        "phone": phone or contact['phone'],
        "email": email or contact['email'],
        "address": address or contact['address']
    }
    messagebox.showinfo("Success", "Contact updated successfully!")
    view_contacts()


def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a contact to delete!")
        return
    index = selected[0]
    contacts.pop(index)
    messagebox.showinfo("Deleted", "Contact deleted successfully!")
    view_contacts()


def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Management System")
root.geometry("500x500")


tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address:").pack()
address_entry = tk.Entry(root)
address_entry.pack()


tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="View Contacts", command=view_contacts).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)


contact_list = tk.Listbox(root, width=50, height=10)
contact_list.pack(pady=10)

root.mainloop()
