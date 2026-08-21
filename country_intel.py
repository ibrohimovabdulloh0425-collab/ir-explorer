"""
Davlatlar haqidagi siyosiy, iqtisodiy va xalqaro tashkilotlar ma'lumotlarini boyituvchi modul.
"""

SCO_MEMBERS = {"UZ", "CN", "RU", "IN", "PK", "KZ", "KG", "TJ", "IR", "BY"}
NATO_MEMBERS = {"US", "GB", "FR", "DE", "TR", "IT", "CA", "ES", "PL", "NL", "BE", "GR", "PT", "CZ", "HU", "RO", "BG", "SK", "SI", "HR", "AL", "ME", "MK", "FI", "SE"}
BRICS_MEMBERS = {"BR", "RU", "IN", "CN", "ZA", "EG", "ET", "IR", "AE"}
OTS_MEMBERS = {"UZ", "TR", "AZ", "KZ", "KG"}  # Turk Davlatlari Tashkiloti
G7_MEMBERS = {"US", "GB", "FR", "DE", "IT", "CA", "JP"}
EU_MEMBERS = {"AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE"}
CSTO_MEMBERS = {"RU", "BY", "KZ", "KG", "TJ", "AM"} # KXShT

def get_organizations_list(cca2: str) -> list:
    orgs = ["BMT"]
    if cca2 in SCO_MEMBERS: orgs.append("SCO")
    if cca2 in NATO_MEMBERS: orgs.append("NATO")
    if cca2 in BRICS_MEMBERS: orgs.append("BRICS")
    if cca2 in OTS_MEMBERS: orgs.append("OTS")
    if cca2 in G7_MEMBERS: orgs.append("G7")
    if cca2 in EU_MEMBERS: orgs.append("EU")
    if cca2 in CSTO_MEMBERS: orgs.append("CSTO")
    return orgs

def enrich(c: dict) -> dict:
    cca2 = (c.get("cca2") or "").upper()
    pop = c.get("population") or 0
    
    gdp_usd = c.get("gdp_usd") or round((pop * 4500) / 1e9, 2)
    gdp_per_capita = c.get("gdp_per_capita") or (round((gdp_usd * 1e9) / pop) if pop > 0 else 0)

    org_list = get_organizations_list(cca2)
    org_str = ", ".join(org_list)

    return {
        "gdp_usd": gdp_usd,
        "gdp_per_capita": gdp_per_capita,
        "government": c.get("government") or "Respublika",
        "leader": c.get("leader") or "Davlat rahbari",
        "visa_type": c.get("visa_type") or ("Mahalliy" if cca2 == "UZ" else "Viza kerak"),
        "rel_uz": org_str, # Tashkilotlar ro'yxati bazaga saqlanadi
        "rel_us": c.get("rel_us") or ("NATO ittifoqchisi" if cca2 in NATO_MEMBERS else "Diplomatik aloqalar mavjud"),
        "rel_eu": c.get("rel_eu") or ("YEI a'zosi" if cca2 in EU_MEMBERS else "Hamkorlik mavjud"),
        "stability_score": c.get("stability_score") or 7,
        "stability_note": c.get("stability_note") or f"A'zolik va xalqaro maqom: {org_str}",
    }