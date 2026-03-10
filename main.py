import tkinter as tk
from tkinter import ttk, messagebox
import database
from merge_sort import merge_sort

# Load students from JSON on startup
students = database.load_students()

# --- 1. ADD STUDENT FUNCTION ---
def open_add_student_window():
    add_win = tk.Toplevel(window)
    add_win.title("Add New Student")
    add_win.geometry("300x300")

    tk.Label(add_win, text="Student ID:").pack(pady=2)
    ent_id = tk.Entry(add_win)
    ent_id.pack(pady=2)

    tk.Label(add_win, text="Name:").pack(pady=2)
    ent_name = tk.Entry(add_win)
    ent_name.pack(pady=2)

    tk.Label(add_win, text="Marks:").pack(pady=2)
    ent_marks = tk.Entry(add_win)
    ent_marks.pack(pady=2)

    tk.Label(add_win, text="Age:").pack(pady=2)
    ent_age = tk.Entry(add_win)
    ent_age.pack(pady=2)

    def save_new_student():
        try:
            s_id = ent_id.get().strip()
            s_name = ent_name.get().strip()
            s_marks = float(ent_marks.get())
            s_age = int(ent_age.get())

            if not s_id or not s_name:
                raise ValueError("ID and Name are required!")

            # Add to list and save to JSON
            students.append({"id": s_id, "name": s_name, "marks": s_marks, "age": s_age})
            database.save_students(students)
            
            messagebox.showinfo("Success", f"Student {s_name} added!")
            add_win.destroy()
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid data: {e}")

    tk.Button(add_win, text="Save Student", bg="#4CAF50", fg="white", command=save_new_student).pack(pady=20)

# --- 2. VIEW STUDENTS FUNCTION ---
def view_students():
    if not students:
        messagebox.showinfo("View Students", "No records found.")
        return

    view_win = tk.Toplevel(window)
    view_win.title("All Student Records")
    view_win.geometry("600x400")

    columns = ("ID", "Name", "Marks", "Age")
    tree = ttk.Treeview(view_win, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    for s in students:
        tree.insert("", tk.END, values=(s["id"], s["name"], s["marks"], s["age"]))

    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- 3. SORT FUNCTIONS (Using Merge Sort) ---
def sort_by_marks():
    global students
    if not students: return
    students = merge_sort(students, "marks", reverse=True)
    database.save_students(students)
    messagebox.showinfo("Sort", "Sorted by Marks (High to Low). Opening view...")
    view_students()

def sort_by_name():
    global students
    if not students: return
    students = merge_sort(students, "name", reverse=False)
    database.save_students(students)
    messagebox.showinfo("Sort", "Sorted by Name (A-Z). Opening view...")
    view_students()

# --- 4. SHOW RANKINGS FUNCTION ---
def show_rankings():
    global students
    if not students:
        messagebox.showinfo("Rankings", "No students to rank.")
        return
    
    ranked_list = merge_sort(students, "marks", reverse=True)
    rank_win = tk.Toplevel(window)
    rank_win.title("Rankings")
    rank_win.geometry("500x350")

    tk.Label(rank_win, text="🏆 Student Rankings 🏆", font=("Arial", 14, "bold")).pack(pady=10)

    columns = ("Rank", "Name", "Marks")
    tree = ttk.Treeview(rank_win, columns=columns, show="headings")
    tree.heading("Rank", text="Rank")
    tree.heading("Name", text="Student Name")
    tree.heading("Marks", text="Final Marks")

    for index, s in enumerate(ranked_list, start=1):
        rank_label = f"#{index}"
        if index == 1: rank_label = "🥇 1st"
        elif index == 2: rank_label = "🥈 2nd"
        elif index == 3: rank_label = "🥉 3rd"
        tree.insert("", tk.END, values=(rank_label, s["name"], s["marks"]))

    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- MAIN MENU GUI ---
window = tk.Tk()
window.title("Student Record System")
window.geometry("400x450")

tk.Label(window, text="Student Record System", font=("Arial", 18, "bold")).pack(pady=20)

# Buttons Linked to Functions
tk.Button(window, text="➕ Add Student", width=25, command=open_add_student_window).pack(pady=5)
tk.Button(window, text="📋 View Students", width=25, command=view_students).pack(pady=5)
tk.Button(window, text="📊 Sort by Marks", width=25, command=sort_by_marks).pack(pady=5)
tk.Button(window, text="🔤 Sort by Name", width=25, command=sort_by_name).pack(pady=5)
tk.Button(window, text="🏆 Show Rankings", width=25, bg="#FFD700", command=show_rankings).pack(pady=5)
tk.Button(window, text="❌ Exit", width=25, command=window.quit).pack(pady=20)

window.mainloop()