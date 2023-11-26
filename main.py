import tkinter as tk
from tkinter import messagebox, ttk

# 定义课程类
class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def __str__(self):
        return f"{self.course_id}: {self.course_name}"

# 定义学生类
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            return f"Course {course.course_name} added successfully."
        else:
            return f"Course {course.course_name} is already in your schedule."

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            return f"Course {course.course_name} removed successfully."
        else:
            return f"Course {course.course_name} is not in your schedule."

    def modify_course(self, old_course, new_course):
        if old_course in self.courses:
            self.courses[self.courses.index(old_course)] = new_course
            return f"Course {old_course.course_name} modified to {new_course.course_name}."
        else:
            return f"Course {old_course.course_name} is not in your schedule."

    def view_courses(self):
        return "\n".join(str(course) for course in self.courses) if self.courses else "No courses enrolled."

# 初始化数据
courses = {
    "CS101": Course("CS101", "Introduction to Computer Science"),
    "MATH201": Course("MATH201", "Advanced Mathematics"),
    "PHY301": Course("PHY301", "Physics III")
}
student = Student("12345", "Alice")

# 登录功能
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "admin":
        open_admin_panel()
    elif username == "student" and password == "student":
        open_student_panel()
    else:
        messagebox.showerror("Error", "Invalid username or password")

# 学生面板
def open_student_panel():
    student_panel = tk.Toplevel(root)
    student_panel.title("Student Panel")

    ttk.Label(student_panel, text="Select Course:").pack()
    course_combobox = ttk.Combobox(student_panel, values=list(courses.keys()))
    course_combobox.pack()

    def add_course_to_student():
        selected_course = course_combobox.get()
        if selected_course:
            course = courses[selected_course]
            result = student.add_course(course)
            messagebox.showinfo("Result", result)
        else:
            messagebox.showerror("Error", "No course selected.")
        course_combobox.set('')

    def remove_course_from_student():
        selected_course = course_combobox.get()
        if selected_course:
            course = courses[selected_course]
            result = student.remove_course(course)
            messagebox.showinfo("Result", result)
        else:
            messagebox.showerror("Error", "No course selected.")
        course_combobox.set('')

    def modify_course_for_student():
        old_course = course_combobox.get()
        new_course = new_course_combobox.get()
        if old_course and new_course and old_course != new_course:
            result = student.modify_course(courses[old_course], courses[new_course])
            messagebox.showinfo("Result", result)
        else:
            messagebox.showerror("Error", "Invalid course selection.")
        course_combobox.set('')
        new_course_combobox.set('')

    ttk.Button(student_panel, text="Add Course", command=add_course_to_student).pack()
    ttk.Button(student_panel, text="Remove Course", command=remove_course_from_student).pack()

    ttk.Label(student_panel, text="New Course for Modification:").pack()
    new_course_combobox = ttk.Combobox(student_panel, values=list(courses.keys()))
    new_course_combobox.pack()
    ttk.Button(student_panel, text="Modify Course", command=modify_course_for_student).pack()

    ttk.Button(student_panel, text="View Courses", command=lambda: messagebox.showinfo("Courses", student.view_courses())).pack()

# 管理员面板
def open_admin_panel():
    admin_panel = tk.Toplevel(root)
    admin_panel.title("Admin Panel")

    ttk.Label(admin_panel, text="Course ID:").pack()
    course_id_entry = ttk.Entry(admin_panel)
    course_id_entry.pack()

    ttk.Label(admin_panel, text="Course Name:").pack()
    course_name_entry = ttk.Entry(admin_panel)
    course_name_entry.pack()

    def add_course_to_system():
        course_id = course_id_entry.get()
        course_name = course_name_entry.get()
        if course_id and course_name:
            courses[course_id] = Course(course_id, course_name)
            messagebox.showinfo("Result", f"Course {course_name} added to system.")
            update_course_comboboxes()
        else:
            messagebox.showerror("Error", "Course ID or name is empty.")
        course_id_entry.delete(0, tk.END)
        course_name_entry.delete(0, tk.END)

    ttk.Button(admin_panel, text="Add Course to System", command=add_course_to_system).pack()

    def update_course_comboboxes():
        course_combobox['values'] = list(courses.keys())
        new_course_combobox['values'] = list(courses.keys())

# 创建主窗口
root = tk.Tk()
root.title("Course Selection System Login")

ttk.Label(root, text="Username:").pack()
username_entry = ttk.Entry(root)
username_entry.pack()

ttk.Label(root, text="Password:").pack()
password_entry = ttk.Entry(root, show="*")
password_entry.pack()

ttk.Button(root, text="Login", command=login).pack()

# 运行应用程序
root.mainloop()
