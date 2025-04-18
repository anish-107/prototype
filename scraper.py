# scraper.py
from scholarly import scholarly

def get_scholar_publications(author_name):
    search_query = scholarly.search_author(author_name)
    author = next(search_query, None)
    
    if not author:
        return []

    author_filled = scholarly.fill(author)
    publications = author_filled.get("publications", [])

    pub_list = []
    for pub in publications[:20]:  # Limit to top 10 for display
        filled_pub = scholarly.fill(pub)
        pub_list.append({
            "title": filled_pub.get("bib", {}).get("title", "No title"),
            "year": filled_pub.get("bib", {}).get("pub_year", "N/A"),
            "venue": filled_pub.get("bib", {}).get("venue", "Unknown"),
            "link": f"https://scholar.google.com/scholar?cluster={filled_pub.get('citedby_url', '')}"
        })
    
    return pub_list
