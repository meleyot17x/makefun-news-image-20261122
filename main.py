"""THE SIGNAL TOWER untuk @meleyotcok (Akun Final 3) — NI22 Wave 7.

Penjaga berkas gambar berita gelombang ketujuh: program kecil ini
memastikan menara sinyal kami lolos gerbang ukuran, lalu menyalinnya
persis apa adanya ke folder keluaran tanpa mengubah satu byte pun.
Semua pemeriksaan gagal secara tegas dengan kode keluar 1.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

CONCEPT = "THE SIGNAL TOWER"
ACCOUNT = "@meleyotcok"
ACCOUNT_LABEL = "Akun Final 3"
BOUNTY = "news-image-20261122"
STORIES = 36
MAX_SIDE = 1024

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def digest_of(path):
    """Hitung sidik sha256 serta panjang berkas dalam satu lintasan baca."""
    hasher = hashlib.sha256()
    total = 0
    with open(path, "rb") as handle:
        while True:
            block = handle.read(65536)
            if not block:
                break
            hasher.update(block)
            total += len(block)
    return hasher.hexdigest(), total


def inspect_header(path):
    """Baca 33 byte pembuka, sahkan tanda PNG dan IHDR, kembalikan dimensi."""
    with open(path, "rb") as handle:
        head = handle.read(33)
    if len(head) < 33:
        print("Header terlalu pendek, berkas ditolak.", file=sys.stderr)
        sys.exit(1)
    if head[:8] != PNG_MAGIC:
        print("Tanda tangan PNG tidak dikenal, berkas ditolak.", file=sys.stderr)
        sys.exit(1)
    if head[12:16] != b"IHDR":
        print("Chunk IHDR tidak ditemukan, berkas ditolak.", file=sys.stderr)
        sys.exit(1)
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print("entry.png tidak ada di samping main.py.", file=sys.stderr)
        return 1

    width, height = inspect_header(source)
    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"Dimensi {width}x{height} melewati batas {MAX_SIDE}.", file=sys.stderr)
        return 1

    src_hash, src_size = digest_of(source)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(source.read_bytes())

    dst_hash, dst_size = digest_of(target)
    if dst_hash != src_hash or dst_size != src_size:
        print("Salinan tidak sama persis dengan sumber.", file=sys.stderr)
        return 1

    print(f"Concept: {CONCEPT}")
    print(f"Account: {ACCOUNT} ({ACCOUNT_LABEL})")
    print(f"Bounty: {BOUNTY}")
    print("File: entry.png")
    print(f"Size: {src_size}")
    print(f"Dim: {width}x{height}")
    print(f"SHA256: {src_hash}")
    print(f"Stories: {STORIES}")
    print("Copy verified byte-identical.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
