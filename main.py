import tkinter as tk
from tkinter import ttk

def update_token():
    token = token_entry.get()
    print(f"Jira Token Updated: {token}")

# Create the main window
root = tk.Tk()
root.title("Jira and Settings UI")

# Create the notebook (tab container)
notebook = ttk.Notebook(root)

# Tab 1: Jira Issue
jira_tab = ttk.Frame(notebook)
notebook.add(jira_tab, text="JiraIssue")

# Tab 2: Settings
settings_tab = ttk.Frame(notebook)
notebook.add(settings_tab, text="Settings ⚙️")

# Layout for Jira Issue tab
jira_label = ttk.Label(jira_tab, text="Jira Issue Key:")
jira_label.pack(pady=5, anchor="w")

jira_entry = ttk.Entry(jira_tab, width=30)
jira_entry.pack(pady=5, anchor="w")

description_label = ttk.Label(jira_tab, text="Description:")
description_label.pack(pady=5, anchor="w")

description_text = tk.Text(jira_tab, width=40, height=10, state="normal")
description_text.pack(pady=5)

# Layout for Settings tab
token_label = ttk.Label(settings_tab, text="Jira Token:")
token_label.pack(pady=5, anchor="w")

token_entry = ttk.Entry(settings_tab, width=30)
token_entry.pack(pady=5, anchor="w")

update_button = ttk.Button(settings_tab, text="Update", command=update_token)
update_button.pack(pady=10)

# Pack notebook (tabs)
notebook.pack(expand=True, fill="both")

# Run the application
root.mainloop()
