from flask import Flask, render_template, send_from_directory, current_app, jsonify, request
import subprocess
import os
import json
from utils.data_loader import load_publications

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    """
    This route handles the home page ('/') of the web application.
    It renders the 'index.html' template and passes an additional
    variable 'active_page' to mark the home link as active in the navbar.
    """
    return render_template("index.html", active_page='home')

# Projects
@app.route('/projects')
def projects():
    """
    This route handles the projects page by loading data from JSON.
    """
    try:
        # Path to your JSON file
        file_path = os.path.join(current_app.root_path, 'data', 'projects.json')
        
        # Load the JSON data
        with open(file_path, 'r', encoding='utf-8') as f:
            projects_data = json.load(f)
            
    except FileNotFoundError:
        # Handle case where JSON file doesn't exist
        current_app.logger.error(f"Projects data file not found at {file_path}")
        projects_data = []
        
    except json.JSONDecodeError:
        current_app.logger.error(f"Invalid JSON in projects data file at {file_path}")
        projects_data = []
        
    except Exception as e:
        current_app.logger.error(f"Unexpected error loading projects data: {str(e)}")
        projects_data = []
    
    return render_template("projects.html", 
                         projects=projects_data, 
                         active_page='projects')

@app.route('/protected/<path:filename>')
def protected_files(filename):
    return send_from_directory(
        'secure_docs',  
        filename,
        as_attachment=True  
    )


# Publications
@app.route('/publications')
def publications():
    # Load all publication data
    data = load_publications()
    
    # Extract years from both journal and conference publications
    years = sorted(
        set(data['journals'].keys()).union(set(data['conferences'].keys())),
        reverse=True
    )
    
    # Extract all unique topics
    topics = set()
    
    for pub_type in ['journals', 'conferences']:
        for year_pubs in data[pub_type].values():
            for pub in year_pubs:
                if 'topics' in pub:
                    topics.update(pub['topics'])
    
    return render_template('publications.html',
                         journal_pubs=data['journals'],
                         conference_pubs=data['conferences'],
                         scholar_pubs=data['scholar'],
                         years=years,
                         topics=sorted(topics),
                         active_page='publications')

# Books Section
@app.route('/books')
def books():
    """
    This route handles the books page by loading data from JSON.
    Uses consistent error handling pattern.
    """
    try:
        # Path to your JSON file
        file_path = os.path.join(current_app.root_path, 'data', 'books_data.json')
        
        # Load the JSON data
        with open(file_path, 'r', encoding='utf-8') as f:
            books_data = json.load(f)
            
    except FileNotFoundError:
        # Handle case where JSON file doesn't exist
        current_app.logger.error(f"Books data file not found at {file_path}")
        books_data = []
        
    except json.JSONDecodeError:
        current_app.logger.error(f"Invalid JSON in books data file at {file_path}")
        books_data = []
        
    except Exception as e:
        current_app.logger.error(f"Unexpected error loading books data: {str(e)}")
        books_data = []
    
    return render_template("books.html", 
                         books=books_data, 
                         active_page='books')

# News
@app.route('/news')
def news():
    """
    This route handles the news page by loading data from JSON files.
    Uses consistent error handling pattern for both news and announcements.
    """
    # Initialize default empty data
    news_items = []
    announcements = []

    try:
        # Load news data
        news_path = os.path.join(current_app.root_path, 'data', 'news_data.json')
        with open(news_path, 'r', encoding='utf-8') as f:
            news_items = json.load(f)
            if not isinstance(news_items, list):  # Validate data type
                current_app.logger.error("News data is not a list")
                news_items = []
                
    except FileNotFoundError:
        current_app.logger.error("News data file not found")
    except json.JSONDecodeError:
        current_app.logger.error("Invalid JSON in news data file")
    except Exception as e:
        current_app.logger.error(f"Error loading news data: {str(e)}")

    try:
        # Load announcements data
        ann_path = os.path.join(current_app.root_path, 'data', 'announcement_data.json')
        with open(ann_path, 'r', encoding='utf-8') as f:
            announcements = json.load(f)
            if not isinstance(announcements, list):  # Validate data type
                current_app.logger.error("Announcements data is not a list")
                announcements = []
                
    except FileNotFoundError:
        current_app.logger.error("Announcements data file not found")
    except json.JSONDecodeError:
        current_app.logger.error("Invalid JSON in announcements data file")
    except Exception as e:
        current_app.logger.error(f"Error loading announcements: {str(e)}")

    return render_template('news.html',
                         news_items=news_items,
                         announcements=announcements,
                         active_page='news')

# Responsibilities
@app.route('/responsibilities')
def responsibilities():
    """
    This route handles the responsibilities page by loading data from JSON file.
    """
    try:
        # Load responsibilities data
        resp_path = os.path.join(current_app.root_path, 'data', 'responsibility.json')
        with open(resp_path, 'r', encoding='utf-8') as f:
            responsibilities_data = json.load(f)
            if not isinstance(responsibilities_data, dict):
                current_app.logger.error("Responsibilities data is not properly formatted")
                responsibilities_data = {"responsibilities": []}
    except Exception as e:
        current_app.logger.error(f"Error loading responsibilities data: {str(e)}")
        responsibilities_data = {"responsibilities": []}

    return render_template("responsibilities.html",
                         responsibilities=responsibilities_data["responsibilities"],
                         active_page='responsibilities')


