from mi_hash.core import generar_hash

def test_generar_hash():
    texto = "hola"
    resultado = generar_hash(texto)
    assert isinstance(resultado, str)
    assert len(resultado) == 64
