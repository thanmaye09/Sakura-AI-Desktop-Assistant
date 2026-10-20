"""Email draft helper. Does not send messages or read an inbox."""
import re
from urllib.parse import urlencode


def mailto_url(recipient: str, subject: str, body: str) -> str:
    recipient = recipient.strip()
    if recipient and not re.fullmatch(r"[^\s@,;]+@[^\s@,;]+\.[^\s@,;]+", recipient):
        raise ValueError("Enter one valid recipient email address")
    parameters = urlencode({"subject": subject, "body": body})
    return f"mailto:{recipient}?{parameters}"
