# SPM Browser Updates

Öffentliche Verteilung der signierten SPM-Browser-Updates. Das private Quellprojekt liegt in [SonyPlaystationModdingBrowser](https://github.com/lintopino-dotcom/SonyPlaystationModdingBrowser).

## APK herunterladen

[Neueste Browser-Veröffentlichung öffnen](https://github.com/lintopino-dotcom/SPM-Browser-Updates/releases/latest) und unter **Assets** die Datei `SPM-Browser-….apk` auswählen.

Stand **29. Oktober 2026**: Die aktuelle Veröffentlichung ist [SPM Browser 19.11.3](https://github.com/lintopino-dotcom/SPM-Browser-Updates/releases/tag/v19.11.3). Version 19.9.0 ist eine ältere Testveröffentlichung.

## Update-Feed

Der automatische Update-Feed liegt unter:

https://github.com/lintopino-dotcom/SPM-Browser-Updates/releases/latest/download/manifest.json

Die App muss diesen Feed verwenden und die signierten Metadaten prüfen. Die Metadaten haben ein Ablaufdatum; ihre Erneuerung erfordert den privaten Release-Schlüssel. Dieser Schlüssel wird nicht in diesem öffentlichen Repository gespeichert.

## Aufbau

| Pfad | Zweck |
| --- | --- |
| `manifest.json` | Signierte Update-Metadaten |
| `releases/<version>/` | Teile der jeweiligen Veröffentlichung |
| `releases/assemble-<version>.py` | Zusammensetzen der Veröffentlichungsdateien |
| `.github/workflows/publish.yml` | Zusammensetzen, Prüfen und Veröffentlichen der aktuellen Version |
| `release-parts/` | Teile einer früheren Veröffentlichung |

Der Veröffentlichungsworkflow prüft die Signatur und anschließend den öffentlichen Download samt APK-Prüfsumme. Die Release-Hinweise zu 19.11.3 nennen einen noch ausstehenden Xperia-Gerätetest und eine noch ausstehende Akkumessung.

## Weitere SPM-Projekte

- [Browser, Galerie und Dateimanager: Quellprojekt](https://github.com/lintopino-dotcom/SonyPlaystationModdingBrowser)
- [SPM Panorama](https://github.com/lintopino-dotcom/PanoramaApp)
