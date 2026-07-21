import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
import logging
import os
import time


# =====================================================
# CONFIGURATION
# =====================================================

APP_NAME = "Software Factory Tool"
APP_VERSION = "2.0.0"
LICENSE_STATUS = True

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# =====================================================
# LICENSE
# =====================================================

def check_license():
    return LICENSE_STATUS


# =====================================================
# MAIN APPLICATION
# =====================================================

class SoftwareFactoryApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.selected_file = None

        self.title(f"{APP_NAME} v{APP_VERSION}")
        self.geometry("800x550")
        self.minsize(700, 500)

        logging.info("Application started")

        self.create_widgets()

    # =================================================
    # UI
    # =================================================

    def create_widgets(self):

        self.title_label = ctk.CTkLabel(
            self,
            text=APP_NAME,
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(25, 10))

        self.description_label = ctk.CTkLabel(
            self,
            text="Professional Desktop Utility Framework",
            font=("Arial", 14)
        )
        self.description_label.pack(pady=(0, 20))

        self.file_button = ctk.CTkButton(
            self,
            text="📂 Select File",
            width=220,
            command=self.select_file
        )
        self.file_button.pack(pady=10)

        self.file_label = ctk.CTkLabel(
            self,
            text="No file selected",
            wraplength=700
        )
        self.file_label.pack(pady=10)

        self.run_button = ctk.CTkButton(
            self,
            text="▶ Run Tool",
            width=220,
            state="disabled",
            command=self.start_processing
        )
        self.run_button.pack(pady=15)

        self.progress = ctk.CTkProgressBar(
            self,
            width=500
        )
        self.progress.pack(pady=15)
        self.progress.set(0)

        self.status_label = ctk.CTkLabel(
            self,
            text="Status: Ready"
        )
        self.status_label.pack(pady=10)

        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.pack(
            fill="x",
            padx=20,
            pady=20
        )

        self.info_label = ctk.CTkLabel(
            self.info_frame,
            text=(
                f"Version: {APP_VERSION}\n"
                f"License: Active\n"
                f"Log File: app.log"
            )
        )

        self.info_label.pack(pady=15)

    # =================================================
    # FILE SELECTION
    # =================================================

    def select_file(self):

        file_path = filedialog.askopenfilename()

        if not file_path:
            return

        self.selected_file = file_path

        self.file_label.configure(
            text=f"Selected File:\n{file_path}"
        )

        self.run_button.configure(state="normal")

        self.status_label.configure(
            text="Status: File Loaded"
        )

        logging.info(f"File selected: {file_path}")

    # =================================================
    # THREAD START
    # =================================================

    def start_processing(self):

        if self.selected_file is None:

            messagebox.showwarning(
                "Warning",
                "Please select a file first."
            )

            return

        self.run_button.configure(state="disabled")

        worker = threading.Thread(
            target=self.run_tool,
            daemon=True
        )

        worker.start()

    # =================================================
    # MAIN LOGIC
    # =================================================

    def run_tool(self):

        try:

            self.status_label.configure(
                text="Status: Processing..."
            )

            logging.info(
                f"Processing started: {self.selected_file}"
            )

            # ==========================================
            # YOUR PRODUCT LOGIC GOES HERE
            # ==========================================

            filename = os.path.basename(
                self.selected_file
            )

            for step in range(1, 101):

                time.sleep(0.03)

                self.progress.set(step / 100)

                self.after(
                    0,
                    lambda s=step:
                    self.status_label.configure(
                        text=f"Status: Processing {s}%"
                    )
                )

            # Example output file path
            output_path = (
                os.path.dirname(self.selected_file)
            )

            # ==========================================
            # END PRODUCT LOGIC
            # ==========================================

            logging.info(
                f"Processing completed: {filename}"
            )

            self.after(
                0,
                self.processing_finished,
                output_path
            )

        except Exception as e:

            logging.exception("Application error")

            self.after(
                0,
                self.processing_error,
                str(e)
            )

    # =================================================
    # SUCCESS
    # =================================================

    def processing_finished(self, output_path):

        self.progress.set(1)

        self.status_label.configure(
            text="Status: Completed"
        )

        self.run_button.configure(
            state="normal"
        )

        messagebox.showinfo(
            "Completed",
            (
                "Task completed successfully.\n\n"
                f"Output Folder:\n{output_path}"
            )
        )

    # =================================================
    # ERROR
    # =================================================

    def processing_error(self, error):

        self.status_label.configure(
            text="Status: Error"
        )

        self.run_button.configure(
            state="normal"
        )

        messagebox.showerror(
            "Error",
            error
        )


# =====================================================
# STARTUP
# =====================================================

if __name__ == "__main__":

    if check_license():

        app = SoftwareFactoryApp()
        app.mainloop()

    else:

        messagebox.showerror(
            "License Error",
            "This copy is not activated."
        )