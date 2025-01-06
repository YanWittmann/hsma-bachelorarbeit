---
geometry: margin=1.5in
---

# Bachelorarbeit Yan Wittmann

> an der Hochschule Mannheim, Fakultät für Informatik, im SS2025  
> in Kooperation mit der metaeffekt GmbH

## Hintergrund

Die metaeffekt entwickelt seit einigen Jahren eine Software zur automatisierten Identifikation von Schwachstellen in
Softwareprodukten, das mit einer offenen Lizenz frei verwendbar ist.
Dieser Scan basiert auf den Ergebnissen der vorhergehenden Software-Kompositionsanalyse, die von einem weiteren Modul
der metaeffekt durchgeführt wird.
Das langfristige Ziel der metaeffekt ist es, die Schwachstellidentifikation vollständig zu automatisieren.

Hierbei werden einige öffentlich verfügbare Datenquellen für Schwachstellinformationen,
wie die NVD und unterschiedliche OSV-DBs, aber auch Sicherheitsratgeber (Security Advisories) von Softwareherstellern
und -anbietern, genutzt um das Abgleichen von Schwachstellen zu den verwendeten Softwareprodukten zu ermöglichen.

Diese Anbieter von Schwachstellendaten unterscheiden sich allerdings stark in dem Format, in dem sie diese
Schwachstellen und Sicherheitsratgeber herausgeben.
Vor allem bei der Produktidentifikation und -zuordnung gibt es keine einheitliche Lösung, jeder setzt auf ein anderes
Format.
So nutzen einige den CPE-Standard, PURLs, interne IDs und andere wieder weitere, was für jede neue Datenquelle eine
neue Anpassung des Scanners erfordert.

Ebenso kommt es auch auf die Eingabedaten an, die der Scanner aus der Software-Kompositionsanalyse erhält.
Oft sind diese Daten nicht einheitlich, da unterschiedliche Betriebssysteme, Paketmanager, aber auch Projektweise
unterschiedliche Versionen und Namen für die gleiche Software genutzt werden und in unseren Software-Inventaren
unterschiedliche Repräsentationen erzeugen.

Diese unterschiedlichen externen Produktidentifikatoren werden im Moment automatisch mit individuellen Prüf-Regeln
analysiert und ausgewertet.
Die Erfolgsrate (true-positive matches) dieses automatisierten Prozesses ist damit allerdings sowohl stark vom Format
abhängig, das die entsprechende verwendete Datenbank verwendet, als auch von den eigenen Eingabedaten.
Denn einige der Formate, wie PURLs, sind deutlich einfacher automatisiert mit den eigenen Daten abzugleichen als andere.
So können einige, wie CPE, nur mit einer Heuristik mit einer gewissen Wahrscheinlichkeit,
und andere Formate wie die Microsoft Produkt IDs überhaupt nicht, oder nur selten automatisiert zugeordnet werden.

Darum musste bereits vor einigen Jahren ein manueller Prozess dazwischen geschoben werden, der es einem menschlichen
Assistenten ermöglicht, diesen Automatismus mit externem Wissen zu befüllen und damit zu beeinflussen.
Dieser Prozess wird bei uns "Produkt-Korrelation" genannt, mit dem Format der "Korrelationsdateien",
einem eigens erstellen YAML-Formats, das die manuelle Nachkorrektur des Automatismus ermöglicht.
Es wurde zudem ein einfaches Web-UI dazu entwickelt, das diesen Prozess für das Korrelations-Team erleichtern soll.

Dieses Format funktionierte die letzten Jahre gut genug, um nicht infrage gestellt zu werden.
Jedoch haben sind in den letzten Monaten immer mehr Probleme offenbart, die sowohl die Entwickler,
als auch das Korrelations-Team damit haben.
So ist sind zum Beispiel die vielen tausende Zeilen lange YAML-Dokumente nicht zukunftsfähig,
da sie schon lange nicht mehr übersichtlich genug sind, um gewisse Einträge einfach wiederzufinden.
Aber auch der grundlegende Ansatz hinter dem Format wird hinterfragt:
neue Konzepte für die Art und Weise, wie diese Einträge angelegt,
verwaltet und vom Programm interpretiert werden müssen entwickelt werden.

## Bachelor-Arbeitsplan

Im Zentrum der Bachelorarbeit mit der metaeffekt soll die Verbesserung der eingesetzten Schwachstellidentifikation
liegen.
Konkret soll die Arbeit die folgenden Punkte behandeln und Assets erzeugen:

- Es soll ein besseres Verständnis für das Produkt-Identifikationsökosystem erlangt werden.
- Eine Analyse von anderen Tools, die diese Daten ebenfalls konsumieren, wie diese die Daten verarbeiten.
- Die eigenen Eingabeformate sollen analysiert werden, um einen Abgleich mit den externen Formaten machen zu können.
- Schwächen des bisherigen Korrelationsformates zu identifizieren und aufzuführen.
- Endgültiges Ziel ist es, ein neues Korrelationsformat zu entwickeln, das alle neuen Anforderungen
  und die externen Formate berücksichtigt.