# People Section
@app.route('/people')
def people():
    """
    This route handles the people page by loading data from JSON.
    Uses consistent error handling pattern.
    """
    try:
        # Path to your JSON file
        file_path = os.path.join(current_app.root_path, 'data', 'people.json')
        
        # Load the JSON data
        with open(file_path, 'r', encoding='utf-8') as f:
            people_data = json.load(f)
            
    except FileNotFoundError:
        # Handle case where JSON file doesn't exist
        current_app.logger.error(f"People data file not found at {file_path}")
        people_data = []
        
    except json.JSONDecodeError:
        current_app.logger.error(f"Invalid JSON in people data file at {file_path}")
        people_data = []
        
    except Exception as e:
        current_app.logger.error(f"Unexpected error loading people data: {str(e)}")
        people_data = []
    
    return render_template("people.html", 
                         people=people_data, 
                         active_page='people')


# Talks and Writings
@app.route('/talks_delivered')
def talks_delivered():
    """
    This route handles the talks delivered page by loading data from JSON.
    """
    # Path to your JSON file (assuming it's in a 'data' directory)
    file_path = os.path.join(current_app.root_path, 'data', 'talks_delivered.json')
    
    try:
        # Load the JSON data
        with open(file_path, 'r', encoding='utf-8') as f:
            talks_data = json.load(f)
        
        # Sort years in descending order (newest first)
        sorted_years = sorted(talks_data.keys(), reverse=True)
        
        return render_template(
            "talks_delivered.html",
            active_page='talks_delivered',
            talks_by_year=talks_data,
            years=sorted_years  # Pass sorted years to template
        )
    
    except FileNotFoundError:
        # Handle case where JSON file doesn't exist
        current_app.logger.error(f"Talks data file not found at {file_path}")
        return render_template(
            "talks_delivered.html",
            active_page='talks_delivered',
            talks_by_year={},
            years=[]
        )


@app.route('/refresh_publications', methods=['POST'])
def refresh_publications():
    try:
        # Run the scraper script
        result = subprocess.run(['python', 'scraper.py'], capture_output=True, text=True)
        
        if result.returncode == 0:
            return jsonify({'success': True, 'message': 'Publications refreshed successfully'})
        else:
            return jsonify({'success': False, 'message': result.stderr}), 400
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
    

# Gallery
@app.route('/gallery')
def gallery():
    """
    This route handles the blogs route.
    """
    return render_template("gallery.html", active_page='gallery')


# Seminars
@app.route('/seminar_workshop')
def seminar_workshop():
    """
    This route handles the seminar/workshop page by loading data from JSON.
    Uses consistent error handling with talks_delivered route.
    """
    try:
        # Path to your JSON file
        file_path = os.path.join(current_app.root_path, 'data', 'seminar_workshop.json')
        
        # Load the JSON data
        with open(file_path, 'r', encoding='utf-8') as f:
            seminar_workshop_entries = json.load(f)
            
    except FileNotFoundError:
        # Handle case where JSON file doesn't exist
        current_app.logger.error(f"Seminar data file not found at {file_path}")
        seminar_workshop_entries = []
        
    except json.JSONDecodeError:
        current_app.logger.error(f"Invalid JSON in seminar data file at {file_path}")
        seminar_workshop_entries = []
        
    except Exception as e:
        current_app.logger.error(f"Unexpected error loading seminar data: {str(e)}")
        seminar_workshop_entries = []
    
    return render_template('seminar_workshop.html',
                        seminar_workshop_entries=seminar_workshop_entries,
                        active_page='seminar_workshop')

# Contact route
@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

@app.route('/submit_contact_form', methods=['POST'])
def handle_form_submission():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    "status": "error",
                    "message": f"Missing required field: {field}"
                }), 400
        
        # Here you would typically:
        # 1. Validate email format
        # 2. Sanitize inputs
        # 3. Send email or store in database
        
        # For now, just log the data
        print("New contact form submission:")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Subject: {data['subject']}")
        print(f"Message: {data['message']}")
        
        return jsonify({
            "status": "success",
            "message": "Thank you for your message! We will get back to you soon."
        })
        
    except Exception as e:
        print("Error processing form:", str(e))
        return jsonify({
            "status": "error",
            "message": "An error occurred while processing your request."
        }), 500

# About Me
@app.route('/about-me')
def about_me():
    '''
    This is the dedicated page for professor's about section
    '''
    return render_template('about_me.html')


# Appointment
@app.route('/appointment')
def appointment():
    return render_template('appointment_form.html')



if __name__ == '__main__':
    """
    Run the Flask application in debug mode for development purposes.
    This allows for automatic reloading and better error messages.
    """
    app.run(debug=True)
