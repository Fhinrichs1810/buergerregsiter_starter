from typing import List, Tuple
from .validation import validiere_person
from .models import Person
from .validation import parse_and_validate_birth_year


class Buergerregister:
    """
    Verwaltet eine Liste von Personen im Arbeitsspeicher (In-Memory).
    """

    def __init__(self):
        # Interne Liste zur Speicherung der Person-Objekte
        self._personen: List[Person] = []

    def add(self, person: Person) -> Tuple[bool, str]:
        """
        Fügt eine Person hinzu, sofern sie valide ist und noch nicht existiert.

        Returns:
            Tuple[bool, str]: (Erfolg, Nachricht/Fehlergrund)
        """
        # 1. Validierung aufrufen (Umwandlung in Dict für den Validator)
        ok, errors = validiere_person(person.__dict__)
        if not ok:
            # Fehlerliste zu einem String zusammenbauen
            return False, "Validierungsfehler: " + ", ".join(errors)

        # 2. Duplikatprüfung (Vorname + Nachname)
        # Wir nutzen einen Generator-Ausdruck für Effizienz
        if any(p.nachname == person.nachname and p.vorname == person.vorname for p in self._personen):
            return False, "Warnung: Diese Person existiert bereits (Duplikat)."

        # 3. Speichern
        self._personen.append(person)
        return True, "Person erfolgreich hinzugefügt."

    def list(self) -> List[Person]:
        """Gibt eine Kopie der aktuellen Personenliste zurück."""
        return list(self._personen)

    def find(self, nachname: str) -> List[Person]:
        """Sucht Personen anhand des Nachnamens (Groß-/Kleinschreibung wird beachtet)."""
        # List Comprehension für Filterung
        return [p for p in self._personen if p.nachname == nachname]
    
    


    
    
    
