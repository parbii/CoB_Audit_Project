from bs4 import BeautifulSoup

# 1. Load the full file
with open("org.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# 2. Extract every single link that looks like an organization
all_orgs = []
for link in soup.find_all('a', href=True):
    if '/engage/organization/' in link['href']:
        name = link.get_text(strip=True)
        if name and len(name) > 2:
            all_orgs.append(name)

# 3. Remove duplicates and sort alphabetically
all_orgs = sorted(list(set(all_orgs)))

# 4. Print for easy Copy-Paste
print(f"--- FOUND {len(all_orgs)} ORGANIZATIONS ---")
for org in all_orgs:
    print(org)