from fastmcp import FastMCP
import threading
import tkinter as tk
from tkinter import messagebox

mcp = FastMCP("email-demo")


def show_popup(title: str, message: str):
    """
    opens a popup with the given title and message in a separate 
    thread to avoid blocking the main thread.
    """
    def _popup():
        root = tk.Tk()
        root.withdraw()  # esconde janela principal
        messagebox.showinfo(title, message)
        root.destroy()

    threading.Thread(target=_popup).start()


@mcp.tool()
def send_email(to: str, subject: str, body: str) -> str:
    """
    Simulation of sending an email. In a real implementation,
    this would integrate with an email service.

    Args:
        to: recipient
        subject: subject
        body: content
    """
    msg = f"To: {to}\nSubject: {subject}\n\n{body}"

    show_popup("📧 Fake Email Sent", msg)

    return f"Email sent to {to} (simulated)"


if __name__ == "__main__":
    mcp.run()