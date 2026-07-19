import customtkinter as ctk
from tkinter import filedialog, messagebox
import os


# ==============================
# Application information
# ==============================

APP_NAME = "Software Factory Tool"
APP_VERSION = "1.0.0"
LICENSE_STATUS = True


# ==============================
# Main application class
# ==============================

class SoftwareFactoryApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Window configuration
        self.title(f"{APP_NAME} v{APP_VERSION}")
        self.geometry("700x450")

        # Create user interface
        self.create_widgets()


    # ==============================
    # Build interface components
    # ==============================

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text=APP_NAME,
            font=("Arial", 28)
        )

        title.pack(pady=30)


        description = ctk.CTkLabel(
            self,
            text="A professional digital tool created by Software Factory"
        )

        description.pack(pady=10)


        self.file_button = ctk.CTkButton(
            self,
            text="Select File",
            command=self.select_file
        )

        self.file_button.pack(pady=20)


        self.execute_button = ctk.CTkButton(
            self,
            text="Run Tool",
            command=self.run_tool
        )

        self.execute_button.pack(pady=20)


        self.status_label = ctk.CTkLabel(
            self,
            text="Ready"
        )

        self.status_label.pack(pady=20)



    # ==============================
    # File selection
    # ==============================

    def select_file(self):

        file_path = filedialog.askopenfilename()

        if file_path:

            self.selected_file = file_path

            self.status_label.configure(
                text=f"Selected: {os.path.basename(file_path)}"
            )


    # ==============================
    # Main product functionality
    # Replace this function with your app logic
    # ==============================

    def run_tool(self):

        if not hasattr(self, "selected_file"):

            messagebox.showwarning(
                "No file",
                "Please select a file first."
            )

            return


        # ---------------------------------
        # PRODUCT LOGIC GOES HERE
        #
        # Example:
        # - Convert images
        # - Merge PDFs
        # - Clean Excel files
        # - Organize folders
        #
        # This section changes for every app.
        # ---------------------------------


        messagebox.showinfo(
            "Completed",
            "Your task has been completed successfully!"
        )


# ==============================
# License verification placeholder
# ==============================

def check_license():

    # Later this can connect to:
    # - Online license server
    # - Payment platform API
    # - Activation keys

    if LICENSE_STATUS:
        return True

    return False



# ==============================
# Application startup
# ==============================

if __name__ == "__main__":

    if check_license():

        app = SoftwareFactoryApp()
        app.mainloop()

    else:

        messagebox.showerror(
            "License Error",
            "This copy is not activated."
        )