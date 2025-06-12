from bs4 import BeautifulSoup

def parse_product(html, source_url):
    # use built-in parser so no extra deps
    soup = BeautifulSoup(html, "html.parser")

    def sel_one(selector):
        el = soup.select_one(selector)
        return el.get_text(strip=True) if el else None

    return {
        "name":    sel_one(".product-title"),
        "price":   sel_one(".price"),
        "moq":     sel_one(".moq"),
        "supplier":sel_one(".supplier-name"),
        "location":sel_one(".location"),
        "source_url": source_url,
    }
