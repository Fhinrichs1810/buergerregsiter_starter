from typing import Any, Dict, List, Tuple

def validiere_person(daten: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Prüft ein Personen-Dictionary auf Pflichtfelder und Plausibilität.

    Args:
        daten (dict): Ein Dictionary mit den Schlüsseln 'vorname', 'nachname',
                      'geburtsjahr' und 'wohnort'.

    Returns:
        tuple: (ist_valide (bool), fehlerliste (list[str]))
    """
    errors: List[str] = []

    # Prüfung auf leere Strings (Pflichtfelder)
    if not daten.get("vorname"):
        errors.append("Der Vorname darf nicht leer sein.")
    
    if not daten.get("nachname"):
        errors.append("Der Nachname darf nicht leer sein.")
    
    if not daten.get("wohnort"):
        errors.append("Der Wohnort darf nicht leer sein.")

    # Plausibilitätsprüfung Geburtsjahr
    jahr = daten.get("geburtsjahr")
    if not isinstance(jahr, int):
        errors.append("Das Geburtsjahr muss eine Zahl sein.")
    elif not (1900 <= jahr <= 2025):
        errors.append(f"Das Geburtsjahr {jahr} ist unplausibel (muss zwischen 1900 und 2025 liegen).")

    # Ergebnis zurückgeben: True wenn keine Fehler da sind
    return (len(errors) == 0, errors)


def parse_and_validate_birth_year(year_str: str) -> int:
    """
    Parst ein Geburtsjahr und validiert den Bereich (1900-2025).
    Raises: ValueError bei ungültigem Format oder Bereich.
    """
    try:
        year = int(year_str.strip())
    except ValueError:
        raise ValueError(f"'{year_str}' ist keine gültige Zahl.")

    if not (1900 <= year <= 2025):
        raise ValueError(f"Das Jahr {year} liegt nicht zwischen 1900 und 2025.")
        
    return year
