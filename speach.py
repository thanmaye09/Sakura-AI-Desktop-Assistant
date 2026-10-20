"""Offline text reading using the operating system's speech engine."""


def speak_text(text: str) -> None:
    if not text.strip():
        raise ValueError("Enter some text to read")
    try:
        import pyttsx3
    except ImportError as exc:
        raise RuntimeError("Install text-to-speech requirements first") from exc
    engine = pyttsx3.init()
    engine.setProperty("rate", 165)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


