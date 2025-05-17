# scraper.py
import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import urljoin
import time
from datetime import datetime

def scrape_scholar_profile(scholar_id):
    """
    Scrape publications from a Google Scholar profile and classify them
    """
    base_url = f"https://scholar.google.com/citations?hl=en&user=UYHadLQAAAAJ"
    publications = []
    
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    
    page = 1
    while True:
        url = f"{base_url}&pagesize=100&cstart={(page-1)*100}"
        try:
            response = session.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            entries = soup.find_all('tr', class_='gsc_a_tr')
            if not entries:
                break
                
            for entry in entries:
                title = entry.find('a', class_='gsc_a_at').text
                authors = entry.find('div', class_='gs_gray').text
                venue = entry.find_all('div', class_='gs_gray')[-1].text
                year = entry.find('span', class_='gsc_a_h').text if entry.find('span', class_='gsc_a_h') else "N/A"
                relative_link = entry.find('a', class_='gsc_a_at')['href']
                citation_link = urljoin(base_url, relative_link)
                
                publications.append({
                    'title': title,
                    'authors': authors,
                    'venue': venue,
                    'year': year,
                    'citation_link': citation_link,
                    # Default values matching your existing structure
                    'doi': '',
                    'pdf': '',
                    'bibtex': f'@article{{scholar_{year}_{len(publications)},\n  title={{{title}}},\n  author={{{authors}}},\n  journal={{{venue}}},\n  year={{{year}}}\n}}',
                    'topics': []
                })
            
            page += 1
            time.sleep(2)
            
        except Exception as e:
            print(f"Error scraping page {page}: {str(e)}")
            break
    
    return publications

def classify_publications(publications):
    """
    Classify publications into journals and conferences by year
    """
    journals = {}
    conferences = {}
    
    for pub in publications:
        year = pub['year']
        if not year.isdigit():  # Skip invalid years
            continue
            
        venue = pub['venue'].lower()
        # Classification logic
        if 'conf' in venue or 'proceedings' in venue or 'conference' in venue:
            if year not in conferences:
                conferences[year] = []
            conferences[year].append(pub)
        else:
            if year not in journals:
                journals[year] = []
            journals[year].append(pub)
    
    return {
        'journals': journals,
        'conferences': conferences
    }

def save_to_json(data, filename):
    """Save data to JSON file in data/ directory"""
    os.makedirs('data', exist_ok=True)
    filepath = os.path.join('data', filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Data successfully saved to {filepath}")

def main():
    scholar_id = "REPLACE_WITH_SCHOLAR_ID"  # Replace with actual ID
    
    print(f"Scraping Google Scholar profile for ID: {scholar_id}")
    publications = scrape_scholar_profile(scholar_id)
    
    if publications:
        classified = classify_publications(publications)
        save_to_json(classified, 'scholar.json')
        
        print(f"\nSummary:")
        print(f"Total publications: {len(publications)}")
        print(f"Journal publications: {sum(len(v) for v in classified['journals'].values())}")
        print(f"Conference publications: {sum(len(v) for v in classified['conferences'].values())}")
    else:
        print("No publications found or scraping failed.")

if __name__ == "__main__":
    main()