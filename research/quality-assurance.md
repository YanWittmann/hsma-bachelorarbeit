# Was sind die Qualitätsmetriken für das neue Korrelationsformat?

### Vollständiger Vergleich mit den vorhandenen Korrelationsdaten

- Vollständige Abdeckung von allen Einträgen, für jeden vorhandenen Eintrag gibt es auch einen Match im neuen System

### Innere Konsistenz

- Es darf keine losen Knoten geben
- Jedes Artefakt was von außen zur identifikation reingeschickt wird, muss GENAU EIN Produkt gefunden werden

### Datensatz erklärt sich selbst

- Jeder Knoten (Produktidentifikation, Gruppierung, ...) muss eine Erklärung angehängt haben, die ihre Richtigkeit
  erklärt
- Hier wäre eine Maschinen-auswertbare Form interessant (see reason editor)

## Wie kann für die Zukunft gesichert werden, dass die Qualität konsistent bleibt?

- Durch das Anlegen eines immer weiter wachsenden Datensatzes:
    - Jeder Datensatz der manuell durchgeschickt wird
