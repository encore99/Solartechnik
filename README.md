# Solartechnik
Python &amp; C++ Projekt zu Solar berechnung


Um dein **48V-System** mit dem **SmartSolar MPPT 250/100-MC4 VE.CAN** und den **Trina Vertex S 450W Modulen** zu betreiben, müssen wir die maximale Anzahl an Modulen bestimmen, die du anschließen kannst. Dazu schauen wir uns die **Spannungs-** und **Stromgrenzen** des Ladereglers sowie die **Daten der Solarmodule** an.

### Technische Daten des SmartSolar MPPT 250/100-MC4 VE.CAN:
- **Maximale PV-Eingangsspannung (Voc)**: 250 V
- **Maximaler Ladestrom**: 100 A
- **Maximale PV-Leistung (bei 48V Batteriesystem)**: 5.800 W

### Daten der Trina Vertex S 450W Module:
- **Leerlaufspannung (Voc)**: 41,1 V
- **Spannung bei maximaler Leistung (Vmp)**: 34,1 V
- **Kurzschlussstrom (Isc)**: 13,88 A
- **Strom bei maximaler Leistung (Imp)**: 13,2 A
- **Nennleistung (Pmax)**: 450 W

### Berechnungen für das 48V-System:

#### 1. **Maximale Anzahl der Module in Serie (basierend auf Spannung)**
- Die maximale **Leerlaufspannung (Voc)** des Ladereglers beträgt 250 V. Um die Anzahl der Module zu berechnen, die in Serie geschaltet werden können:
\[
\text{Anzahl der Module in Serie} = \frac{250V}{41,1V} \approx 6 Module
\]
Das bedeutet, du kannst **maximal 6 Module in Serie** schalten, ohne die 250 V Grenze des Ladereglers zu überschreiten.

#### 2. **Maximale Anzahl der Module in Parallel (basierend auf Strom)**
- Der Laderegler kann einen maximalen Strom von **100 A** verarbeiten.
- Da jedes Modul einen maximalen Strom von **13,2 A** hat, kannst du berechnen, wie viele parallele Strings du anschließen kannst:
\[
\text{Anzahl der parallelen Strings} = \frac{100A}{13,2A} \approx 7,57
\]
Das bedeutet, du kannst **maximal 7 parallele Strings** anschließen.

#### 3. **Maximale Anzahl der Module (basierend auf Leistung)**
- Bei einem **48V-System** kann der Laderegler eine maximale Leistung von **5.800 W** verarbeiten. Jedes Trina-Vertex S 450W Modul liefert 450 W. Die maximale Anzahl an Modulen, die du anschließen kannst, basiert auf der Leistung:
\[
\text{Anzahl der Module (Leistung)} = \frac{5.800W}{450W} \approx 12,88
\]
Das bedeutet, dass du **maximal 12 Module** anschließen kannst, um die Leistung des Ladereglers nicht zu überschreiten.

### Ergebnis: Maximal mögliche Anzahl der Module
Du kannst in deinem System **2 Strings à 6 Module in Serie** betreiben, was insgesamt **12 Module** ergibt.

### Anschlussplan der Strings:

#### String 1 (6 Module in Serie):
1. **Positiver Anschluss Modul 1** → **Negativer Anschluss Modul 2**
2. **Positiver Anschluss Modul 2** → **Negativer Anschluss Modul 3**
3. **Positiver Anschluss Modul 3** → **Negativer Anschluss Modul 4**
4. **Positiver Anschluss Modul 4** → **Negativer Anschluss Modul 5**
5. **Positiver Anschluss Modul 5** → **Negativer Anschluss Modul 6**
6. **Positiver Anschluss Modul 6** geht zum **positiven Anschluss des Ladereglers (MPPT)**
7. **Negativer Anschluss Modul 1** geht zum **negativen Anschluss des Ladereglers (MPPT)**

#### String 2 (6 Module in Serie):
1. **Positiver Anschluss Modul 1** → **Negativer Anschluss Modul 2**
2. **Positiver Anschluss Modul 2** → **Negativer Anschluss Modul 3**
3. **Positiver Anschluss Modul 3** → **Negativer Anschluss Modul 4**
4. **Positiver Anschluss Modul 4** → **Negativer Anschluss Modul 5**
5. **Positiver Anschluss Modul 5** → **Negativer Anschluss Modul 6**
6. **Positiver Anschluss Modul 6** wird parallel zum **positiven Anschluss des Ladereglers (MPPT)** angeschlossen (zusammen mit dem positiven Anschluss des ersten Strings).
7. **Negativer Anschluss Modul 1** wird parallel zum **negativen Anschluss des Ladereglers (MPPT)** angeschlossen (zusammen mit dem negativen Anschluss des ersten Strings).

### Zusammenfassung:
- **Module pro String**: 6 Module
- **Anzahl der Strings**: 2
- **Gesamtanzahl der Module**: 12 (2 Strings à 6 Module)
- **Maximale Spannung**: 246,6 V (6 Module in Serie, Voc)
- **Maximaler Strom**: 26,4 A (2 parallele Strings, Imp)

Mit dieser Konfiguration nutzt du die maximale Kapazität deines **SmartSolar MPPT 250/100** optimal aus, ohne die Spannungs- oder Stromgrenzen zu überschreiten.
