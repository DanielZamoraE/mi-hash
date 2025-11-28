import argparse
from mi_hash.core import generar_hash

VERSION = "0.1.0"

def main():
    parser = argparse.ArgumentParser(prog="mi-hash", description="Generador de hash SHA-256 (mi-hash)")
    parser.add_argument("texto", nargs="?", help="Texto a hashear. Si no se da, lee stdin.")
    parser.add_argument("--version", action="store_true", help="Muestra la versión y sale.")
    args = parser.parse_args()

    if args.version:
        print(f"mi-hash {VERSION}")
        return

    if args.texto:
        txt = args.texto
    else:
        import sys
        txt = sys.stdin.read().strip()
        if not txt:
            print("Error: No se proporcionó texto. Usa: mi-hash \"texto\" o pásalo por stdin.")
            return

    print(generar_hash(txt))

if __name__ == "__main__":
    main()
