import hashlib

def generar_hash(texto: str) -> str:
    """
    Genera un hash SHA-256 a partir de un texto.
    """
    if not isinstance(texto, str):
        raise TypeError("El texto debe ser un string")

    return hashlib.sha256(texto.encode("utf-8")).hexdigest()
