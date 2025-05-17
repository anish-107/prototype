import json
import os
from flask import current_app

def load_publications():
    """Load and combine all publication data from JSON files"""
    data = {
        'journals': {},
        'conferences': {},
        'scholar': []
    }

    # Load manual journals
    try:
        with open(os.path.join(current_app.root_path, 'data', 'manual_journals.json'), 'r', encoding='utf-8') as f:
            data['journals'] = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, UnicodeDecodeError) as e:
        current_app.logger.error(f"Error loading manual journals: {str(e)}")

    # Load manual conferences
    try:
        with open(os.path.join(current_app.root_path, 'data', 'manual_conferences.json'), 'r', encoding='utf-8') as f:
            data['conferences'] = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, UnicodeDecodeError) as e:
        current_app.logger.error(f"Error loading manual conferences: {str(e)}")

    # Load scraped scholar data
    try:
        with open(os.path.join(current_app.root_path, 'data', 'scholar.json'), 'r', encoding='utf-8') as f:
            scholar_data = json.load(f)
            data['scholar'] = scholar_data.get('all_publications', [])
            
            # Merge scholar journals
            for year, pubs in scholar_data.get('journals', {}).items():
                if year not in data['journals']:
                    data['journals'][year] = []
                data['journals'][year].extend(pubs)
            
            # Merge scholar conferences
            for year, pubs in scholar_data.get('conferences', {}).items():
                if year not in data['conferences']:
                    data['conferences'][year] = []
                data['conferences'][year].extend(pubs)
                
    except (FileNotFoundError, json.JSONDecodeError, UnicodeDecodeError) as e:
        current_app.logger.error(f"Error loading scholar data: {str(e)}")

    return data
