import uuid
from dataclasses import dataclass

@dataclass(frozen=True)  # frozen=True macht die Klasse hashable für Sets/Dicts
class Person:
    id: uuid.UUID
    vorname: str
    nachname: str
    geburtsjahr: int  # Hinzugefügt, um die Eindeutigkeit zu erhöhen

    @property
    def business_key(self):
        """
        Erzeugt einen fachlichen Schlüssel für die Duplikatprüfung.
        Kombination aus normierten Namen und Geburtsjahr.
        """
        return (self.nachname.lower(), self.vorname.lower(), self.geburtsjahr)


    def normalize_name(self, name: str) -> str:
        """
        Normalizes a name string by stripping whitespace and converting to title case.

        Args:
        name (str): The name string to normalize.

        Returns:
            str: The normalized name string.
        """
        return name.strip().title()
