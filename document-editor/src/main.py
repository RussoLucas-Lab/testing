class DocumentEditor:
    def __init__(self) -> None:
        self.content = ""
        self.history: list[str] = []

    def write(self, text: str) -> None:
        # Ojo: guardamos el snapshot ANTES de aplicar el nuevo texto, por lo
        # que history queda un paso atras respecto a content.
        self.history.append(self.content)
        self.content += text

    def clear(self) -> None:
        self.content = ""

    def is_empty(self) -> bool:
        return self.content == ""

    def get_last_content(self) -> str:
        if len(self.history) == 0:
            raise ValueError("No history available: no operations done yet.")

        return self.history[-1]
