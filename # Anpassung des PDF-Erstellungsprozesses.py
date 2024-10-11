# Anpassung des PDF-Erstellungsprozesses, um Unicode-Probleme zu vermeiden
from fpdf import FPDF

# Erstellen eines PDF-Dokuments
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Titel
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Anschlussplan der Solarstrings für 48V-System", ln=True, align='C')

# Leerer Platz
pdf.ln(10)

# Einleitung
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, 
    """Dieser Anschlussplan beschreibt, wie Sie 12 Trina Vertex S+ 450W Solarmodule in einem 48V-System anschließen, \
unter Verwendung des Victron SmartSolar MPPT 250/100-MC4 VE.CAN Ladereglers. Das System verwendet 2 Strings à 6 Module in Serie.

Maximale Systemwerte:
- Modul-Leistung: 450W
- Systemspannung: 48V
- Maximalstrom des Ladereglers: 100A
- Maximale Eingangsleistung: 5.800W
- Maximale Spannung (Voc): 250V

Anschlussdetails der Strings:
""")

# String 1 Beschreibung
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, txt="String 1 (6 Module in Serie):", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, 
    """1. Positiver Anschluss Modul 1 zu Negativer Anschluss Modul 2
2. Positiver Anschluss Modul 2 zu Negativer Anschluss Modul 3
3. Positiver Anschluss Modul 3 zu Negativer Anschluss Modul 4
4. Positiver Anschluss Modul 4 zu Negativer Anschluss Modul 5
5. Positiver Anschluss Modul 5 zu Negativer Anschluss Modul 6
6. Positiver Anschluss Modul 6 geht zum positiven Anschluss des Ladereglers (MPPT)
7. Negativer Anschluss Modul 1 geht zum negativen Anschluss des Ladereglers (MPPT)
""")

# String 2 Beschreibung
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, txt="String 2 (6 Module in Serie):", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, 
    """1. Positiver Anschluss Modul 1 zu Negativer Anschluss Modul 2
2. Positiver Anschluss Modul 2 zu Negativer Anschluss Modul 3
3. Positiver Anschluss Modul 3 zu Negativer Anschluss Modul 4
4. Positiver Anschluss Modul 4 zu Negativer Anschluss Modul 5
5. Positiver Anschluss Modul 5 zu Negativer Anschluss Modul 6
6. Positiver Anschluss Modul 6 wird parallel zum positiven Anschluss des Ladereglers (MPPT) angeschlossen.
7. Negativer Anschluss Modul 1 wird parallel zum negativen Anschluss des Ladereglers (MPPT) angeschlossen.
""")

# Fazit
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, txt="Zusammenfassung:", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, 
    """- Module pro String: 6 Module
- Anzahl der Strings: 2
- Gesamtanzahl der Module: 12 (2 Strings à 6 Module)
- Maximale Spannung (Voc): 246,6 V
- Maximaler Strom: 26,4 A (2 parallele Strings)

Mit dieser Konfiguration wird die maximale Kapazität des SmartSolar MPPT 250/100 genutzt, ohne die Spannungs- oder Stromgrenzen zu überschreiten.""")

# Speichern des PDFs
pdf_file_path = r"C:\Users\eNcore\Documents\python\Neuer Ordner\Solartechnik\pdf\Anschlussplan_Solarstrings_48V.pdf"
pdf.output(pdf_file_path)

pdf_file_path
