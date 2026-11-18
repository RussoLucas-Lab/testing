import pytest

from src.main import DocumentEditor


class TestDocumentEditor:
    def test_write(self):
        editor = DocumentEditor()
        editor.write("Hola Wachin!")
        assert editor.content == "Hola Wachin!"

    def test_history(self):
        editor = DocumentEditor()
        editor.write("Hola Wachin!")
        editor.write("Chau Wachin!")

        assert editor.history == ["", "Hola Wachin!"]

    def test_clear(self):
        editor = DocumentEditor()
        editor.write("Hola Wachin!")
        editor.clear()

        assert editor.content == ""

    def test_is_empty(self):
        editor = DocumentEditor()
        assert editor.is_empty()

    @pytest.mark.xfail(
        reason=(
            "Bug intencional en DocumentEditor.write(): hace "
            "history.append(self.content) ANTES de actualizar self.content, "
            "por lo que get_last_content() siempre devuelve el contenido "
            "previo al ultimo write, nunca el actual. Ejemplo didactico de "
            "por que el orden de las operaciones importa al manejar historial."
        )
    )
    def test_get_last_content(self):
        editor = DocumentEditor()
        editor.write("Hola Wachin!")
        editor.write("Chau Wachin!")

        assert editor.get_last_content() == "Chau Wachin!"

    def test_raise_error_if_no_history(self):
        editor = DocumentEditor()

        with pytest.raises(Exception):
            editor.get_last_content()
