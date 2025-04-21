- Analyse was es für formate gibt, um produkte zu identifizieren
- Analyse was es für Tools gibt die auch schwachstellen scans und damit auch produktidentifikation machen

---

https://github.com/jeremylong/DependencyCheck/blob/505ddff92744dc8e24b89facc7151f136665e0f9/core/src/main/java/org/owasp/dependencycheck/dependency/VulnerableSoftware.java#L396
VulnerableSoftware # protected static boolean compareVersions(VulnerableSoftware vs, String targetVersion) {

https://github.com/jeremylong/DependencyCheck/blob/main/core/src/main/java/org/owasp/dependencycheck/utils/DependencyVersion.java#L235
DependencyVersion # public int compareTo(@NotNull DependencyVersion version) {

---

Papers and presentations

- Software-Identification-Ecosystem-Option-Analysis
    - https://www.cisa.gov/sites/default/files/2023-10/Software-Identification-Ecosystem-Option-Analysis-508c.pdf  
      downloaded as
      [Software-Identification-Ecosystem-Option-Analysis-508c.pdf](documents/Software-Identification-Ecosystem-Option-Analysis-508c.pdf)
- Graph-Based CPE Matching for Identification of Vulnerable Asset Configurations
    - https://dl.ifip.org/db/conf/im/im2021-ws4-grasec/213273.pdf  
      downloaded as
      [Graph-Based CPE Matching for Identification of Vulnerable Asset Configurations.pdf](documents/Graph-Based%20CPE%20Matching%20for%20Identification%20of%20Vulnerable%20Asset%20Configurations.pdf)
- Universal-Software-Product-Indentity (Thomas Schmidt, FIRSTCON23)
    - https://www.first.org/resources/papers/conf2023/FIRSTCON23-TLPCLEAR-Schmidt-Manion-Universal-Software-Product-Indentity.pdf  
      downloaded as
      [FIRSTCON23-TLPCLEAR-Schmidt-Manion-Universal-Software-Product-Indentity.pdf](documents/FIRSTCON23-TLPCLEAR-Schmidt-Manion-Universal-Software-Product-Indentity.pdf)
    - https://www.karlton.org/2017/12/naming-things-hard/
    - Name ≠ Identity, Intrinsic vs extrinsic naming scheme
    - SWID

---

Other websites and projects

- [OWASP Web Security Testing Guide's "Naming Schemes": describes SWID, CPE, and PURL to uniquely identify software vulnerabilities](https://owasp.org/www-project-web-security-testing-guide/latest/5-Reporting/02-Naming_Schemes)
- [How does OSS Index manage to map these CVEs to Maven packages, as from a quick glance nothing in the CVEs looks like (complete) Maven coordinates](https://github.com/aboutcode-org/vulnerablecode/issues/279#issuecomment-740439444)

---

PURL 2 CPE

- [PURL to CPE Relationship mapping project](https://github.com/scanoss/purl2cpe)
- https://raw.githubusercontent.com/scanoss/purl2cpe/refs/heads/main/purl2cpe.db.zip

---

Thomas Schmidt vom BSI:

> Product Identifikation presents one of the greatest challenges in the field of vulnerability management.
> If it is not solved, automation of vulnerability matching is not possible.

und:

> CSAF 3.0 will not be published until it is solved.

---

Automatisiertes Schwachstellen-Matching Optimierung - Deep Research
https://chatgpt.com/share/68063fc6-3d68-8006-b0f9-0d9f57172a2e
