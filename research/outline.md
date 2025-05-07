<!-- Allgemeine Länge einer Bachelorarbeit sind 50-60 Seiten (ohne Anhang) -->

# Produktidentifikation und Korrelationsformate in der Schwachstellenanalyse

<!-- TOC -->

* [Produktidentifikation und Korrelationsformate in der Schwachstellenanalyse](#produktidentifikation-und-korrelationsformate-in-der-schwachstellenanalyse)
    * [Abstract](#abstract)
    * [Einleitung](#einleitung)
        * [Hintergrund und Motivation](#hintergrund-und-motivation)
        * [Zielsetzung und Forschungsfrage(n)](#zielsetzung-und-forschungsfragen)
        * [Aufbau der Arbeit](#aufbau-der-arbeit)
    * [Hauptteil](#hauptteil)
        * [Stand der Technik](#stand-der-technik)
            * [Interne Produktmodellierung (metaeffekt)](#interne-produktmodellierung-metaeffekt)
            * [Produktidentifikationsstandards und relevante Formate](#produktidentifikationsstandards-und-relevante-formate)
            * [Analyse bestehender Produkt-Mapping Algorithmen](#analyse-bestehender-produkt-mapping-algorithmen)
        * [Analyse des metaeffekt-Schwachstellenscanners](#analyse-des-metaeffekt-schwachstellenscanners)
        * [Verwandte Arbeiten](#verwandte-arbeiten)
            * [Aktuelles Korrelationsformat](#aktuelles-korrelationsformat)
            * [Schwächen und Herausforderungen des aktuellen Korrelationsformats](#schwächen-und-herausforderungen-des-aktuellen-korrelationsformats)
        * [Anforderungen an das neue YAML-Korrelationsformat](#anforderungen-an-das-neue-yaml-korrelationsformat)
        * [Konzeption und Implementierung des neuen Formats](#konzeption-und-implementierung-des-neuen-formats)
            * [Modellierungsansatz für Produktidentifikation](#modellierungsansatz-für-produktidentifikation)
            * [Implementierung und Integration](#implementierung-und-integration)
            * [Beispielhafte Anwendung](#beispielhafte-anwendung)
        * [Evaluation](#evaluation)
            * [Evaluationsmethodik](#evaluationsmethodik)
            * [Ergebnisse und Diskussion](#ergebnisse-und-diskussion)
    * [Schluss](#schluss)
        * [Zusammenfassung der Arbeit](#zusammenfassung-der-arbeit)
        * [Ausblick](#ausblick)

<!-- TOC -->

## Abstract

<!--
Fasst die Arbeit sehr kurz zusammen (< 20 Zeilen). Es wird kurz der Hintergrund und das Problem erläutert sowie die
Lösung und das Ergebnis vorgestellt. Ein zusätzlicher englischer Abstract hilft auch auswärtigen Lesern, einen
Einblick zu bekommen und sollte nicht fehlen.
-->

## Einleitung

### Hintergrund und Motivation

https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Cyber_Resilience_Act/cyber_resilience_act_node.html  
Der CRA fordert ab 11. Juni 2026, dass Unternehmen eine Liste an Schwachstellen und Security Incidents führen müssen, um
jederzeit darüber Auskunft geben zu können.

Das bisher verwendete Korrelationsformat verursacht sowohl intern als auch extern einige Leidenspunkte, die wir mit
einer neuen Version beheben wollen.

### Zielsetzung und Forschungsfrage(n)

Herleitung der Kernfrage:

Wir starten mit der ursprünglichen Frage, die man als Software-Hersteller und Verteiler haben kann:

- Von welchen öffentlich bekannten Schwachstellen ist unser Produkt, das aus Open/Closed-Source-Komponenten besteht,
  betroffen?

Schwachstellen und Sicherheitsratgeber werden von diversen Quellen herausgegeben.
Jeder Eintrag hat neben seinen Metadaten wie Beschreibungen noch Matching-Informationen angehängt,
die dazu genutzt werden könne, um herauszufinden, ob man von diesen betroffen ist.

Allerdings nutzen die meisten unterschiedlichen Herausgeber verschiedene Weisen,
wie Produkte bei ihnen repräsentiert werden.

Daraus leitet sich die Frage ab:

- Wie können wir zu unseren eingesetzten Produkten herausfinden, welchen CPEs, PURLs und anderen Repräsentationen diese
  darstellen?

Weitergedacht bringt uns das zu:

- Zu einem gegebenen Produkt in einer beliebigen Repräsentation, welche weiteren Repräsentationen gibt es, die das
  gleiche reale Produkt darstellen?

Und dies führt uns auf die Fragestellung, die hier in dieser Arbeit beantwortet werden soll:

- Wie kann ein Produkt-Graph aufgebaut werden, der es erlaubt, zwischen unterschiedlichen Repräsentationen eines
  Produktes zu wechseln?

Wenn man einen solchen Graphen erst einmal aufgestellt hat, dann können auch weitere Fragestellungen außerhalb des
Schwachstellen-Scanning-Kontexts beantwortet werden: Etwa welchen End of Life-Identifier ein Produkt hat.
Natürlich gibt es weitere Komplexitäten mit komplexeren Produktverhältnissen, ist als Startpunkt gedacht.

### Aufbau der Arbeit

- Zunächst werden die unterschiedlichen Formate vorgestellt, die die metaeffekt in diesem Kontext berühren
- Dann werden existierende Scanner und Matching-Algorithmen vorgestellt, die bereits Teile einer gesuchten Lösung
  implementieren
- Daraufhin wird das vorhandene Korrelationssystem vorgestellt und die Herausforderungen damit aufgeführt
- Anschließend werden daraus Anforderungen an das neue System abgeleitet, Qualitätsmetriken aufgestellt anhand denen
  dieses geprüft werden kann und der Ansatz für die Implementierung erklärt
- Abschließend wird noch die Implementierung vorgestellt und anhand von den Qualitätsmetriken geprüft.

## Hauptteil

### Stand der Technik

#### Interne Produktmodellierung (metaeffekt)

https://github.com/org-metaeffekt/metaeffekt-core/blob/master/libraries/ae-inventory-processor/src/main/java/org/metaeffekt/core/inventory/processor/model/Inventory.java  
Die metaeffekt verwendet ein proprietäres Format ("Inventory"), um Software-Komponenten, Schwachstellen und weitere
Daten zu verwalten.

https://github.com/org-metaeffekt/metaeffekt-core/blob/master/libraries/ae-inventory-processor/src/main/java/org/metaeffekt/core/inventory/processor/model/Artifact.java  
Software-Komponenten werden als eine Liste an "Artefakten" erfasst, die jeweils eine Map\<String, String> darstellen
und damit unter bekannten Keys beliebige Werte ablegen können.

Zwei Beispiele:

| Id                              | Component                 | Version | Type       | ... |
|---------------------------------|---------------------------|---------|------------|-----|
| react-transition-group-4.4.5    | react-transition-group    | 4.4.5   | npm-module |     |
| @types/debug-4.1.12             | @types/debug              | 4.1.12  | npm-module |     |
| get-nonce-1.0.1                 | get-nonce                 | 1.0.1   | npm-module |     |
| micromark-core-commonmark-2.0.3 | micromark-core-commonmark | 2.0.3   | npm-module |     |

| Id                        | Component    | Group Id                      | Version     | Checksum                         | ... |
|---------------------------|--------------|-------------------------------|-------------|----------------------------------|-----|
| alternatives-1.24         | alternatives |                               | 1.24        |                                  |     |
| angus-core-2.0.1.jar      |              | org.eclipse.angus             | 2.0.1       |                                  |     |
| arjuna-7.0.0.Final.jar    |              | org.jboss.narayana.arjunacore | 7.0.0.Final |                                  |     |
| basesystem-11             | basesystem   |                               | 11          |                                  |     |
| bash-5.1.8                | bash         |                               | 5.1.8       |                                  |     |
| bcprov-jdk18on-1.78.1.jar |              |                               | 1.78.1      | 9646d6d9c087fd408fafe0e3cfe56c25 |     |

Die relevantesten Felder sind:

- `Id`: entweder der **Dateiname** oder **Paketname mit Version mit "-" getrennt**, oder aber ein **benutzerdefinierter
  Komponentenname** (selten)
- `Component`: der Artefakt-name
- `Version`
- `Type`: Die "Art" des Artefakts, "npm-module", etc.
- `Ecosystem`: "maven", "npm", "pyPi", etc., etwa gleichzusetzen mit einem Paketmanager
- `Group Id`: Maven-spezifisch
- uvm. siehe
  [Artifact.Attribute](https://github.com/org-metaeffekt/metaeffekt-core/blob/master/libraries/ae-inventory-processor/src/main/java/org/metaeffekt/core/inventory/processor/model/Artifact.java#L40)
  für eine Liste der häufigsten.

Dieses System kommt allerdings nicht ohne seine Herausforderungen, und es sind bereits lange Änderungen an diesem
geplant:

- Das Type-Feld wird nicht konsistent in allen Prozessen gesetzt, und es gibt auch nur wenige Types die überhaupt
  gesetzt werden können. Hier muss eine Hierarchisch-aufgebaute Erweiterung des Type-Systems stattfinden.
  Der Type ist vor allem im Vulnerability-Scanning-Kontext wichtig, da in Schwachstelldatenbanken oft als Ökosystem ein
  äquivalenter Repräsentant verwendet wird.
  Intern gibt es bereits mehrere Tickets, die Details dazu spezifizieren, der Großteil liegt allerdings noch vor uns.
- Das Feld `Group Id` soll in Zukunft unter einem generischeren Bezeichner `Namespace` geführt werden,
  sodass wir uns näher an den PURL-Bezeichnern bewegen.
- Oft ist es so, dass weder die `Id`, noch das `Component` den "wahren" Namen einer Komponente enthalten. Hier soll
  ebenfalls ein neues Feld angelegt werden, dass diesen führen wird. Hier müssen intern noch entsprechende Definitionen
  aufgestellt werden.
- Generell ist es momentan oft schwer ein scharfes Matching betreiben zu können, da die nötigen Felder entweder nicht
  vorhanden/ausgefüllt sind, oder nicht genügend Detail enthalten, um genaue Ableitungen zu bilden. So sind im Moment
  die Prozesse eher darauf ausgelegt, zu viele False-Positives zu generieren als False-Negatives und damit Information
  zu verlieren. Mit den oben-beschriebenen Änderungen soll dies sich zum Besseren ändern, aber auch das neue
  Korrelationssystem soll hierbei unterstützen.

<!--
Interne Tickets:

- https://metaeffekt.atlassian.net/browse/AE-985
- https://metaeffekt.atlassian.net/browse/AE-556
-->

#### Produktidentifikationsstandards und relevante Formate

Nach [Software Identification Ecosystem Option Analysis](https://www.cisa.gov/sites/default/files/2023-10/Software-Identification-Ecosystem-Option-Analysis-508c.pdf)
gibt es zwei Arten von Produkt-Identifiers:

**Inherent Identifiers**:  
ergeben sich ausschließlich aus den Eigenschaften eines Paketes, die Kennzeichnung kann ohne
weitere Parteien aus dem Inhalt direkt abgeleitet werden. Sie werden von keiner Authority definiert.
In der Forschungsarbeit sprechen sie hier ausschließlich von Hashes und Hash-Techniken, die auf eine lokale Datei oder
ein Verzeichnis angewandt werden können.  
Leider enthalten die wenigsten Schwachstelldatenbanken konsistent nützliche Matching-Informationen in Form von Hashes,
und es kommt für uns nicht infrage, erst alle Software-Pakete der Welt zu hashen und zu diesen die entsprechenden
anderen Repräsentationen zuzuordnen.  
Daher ist diese Art von Identifier nicht zu nützlich in unserem Kontext.

**Defined Identifiers**:
eerden entweder von einer Authority verwegen (CPE, MS-Product Ids, etc.), oder ergeben sich aus einer Kombination aus
intrinsischen Eigenschaften eines Pakets und einer weiteren externen Information, wie bei PURL mit den Paket-Managern.
Diese Art wird von allen Quellen in irgendeiner Form unterstützt, daher wird der Fokus auf diesen liegen.

Im Anschluss zu dieser ersten Einordnung werden die Formate vorgestellt, die im Laufe der Arbeit relevanz finden.
Diese Formate werden in irgendeiner Form von allen Schwachstell- oder anderen Produkt-zentrischen Datenbanken verwendet
und sind damit für uns wichtig zu erknennen.

Formate:

- CPE, PURL
- OSV, CSAF
- MSRC-Product Ids, EOL Ids
- Hashes
- ...

weitere werden im Laufe der Analyse festgestellt.

#### Analyse bestehender Produkt-Mapping Algorithmen

Vorstellen von existierenden Algorithmen, die versuchen zu Produkten eine CPE oder andere Repräsentationen zuzuordnen.

- [DependencyCheck](https://github.com/dependency-check/DependencyCheck/blob/29fb1112845dd7130b6de03382c5a3c6f672a41c/core/src/main/java/org/owasp/dependencycheck/analyzer/CPEAnalyzer.java#L261)

weitere werden im Laufe der Analyse festgestellt.

### Analyse des metaeffekt-Schwachstellenscanners

Vorstellen der Logik, die aktuell bei der metaeffekt dazu verwendet wird, um zu Artefakten die entsprechenden CPEs zu
"erraten".
Dieser Algorithmus ist der Grund, warum das originale Korrelationssystem nötig geworden ist, da wir eine Möglichkeit
gebraucht haben, um die Ergebnisse hiervon zu korrigieren.

<!-- Internal Repository: https://github.com/org-metaeffekt/metaeffekt-artifact-analysis/blob/main/modules/ae-artifact-analysis/src/main/java/com/metaeffekt/artifact/enrichment/vulnerability/CpeDerivationUtilities.java#L91 -->

Im Weiteren wird noch der Matching-Algorithmus für Schwachstellen kurz erklärt.
Hierrauf liegt allerdings nicht der Fokus und es werden höchstwahrscheinlich eher nur die Artefakt-Felder aufgeführt,
die relevant sind, wie sie verwendet werden, woher sie kommen und erklärt welche Merkmale sie haben müssen, um nützlich
zu sein.

### Verwandte Arbeiten

TBD

#### Aktuelles Korrelationsformat

- Die Notwendigkeit und der Ursprung des Formats begründen
- Erklären des YAML-Formats und die Funktionsweise
- Zeigen eines Beispiels
- Ausmaße des aktuellen Korrelationsdatensets (Anzahl Einträge, Produkte, ...)

#### Schwächen und Herausforderungen des aktuellen Korrelationsformats

In diesem Kapitel wird eine große Liste an Problemen aufgeführt, die ich und meine Kollegen mit dem Format
aus einer Nutzerperspektive (Erstellung, Pflege) und aus Prozesssicht haben.

Hier gibt es intern bereits eine Liste, die über die letzten Monate und teils bereits Jahre erstellt wurde, diese wird
mit dem aktuellen Wissensstand konsolidiert und entsprechend erweitert.

<!-- Internal Link: https://metaeffekt.atlassian.net/wiki/spaces/KM/pages/3037888514/TBD+New+Correlation+System -->

### Anforderungen an das neue YAML-Korrelationsformat

Aus den Herausforderungen des vorherigen Kapitels werden in diesem Kapitel zunächst einmal einige nichtfunktionale
Anforderungen abgeleitet.
Diese decken sich bereits teilweise mit den Punkten unten.

Um die Qualität der Daten über die Zeit sichern zu können, werden diverse Qualitätsmetriken aufgestellt.
Unter anderem gibt hier diese Ansätze:

- Vollständige Abdeckung der vorhandenen Korrelationsdatenbank
- Innere Konsistenz: Zu jeder Repräsentation, die durch das Modell identifiziert werden soll, darf maximal eine
  eindeutige Identifikation stattfinden und es darf keine losen Knoten geben
- Datensatz erklärt sich selbst: Zu jedem Eintrag und jeder Verbindung muss es eine Begründung jeglicher Art geben
- Ein sich selbst prüfender Datensatz: Nachdem ein Datensatz manuell geprüft wurde, werden alle Identifikationen in
  einem separaten Datensatz abgelegt, um bei zukünftigen Änderungen automatisch geprüft werden zu können. So soll
  gegeben sein, dass die Identifikation eines bekannten Produktes nicht einfach so ändern kann, ohne, dass man es
  mitbekommen würde.

### Konzeption und Implementierung des neuen Formats

#### Modellierungsansatz für Produktidentifikation

Aus den Anforderungen, der Literaturrecherche, der Format-analyse und Analyse von anderen Systemen wird hier konkret das
neue Identifikationssystem aufgebaut.

#### Implementierung und Integration

Implementierungsdetails.

#### Beispielhafte Anwendung

Anhand eines/mehreren konkreten Testfällen zeigen, wie die neuen Zuordnungen funktionieren.

### Evaluation

#### Evaluationsmethodik

#### Ergebnisse und Diskussion

## Schluss

### Zusammenfassung der Arbeit

### Ausblick
