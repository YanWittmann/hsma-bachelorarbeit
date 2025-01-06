- Analyse was es für formate gibt, um produkte zu identifizieren
- Analyse was es für Tools gibt die auch schwachstellen scans und damit auch produktidentifikation machen

---

https://github.com/jeremylong/DependencyCheck/blob/505ddff92744dc8e24b89facc7151f136665e0f9/core/src/main/java/org/owasp/dependencycheck/dependency/VulnerableSoftware.java#L396
VulnerableSoftware # protected static boolean compareVersions(VulnerableSoftware vs, String targetVersion) {

https://github.com/jeremylong/DependencyCheck/blob/main/core/src/main/java/org/owasp/dependencycheck/utils/DependencyVersion.java#L235
DependencyVersion # public int compareTo(@NotNull DependencyVersion version) {

---

- Software-Identification-Ecosystem-Option-Analysis
    - [Software-Identification-Ecosystem-Option-Analysis-508c.pdf](ref/Software-Identification-Ecosystem-Option-Analysis-508c.pdf)
- Graph-Based CPE Matching for Identification of Vulnerable Asset Configurations
    - [Graph-Based CPE Matching for Identification of Vulnerable Asset Configurations.pdf](ref/Graph-Based%20CPE%20Matching%20for%20Identification%20of%20Vulnerable%20Asset%20Configurations.pdf)
- Universal-Software-Product-Indentity (Thomas Schmidt, FIRSTCON23)
    - https://www.first.org/resources/papers/conf2023/FIRSTCON23-TLPCLEAR-Schmidt-Manion-Universal-Software-Product-Indentity.pdf
    - [FIRSTCON23-TLPCLEAR-Schmidt-Manion-Universal-Software-Product-Indentity.pdf](ref/FIRSTCON23-TLPCLEAR-Schmidt-Manion-Universal-Software-Product-Indentity.pdf)
    - https://www.karlton.org/2017/12/naming-things-hard/
    - Name ≠ Identity, Intrinsic vs extrinsic naming scheme
    - SWID

---

Thomas Schmidt vom BSI:

> Product Identifikation presents one of the greatest challenges in the field of vulnerability management.
> If it is not solved, automation of vulnerability matching is not possible.

und:

> CSAF 3.0 will not be published until it is solved.
