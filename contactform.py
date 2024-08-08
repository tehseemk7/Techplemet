import tkinter as tk
from contact import Contact

class ContactForm:
    def __init__(self, master, contact=None):
        self.master = master
        self.contact = contact

        self.first_name_label = tk.Label(master, text="First Name:")
        self.first_name_label.grid(row=0, column=0)
        self.first_name_entry = tk.Entry(master)
        self.first_name_entry.grid(row=0, column=1)

        self.last_name_label = tk.Label(master, text="Last Name:")
        self.last_name_label.grid(row=1, column=0)
        self.last_name_entry = tk.Entry(master)
        self.last_name_entry.grid(row=1, column=1)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=3, column=0)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=3, column=1)

        self.save_button = tk.Button(master, text="Save", command=self.save_contact)
        self.save_button.grid(row=4, column=0)
        self.cancel_button = tk.Button(master, text="Cancel", command=self.master.destroy)
        self.cancel_button.grid(row=4, column=1)

        if contact:
            self.first_name_entry.insert(0, contact.first_name)
            self.last_name_entry.insert(0, contact.last_name)
            self.email_entry.insert(0, contact.email)
            self.phone_entry.insert(0, contact.phone)

    def save_contact(self):
        if self.contact:
            self.contact.first_name = self.first_name_entry.get()
            self.contact.last_name = self.last_name_entry.get()
            self.contact.email = self.email_entry.get()
            self.contact.phone = self.phone_entry.get()
        else:
            self.contact = Contact(0, self.first_name_entry.get(), self.last_name_entry.get(), self.email_entry.get(), self.phone_entry.get())
        self.master.destroy()