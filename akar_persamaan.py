"""
Tugas 1 - Komputasi Numerik
Mencari akar persamaan non-linear f(x) = x^3 - x - 2 = 0
dengan empat metode: Bisection, Regula Falsi, Newton-Raphson, dan Secant.

Hanya memakai library standar Python (tidak perlu install apa pun).
"""

TOLERANSI = 1e-6
MAKS_ITERASI = 100


def f(x):
    """Fungsi yang dicari akarnya."""
    return x**3 - x - 2


def turunan_f(x):
    """Turunan pertama f(x), dipakai metode Newton-Raphson."""
    return 3 * x**2 - 1


def bisection(f, a, b, tol=TOLERANSI, maks_iter=MAKS_ITERASI):
    """Metode Bagi Dua. Syarat: f(a) dan f(b) berbeda tanda."""
    if f(a) * f(b) > 0:
        raise ValueError("f(a) dan f(b) harus berbeda tanda.")
    riwayat = []
    c = a
    for i in range(1, maks_iter + 1):
        c = (a + b) / 2
        galat = (b - a) / 2
        riwayat.append((i, c, f(c), galat))
        if f(c) == 0 or galat < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, riwayat


def regula_falsi(f, a, b, tol=TOLERANSI, maks_iter=MAKS_ITERASI):
    """Metode Posisi Palsu. Syarat: f(a) dan f(b) berbeda tanda."""
    if f(a) * f(b) > 0:
        raise ValueError("f(a) dan f(b) harus berbeda tanda.")
    riwayat = []
    c_lama = a
    c = a
    for i in range(1, maks_iter + 1):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        galat = abs(c - c_lama)
        riwayat.append((i, c, f(c), galat))
        if f(c) == 0 or (i > 1 and galat < tol):
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c_lama = c
    return c, riwayat


def newton_raphson(f, turunan, x0, tol=TOLERANSI, maks_iter=MAKS_ITERASI):
    """Metode Newton-Raphson. Butuh tebakan awal dan turunan f(x)."""
    riwayat = []
    x = x0
    for i in range(1, maks_iter + 1):
        if turunan(x) == 0:
            raise ZeroDivisionError("Turunan bernilai nol, metode gagal.")
        x_baru = x - f(x) / turunan(x)
        galat = abs(x_baru - x)
        riwayat.append((i, x_baru, f(x_baru), galat))
        x = x_baru
        if f(x) == 0 or galat < tol:
            break
    return x, riwayat


def secant(f, x0, x1, tol=TOLERANSI, maks_iter=MAKS_ITERASI):
    """Metode Secant. Butuh dua tebakan awal, tanpa turunan."""
    riwayat = []
    for i in range(1, maks_iter + 1):
        if f(x1) - f(x0) == 0:
            raise ZeroDivisionError("f(x1) - f(x0) bernilai nol, metode gagal.")
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        galat = abs(x2 - x1)
        riwayat.append((i, x2, f(x2), galat))
        x0, x1 = x1, x2
        if f(x1) == 0 or galat < tol:
            break
    return x1, riwayat


def cetak_tabel(nama, riwayat):
    """Mencetak tabel iterasi: iterasi, x, f(x), galat."""
    print(f"\n=== {nama} ===")
    print(f"{'Iter':>4} | {'x':>12} | {'f(x)':>12} | {'Galat':>12}")
    print("-" * 49)
    for i, x, fx, galat in riwayat:
        print(f"{i:>4} | {x:>12.8f} | {fx:>12.2e} | {galat:>12.2e}")


def main():
    print("Mencari akar f(x) = x^3 - x - 2 = 0")
    print(f"Toleransi galat: {TOLERANSI}")

    hasil = []

    akar, riwayat = bisection(f, 1, 2)
    cetak_tabel("Bisection (a=1, b=2)", riwayat)
    hasil.append(("Bisection", akar, len(riwayat)))

    akar, riwayat = regula_falsi(f, 1, 2)
    cetak_tabel("Regula Falsi (a=1, b=2)", riwayat)
    hasil.append(("Regula Falsi", akar, len(riwayat)))

    akar, riwayat = newton_raphson(f, turunan_f, 1.5)
    cetak_tabel("Newton-Raphson (x0=1.5)", riwayat)
    hasil.append(("Newton-Raphson", akar, len(riwayat)))

    akar, riwayat = secant(f, 1, 2)
    cetak_tabel("Secant (x0=1, x1=2)", riwayat)
    hasil.append(("Secant", akar, len(riwayat)))

    print("\n=== Perbandingan Hasil ===")
    print(f"{'Metode':<16} | {'Akar':>12} | {'Iterasi':>7} | {'f(akar)':>10}")
    print("-" * 56)
    for nama, akar, jumlah in hasil:
        print(f"{nama:<16} | {akar:>12.8f} | {jumlah:>7} | {f(akar):>10.2e}")


if __name__ == "__main__":
    main()
