from flask import Flask, render_template, send_from_directory
from scraper import get_scholar_publications

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
    This route handles the projects page ('/projects') of the web application.
    It renders the 'projects.html' template.
    """
    # Project List
    PROJECTS = [
    {
        "id": "quantum-computing",
        "title": "Artificial Intelligence Based Techniques",
        "status": "ongoing",
        "year": "2023-Present",
        "funding": " Rs. 20,40, 240/-",
        "description": "Design and Development of Agriculture-Artificial Intelligence Based Techniques for Saffron Production in India",
        "image": "slide1.jpg", # Image
        "team": ["Ranjeet Kumar Rout"],
        "tags": ["Artificial Intelligence", "ML"],
        "patent": False,
        "patent_no": "",
        "sponsored": True,
        "sponsored_by": "DST iHub - IIT ROPAR"
    },
    {
        "id": "ai-healthcare",
        "title": "Analysis and prediction of disease-relevant mutations",
        "status": "completed",
        "year": "2020-2022",
        "funding": " Rs. 3,00,000/- ",
        "description": "Deep learning models for lung cancer detection...",
        "image": "ai-medicine.jpg",
        "team": ["Ranjeet Kumar Rout"],
        "tags": ["Computer Vision", "Medical AI"],
        "sponsored": True,
        "sponsored_by": "TEQIP-III"

    },
    {
        "id": "ai-healthcare",
        "title": "Action Plan for Municipal Solid Waste Management",
        "status": "completed",
        "year": "2020-2022",
        "funding": " Rs. 7,80,000/-",
        "description": "Action Plan for Municipal Solid Waste Management for the City of Srinagar using Machine Learning Identification and Segregation",
        "image": "ai-medicine.jpg",
        "team": ["Ranjeet Kumar Rout"],
        "tags": ["Computer Vision", "Medical AI"],
        "sponsored": True,
        "sponsored_by": "JKST&IC,  DST, J&K"
        
    },
    {
        "id": "ai-healthcare",
        "title": "facial emotion recognition",
        "status": "completed",
        "year": "2021",
        "funding": "",
        "description": "Implementation of facial emotion recognition system using deep neural network approaches and its application",
        "image": "ai-medicine.jpg",
        "team": ["Ranjeet Kumar Rout, Saiyed Umer, and Amrit Lal Sangal"],
        "tags": ["Deep neural network"],
        "patent": True,
        "patent_no": "202111012711",
        "sponsored": False,
        "sponsored_by": ""
        
    },
    {
        "id": "ai-healthcare",
        "title": "Systems and methods for facilitating biometric recognition",
        "status": "completed",
        "year": "2020-2022",
        "funding": "",
        "description": "Systems and methods for facilitating biometric recognition.(United States, Granted)",
        "documents": [{"name": "Research Paper", "url": "/static/docs/DOC1.pdf", "icon": "file-pdf"}],
        "image": "ai-medicine.jpg",
        "team": ["Muhammad Khurram Khan, Saiyed Umer, Ranjeet Kumar Rout, Alamgir Sardar"],
        "tags": ["Computer Vision", "Medical AI"],
        "patent": True,
        "patent_no": "US11762969B1",
        "sponsored": False,
        "sponsored_by": "JKST&IC,  DST, J&K"
        
    },
    {
        "id": "ai-healthcare",
        "title": "A Recommendation System And Method For E-commerce Using Machine Learning",
        "status": "completed",
        "year": "",
        "funding": " ",
        "description": "A Recommendation System And Method For E-commerce Using Machine Learning",
        "image": "ai-medicine.jpg",
        "team": ["Rout, Ranjeet Kumar; Umer, Saiyed; Sahoo, Ratikanta; Acharya, Biswaranjan ,Ranga"],
        "tags": ["Machine Learning"],
        "patent": True,
        "patent_no": "Australian Patent Number:2021106572",
        "sponsored": False,
        "sponsored_by": ""
        
    },
    {
        "id": "ai-Ecommerce",
        "title": "Affine Boolean Function for 16 Queen Problem",
        "status": "completed",
        "year": "2021",
        "funding": "",
        "description": "Implementation of Affine Boolean Function for 16 Queen Problem and Its Application",
        "image": "ai-medicine.jpg",
        "team": ["Ranjeet Kumar Rout, Saiyed Umer, Sabha Sheikh, Harveeer Singh Pali and Ratikanta Sahoo"],
        "tags": ["Artificial Intelligence", "Machine Learning"],
        "patent": True,
        "patent_no": "202111035066",
        "sponsored": False,
        "sponsored_by": ""
        
    },
    {
        "id": "dryer",
        "title": "SOLAR DRYER",
        "status": "completed",
        "year": "2021-2022",
        "funding": "",
        "description": "AN ECO-FRIENDLY LOW COST HYBRID SOLAR DRYER FOR DRYING VEGETABLES AND FRUITS",
        "image": "ai-medicine.jpg",
        "team": ["H. S Pali, Ranjeet Kumar Rout, Saiyed Umer and Ratikanta Sahoo"],
        "tags": ["Computer Vision", "Medical AI"],
        "patent": True,
        "patent_no": "2202111055051",
        "sponsored": False,
        "sponsored_by": ""
        
    },

    {
        "id": "handwritten-equations-cv",
        "title": "Solving Handwritten Linear Equations using Computer Vision & Deep Learning",
        "status": "completed",
        "year": "2021",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["Computer Vision", "Deep Learning"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    },
    {
        "id": "product-eval-comments",
        "title": "Product Evaluation using comment analysis: A Case Study in E-Commerce",
        "status": "completed",
        "year": "2021",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["E-Commerce", "Sentiment Analysis"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    },
    {
        "id": "fake-news-app",
        "title": "Fake news detection App development using machine learning",
        "status": "completed",
        "year": "2021",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["Fake News", "ML"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    },
    {
        "id": "emotion-biased-model",
        "title": "Human emotion recognition using biased deep learning model",
        "status": "completed",
        "year": "2021",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["Emotion Recognition", "Deep Learning"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    },
    {
        "id": "facial-recognition-alexa",
        "title": "Facial recognition and emotion detection using Alexa as voice interface",
        "status": "completed",
        "year": "2020",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["Facial Recognition", "Alexa", "Emotion Detection"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    },
    {
        "id": "peer-connect-chat",
        "title": "Peer connect (An improvised chat application) using Firebase realtime database as backend",
        "status": "completed",
        "year": "2020",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["Chat App", "Firebase"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    },
    {
        "id": "crypto-price-predict",
        "title": "Crypto Currency Price Prediction (ML)",
        "status": "completed",
        "year": "2019",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["Cryptocurrency", "ML"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    },
    {
        "id": "safe-remote-purchase",
        "title": "Safe Remote Purchase (Blockchain)",
        "status": "completed",
        "year": "2019",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["Blockchain", "E-Commerce"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    },
    {
        "id": "3d-map-travel-app",
        "title": "3D Map with travel simulator app",
        "status": "completed",
        "year": "2019",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["3D Mapping", "Simulation"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    },
    {
        "id": "image-processing-ml",
        "title": "Image Processing using ML",
        "status": "completed",
        "year": "2019",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["Image Processing", "ML"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    },
    {
        "id": "community-buybooks",
        "title": "Community Builder App with BuyBooks",
        "status": "completed",
        "year": "2019",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["Community", "App Development"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    },
    {
        "id": "cab-demand-predict",
        "title": "Cab Demand Prediction System",
        "status": "completed",
        "year": "2019",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["Demand Prediction", "ML"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    },
    {
        "id": "car-insurance-ml",
        "title": "Car Insurance Premium Calculator from Driving Behavior of Driver",
        "status": "completed",
        "year": "2019",
        "funding": "",
        "description": "",
        "image": "ai-medicine.jpg",
        "team": [],
        "tags": ["Insurance", "ML"],
        "patent": False,
        "sponsored": False,
        "supervised": True
    }

    ]

    return render_template("projects.html", projects=PROJECTS, active_page='projects')


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

    author_name = "Ranjeet Kumar Rout"  # You can change it or use Google Scholar ID later
    scholar_pubs = get_scholar_publications(author_name)
    journal_pubs = {
        "2024": [
            {
                "title": "Artificial intelligence-based smart agricultural systems for saffron cultivation with integration of Unmanned Aerial Vehicle imagery and deep learning approaches.",
                "authors": "Nazeer, Ishrat, Saiyed Umer, Ranjeet Kumar Rout, M. Tanveer.",
                "venue": "Computers and Electrical Engineering",
                "year": "2024",
                "doi": "10.1016/j.compeleceng.2024.109542",
                "pdf": "paper1.pdf",
                "bibtex": "@article{professor2023advanced,\n  title={Artificial intelligence-based smart agricultural systems for saffron cultivation with integration of Unmanned Aerial Vehicle imagery and deep learning approaches.},\n  author={Nazeer, Ishrat, Saiyed Umer, Ranjeet Kumar Rout,M. Tanveer.},\n  journal={Computers and Electrical Engineering},\n  volume={119},\n  pages={},\n  year={2024},\n  publisher={Elsevier}}\n}",
                "topics": ["Artificial intelligence", "Deep learning approaches"]
            },
            {
                "title": "Hybrid optimization assisted deep ensemble classification framework for skin cancer detection.",
                "authors": "Pukhta, Irfan Rashid, and Ranjeet Kumar Rout.",
                "venue": " Multimedia Tools and Applications",
                "year": "2024",
                "doi": "10.1007/s11042-024-19419-x",
                "pdf": "paper1.pdf",
                "bibtex": "@article{professor2024advanced,\n  title={Hybrid optimization assisted deep ensemble classification framework for skin cancer detection.},\n  author={Pukhta, Irfan Rashid, and Ranjeet Kumar Rout.},\n  journal={Multimedia Tools and Applications},\n  volume={83},\n  pages={63--94},\n  year={2024},\n  publisher={ Springer Science and Business Media LLC​}}\n}",
                "topics": ["Deep Ensemble Classification Framework", "Feature Extraction and Selection"]
            },
             {
                "title": "A Deep Quantum Convolutional Neural Network Based Facial Expression Recognition For Mental Health Analysis.",
                "authors": "Hossain, Sanoar, Saiyed Umer, Ranjeet Kumar Rout, and Hasan Al Marzouqi. ",
                "venue": " IEEE Transactions on Neural Systems and Rehabilitation Engineering",
                "year": "2024",
                "doi": "10.1109/TNSRE.2024.3385336​",
                "pdf": "A_Deep_Quantum_Convolutional_Neural_Network_Based_Facial_Expression_Recognition_For_Mental_Health_Analysis.pdf",
                "bibtex": "@article{professor2024advanced,\n  title={A Deep Quantum Convolutional Neural Network Based Facial Expression Recognition For Mental Health Analysis.},\n  author={Hossain, Sanoar, Saiyed Umer, Ranjeet Kumar Rout, and Hasan Al Marzouqi.},\n  journal={ IEEE Transactions on Neural Systems and Rehabilitation Engineering},\n  volume={32},\n  pages={},\n  year={2024},\n  publisher={IEEE, PubMed​}}\n}",
                "topics": ["Quantum Computing", "Deep Learning", "Convolutional Neural Network"," Facial Expression Recognition", "Mental Health Analysis", "Quantum Machine Learning", "Emotion Recognition", "Quantum Convolutional Neural Network", "QML", "Healthcare AI", "Human-Computer Interaction"]
            },
            {
        "title": "Enhanced Biometric Template Protection Schemes for Securing Face Recognition in IoT Environment.",
        "authors": "Sardar, Alamgir, Saiyed Umer, Ranjeet Kumar Rout, Kshira Sagar Sahoo, and Amir H. Gandomi.",
        "venue": "IEEE Internet of Things Journal",
        "year": "2024",
        "doi": "10.1109/JIOT.2024.3265978",
        "pdf": "paper2.pdf",
        "bibtex": "@article{alamgir2024biometric,\n  title={Enhanced Biometric Template Protection Schemes for Securing Face Recognition in IoT Environment.},\n  author={Sardar, Alamgir, Saiyed Umer, Ranjeet Kumar Rout, Kshira Sagar Sahoo, and Amir H. Gandomi.},\n  journal={IEEE Internet of Things Journal},\n  volume={11},\n  number={5},\n  pages={3567--3578},\n  year={2024},\n  publisher={IEEE}}\n}",
        "topics": ["Biometric Template Protection", "IoT Security"]
    },
    {
        "title": "Energy harvesting‐enabled energy‐efficient routing using spotted hyena optimization in wireless sensor network.",
        "authors": "Gupta, Amardeep, and Ranjeet Kumar Rout.",
        "venue": "International Journal of Communication Systems",
        "year": "2024",
        "doi": "10.1002/dac.5747",
        "pdf": "paper3.pdf",
        "bibtex": "@article{gupta2024energy,\n  title={Energy harvesting‐enabled energy‐efficient routing using spotted hyena optimization in wireless sensor network.},\n  author={Gupta, Amardeep, and Ranjeet Kumar Rout.},\n  journal={International Journal of Communication Systems},\n  volume={37},\n  number={8},\n  pages={e5747},\n  year={2024},\n  publisher={John Wiley & Sons, Ltd.}}\n}",
        "topics": ["Energy Harvesting", "Routing Optimization"]
    },
    {
        "title": "DeepPRMS: advanced deep learning model to predict protein arginine methylation sites.",
        "authors": "Khandelwal, Monika, and Ranjeet Kumar Rout.",
        "venue": "Briefings in Functional Genomics",
        "year": "2024",
        "doi": "10.1093/bfgp/elae001",
        "pdf": "paper4.pdf",
        "bibtex": "@article{khandelwal2024deepprms,\n  title={DeepPRMS: advanced deep learning model to predict protein arginine methylation sites.},\n  author={Khandelwal, Monika, and Ranjeet Kumar Rout.},\n  journal={Briefings in Functional Genomics},\n  volume={23},\n  number={1},\n  pages={1--13},\n  year={2024},\n  publisher={Oxford University Press}}\n}",
        "topics": ["Deep Learning", "Protein Methylation"]
    },
   
      
        ],
        "2023": [
            # More journal publications...
            {
        "title": "Improved traffic sign recognition algorithm based on YOLOv4-tiny.",
        "authors": "Sharma, Vipul, Pankaj Dhiman, and Ranjeet Kumar Rout.",
        "venue": "Journal of Visual Communication and Image Representation",
        "year": "2023",
        "doi": "10.1016/j.jvcir.2023.103774",
        "pdf": "paper5.pdf",
        "bibtex": "@article{sharma2023traffic,\n  title={Improved traffic sign recognition algorithm based on YOLOv4-tiny.},\n  author={Sharma, Vipul, Pankaj Dhiman, and Ranjeet Kumar Rout.},\n  journal={Journal of Visual Communication and Image Representation},\n  volume={91},\n  pages={103774},\n  year={2023},\n  publisher={Elsevier}}\n}",
        "topics": ["Traffic Sign Recognition", "YOLOv4"]
    },
    {
        "title": "Variation of deep features analysis for facial expression recognition system.",
        "authors": "Shabbir, Nazir, and Ranjeet Kumar Rout.",
        "venue": "Multimedia Tools and Applications",
        "year": "2023",
        "doi": "10.1007/s11042-023-11692-5",
        "pdf": "paper6.pdf",
        "bibtex": "@article{shabbir2023deep,\n  title={Variation of deep features analysis for facial expression recognition system.},\n  author={Shabbir, Nazir, and Ranjeet Kumar Rout.},\n  journal={Multimedia Tools and Applications},\n  volume={82},\n  number={8},\n  pages={11507--11522},\n  year={2023},\n  publisher={Springer}}\n}",
        "topics": ["Facial Expression Recognition", "Deep Features"]
    },
    {
  "title": "Fine-grained Image Analysis for Facial Expression Recognition Using Deep Convolutional Neural Networks with Bilinear Pooling",
  "authors": "Hossain, Sanoar; Umer, Saiyed; Rout, Ranjeet Kr; Tanveer, M.",
  "venue": "Applied Soft Computing",
  "year": "2023",
  "doi": "10.1016/j.asoc.2023.109997",
  "pdf": "Fine-grained_Image_Analysis_for_Facial_Expression_Recognition_Using_Deep_Convolutional_Neural_Networks_with_Bilinear_Pooling.pdf",
  "bibtex": "@article{hossain2023fine,\n  title={Fine-grained Image Analysis for Facial Expression Recognition Using Deep Convolutional Neural Networks with Bilinear Pooling},\n  author={Hossain, Sanoar and Umer, Saiyed and Rout, Ranjeet Kr and Tanveer, M.},\n  journal={Applied Soft Computing},\n  volume={136},\n  pages={109997},\n  year={2023},\n  publisher={Elsevier},\n  doi={10.1016/j.asoc.2023.109997}\n}",
  "topics": [
    "Facial Expression Recognition",
    "Deep Learning",
    "Convolutional Neural Networks",
    "Bilinear Pooling",
    "Image Analysis",
    "Computer Vision",
    "Emotion Recognition"
  ]
},
{
  "title": "Smart Sentiment Analysis System for Pain Detection Using Cutting Edge Techniques in a Smart Healthcare Framework",
  "authors": "Ghosh, Anay; Umer, Saiyed; Khan, Muhammad Khurram; Rout, Ranjeet Kumar; Dhara, Bibhas Chandra",
  "venue": "Cluster Computing",
  "year": "2022",
  "doi": "10.1007/s10586-022-03552-z",
  "pdf": "Smart_Sentiment_Analysis_System_for_Pain_Detection_Using_Cutting_Edge_Techniques_in_a_Smart_Healthcare_Framework.pdf",
  "bibtex": "@article{ghosh2022smart,\n  title={Smart Sentiment Analysis System for Pain Detection Using Cutting Edge Techniques in a Smart Healthcare Framework},\n  author={Ghosh, Anay and Umer, Saiyed and Khan, Muhammad Khurram and Rout, Ranjeet Kumar and Dhara, Bibhas Chandra},\n  journal={Cluster Computing},\n  volume={26},\n  number={1},\n  pages={119--135},\n  year={2022},\n  publisher={Springer},\n  doi={10.1007/s10586-022-03552-z}\n}",
  "topics": [
    "Sentiment Analysis",
    "Pain Detection",
    "Smart Healthcare",
    "Facial Expression Recognition",
    "Deep Learning",
    "Convolutional Neural Networks",
    "Healthcare Technology",
    "Emotion Recognition"
  ]
},
{
    "title": "ROTEE: Remora Optimization and Tunicate swarm algorithm‐based Energy‐Efficient cluster‐based routing for EH‐enabled heterogeneous WSNs",
    "authors": "Gupta, Amar Deep, and Ranjeet Kumar Rout",
    "venue": "International Journal of Communication Systems",
    "year": "2023",
    "doi": "10.1002/dac.5372",
    "pdf": "ROTEE_Remora_Optimization_2023.pdf",
    "bibtex": "@article{gupta2023rotee,\n  title={ROTEE: Remora Optimization and Tunicate swarm algorithm-based Energy-Efficient cluster-based routing for EH-enabled heterogeneous WSNs},\n  author={Gupta, Amar Deep and Rout, Ranjeet Kumar},\n  journal={International Journal of Communication Systems},\n  volume={36},\n  number={11},\n  pages={e5372},\n  year={2023},\n  publisher={Wiley},\n  doi={10.1002/dac.5372}\n}",
    "topics": [
        "Wireless Sensor Networks",
        "Energy Harvesting",
        "Swarm Intelligence",
        "Remora Optimization Algorithm",
        "Tunicate Swarm Algorithm",
        "Clustering",
        "Energy Efficiency",
        "Routing Protocols"
    ]
}
        ],
        "2022":[
            {
    "title": "A Secure and Efficient Biometric Template Protection Scheme for Palmprint Recognition System",
    "authors": "Sardar, Alamgir, Saiyed Umer, Ranjeet Ku Rout, and Muhammad Khurram Khan",
    "venue": "IEEE Transactions on Knowledge and Data Engineering",
    "year": "2022",
    "doi": "10.1109/TKDE.2022.3150469",
    "pdf": "Secure_Biometric_Template_Palmprint_2022.pdf",
    "bibtex": "@article{sardar2022secure,\n  title={A Secure and Efficient Biometric Template Protection Scheme for Palmprint Recognition System},\n  author={Sardar, Alamgir and Umer, Saiyed and Rout, Ranjeet Ku and Khan, Muhammad Khurram},\n  journal={IEEE Transactions on Knowledge and Data Engineering},\n  year={2022},\n  publisher={IEEE},\n  doi={10.1109/TKDE.2022.3150469}\n}",
    "topics": [
        "Biometric Security",
        "Palmprint Recognition",
        "Template Protection",
        "Deep Learning",
        "Cryptography",
        "Secure Biometrics",
        "Privacy Preservation",
        "Smart Authentication"
    ]
}

        ]
    }
    
    conference_pubs = {
        "2022": [
            {
  "title": "Protein-Protein Interaction Prediction from Primary Sequences Using Supervised Machine Learning Algorithm",
  "authors": "Monika Khandelwal, Ranjeet Ku Rout, Saiyed Umer",
  "venue": "Confluence 2022",
  "year": "2022",
  "doi": "10.1109/CONFLUENCE.2022.9734061",
  "pdf": "Protein-Protein_Interaction_Prediction_from_Primary_Sequences_Using_Supervised_Machine_Learning_Algorithm.pdf",
  "bibtex": "@inproceedings{khandelwal2022protein,\n  title={Protein-Protein Interaction Prediction from Primary Sequences Using Supervised Machine Learning Algorithm},\n  author={Khandelwal, Monika and Rout, Ranjeet Ku and Umer, Saiyed},\n  booktitle={2022 12th International Conference on Cloud Computing, Data Science & Engineering (Confluence)},\n  pages={123--128},\n  year={2022},\n  organization={IEEE}\n}",
  "topics": ["Protein-Protein Interaction", "Machine Learning", "Bioinformatics", "Sequence Analysis"]
}

        ],
        "2021":[
            {
  "title": "A Novel Template Protection Scheme for Face Recognition System",
  "authors": "Alamgir Sardar, Saiyed Umer, Ranjeet Kumar Rout",
  "venue": "CAMSE 2021, NIT Jalandhar",
  "year": "2021",
  "doi": "",
  "pdf": "A_Novel_Template_Protection_Scheme_for_Face_Recognition_System.pdf",
  "bibtex": "@inproceedings{sardar2021novel,\n  title={A Novel Template Protection Scheme for Face Recognition System},\n  author={Sardar, Alamgir and Umer, Saiyed and Rout, Ranjeet Kumar},\n  booktitle={Proceedings of CAMSE 2021},\n  year={2021},\n  organization={NIT Jalandhar}\n}",
  "topics": ["Biometric Security", "Face Recognition", "Template Protection", "Privacy Preservation"]
},
{
  "title": "Encryption and Decryption Scheme for IoT Communications Using Multilevel Encryption",
  "authors": "Sanchit Sindhwani, Sabha Sheikh, Saiyed Umer, Ranjeet Kumar Rout",
  "venue": "Information and Communication Technology for Competitive Strategies (ICTCS 2020)",
  "year": "2021",
  "doi": "10.1007/978-981-16-0882-7_81",
  "pdf": "Encryption_and_Decryption_Scheme_for_IoT_Communications_Using_Multilevel_Encryption.pdf",
  "bibtex": "@inproceedings{sindhwani2021encryption,\n  title={Encryption and Decryption Scheme for IoT Communications Using Multilevel Encryption},\n  author={Sindhwani, Sanchit and Sheikh, Sabha and Umer, Saiyed and Rout, Ranjeet Kumar},\n  booktitle={Information and Communication Technology for Competitive Strategies (ICTCS 2020)},\n  pages={1013--1022},\n  year={2021},\n  publisher={Springer, Singapore}\n}",
  "topics": ["IoT Security", "Multilevel Encryption", "Cryptography", "Secure Communication"]
},
{
  "title": "Machine Learning Techniques for IoT Data Analytics",
  "authors": "Nailah Afshan, Ranjeet Kumar Rout",
  "venue": "Book Chapter in 'Machine Learning-Based Data Analytics for IoT-Enabled Industry Automation'",
  "year": "2021",
  "doi": "10.1002/9781119740780.ch3",
  "pdf": "Machine_Learning_Techniques_for_IoT_Data_Analytics.pdf",
  "bibtex": "@incollection{afshan2021machine,\n  title={Machine Learning Techniques for IoT Data Analytics},\n  author={Afshan, Nailah and Rout, Ranjeet Kumar},\n  booktitle={Machine Learning-Based Data Analytics for IoT-Enabled Industry Automation},\n  pages={45--67},\n  year={2021},\n  publisher={Wiley}\n}",
  "topics": ["IoT Analytics", "Machine Learning", "Data Processing", "Industry 4.0"]
},
{
  "title": "Implementation of Affine Boolean Function for 16 Queen Problem and Its Application Thereof",
  "authors": "Ranjeet Kumar Rout, Saiyed Umer, Sabha Sheikh, Harveer Singh Pali, Ratikanta Sahoo",
  "venue": "Patent Application",
  "year": "2021",
  "doi": "",
  "pdf": "Implementation_of_Affine_Boolean_Function_for_16_Queen_Problem_and_Its_Application_Thereof.pdf",
  "bibtex": "@misc{rout2021implementation,\n  title={Implementation of Affine Boolean Function for 16 Queen Problem and Its Application Thereof},\n  author={Rout, Ranjeet Kumar and Umer, Saiyed and Sheikh, Sabha and Pali, Harveer Singh and Sahoo, Ratikanta},\n  year={2021},\n  note={Indian Patent Application No. 202111035066}\n}",
  "topics": ["Affine Boolean Functions", "Optimization Problems", "Combinatorial Algorithms", "Patent"]
}
        ]
    }
    
    # Extract all unique years and topics
    years = sorted(set(journal_pubs.keys()).union(set(conference_pubs.keys())), reverse=True)
    
    # Extract all unique topics
    topics = set()
    for year_pubs in journal_pubs.values():
        for pub in year_pubs:
            topics.update(pub["topics"])
    for year_pubs in conference_pubs.values():
        for pub in year_pubs:
            topics.update(pub["topics"])
    
    return render_template('publications.html', 
                         journal_pubs=journal_pubs,
                         conference_pubs=conference_pubs,
                         years=years,
                         topics=sorted(topics), active_page='publications')

# Books Section
@app.route('/books')
def books():
    """
    This route handles the books page ('/books') of the web application.
    It renders the 'books.html' template.
    """
    books_data = [
        {
            "title": "Artificial Intelligence Technologies for Computational Biology",
            "editors": "Ranjeet Kumar Rout, Saiyed Umer, Sabha Sheikh, Amrit Lal Sangal",
            "cover": "both.jpg",
            "link": "https://www.routledge.com/Artificial-Intelligence-Technologies-for-Computational-Biology/Rout-Umer-Sheikh-Sangal/p/book/9781032160009",
            "download": "#"
        },
        {
            "title": "Advancement of Deep Learning in Object Detection and Recognition",
            "editors": "Roohie Naaz Mir, Vipul Kumar Sharma, Ranjeet Kumar Rout, Saiyed Umer",
            "cover": "both2.jpg",
            "link": "https://www.riverpublishers.com/book_details.php?book_id=1021",
            "download": "#"
        },
        # Add more books here as needed
    ]

    return render_template("books.html", books=books_data, active_page='books')


# News Section
@app.route('/news')
def news():
    """
    This route handles the news page ('/news') of the web application.
    It renders the 'news.html' template.
    """
    news_items = [
        {
            "image": "news1.jpg",
            "date": "June 15, 2023",
            "title": "New Research Published",
            "excerpt": "Our quantum computing paper accepted in Nature...",
            "full_text": "Detailed findings show breakthrough in quantum entanglement simulation using novel qubit architecture."
        }
        # Add more as needed
    ]

    announcements = [
        "Paper submission deadline: July 30",
        "New lab equipment arrived"
        # Add more as needed
    ]


    return render_template('news.html', 
                           news_items=news_items,
                           announcements=announcements,
                           active_page='news')


# Responsibilities
@app.route('/responsibilities')
def responsibilities():
    """
    This route handles the responsibilities page ('/responsibilities') of the web application.
    It renders the 'responsibilities.html' template.
    """
    return render_template("responsibilities.html", active_page='responsibilities')

# People Section
@app.route('/people')
def people():
    people = [
        {
            "name": "Venkata  Mahalakshmi",
            "title": "( 2019PHSCSE005 )",
            "degree": "Ph.D.",
            "institution": "Rensselaer Polytechnic Institute",
            "interests": ["E-Health Care System"],
            "image": "avatar.webp"
        },
        {
            "name": "Amardeep Gupta",
            "title": " ( 2019PHSCSE006 ) ",
            "degree": "Ph.D.",
            "institution": "Rensselaer Polytechnic Institute",
            "interests": ["Meta-Huristic algorithms for Energy Harvesting in WSN"],
            "image": "avatar.webp"
        },
        {
            "name": "Nazir Shabbir ",
            "title": " ( 2019PHSCSE008 )",
            "degree": "Ph.D.",
            "institution": "Rensselaer Polytechnic Institute",
            "interests": [" Affective Computing", "Object Detection"],
            "image": "avatar.webp"
        },
        {
            "name": "Irfan Rashid  Pukhta",
            "title": "( 2019PHSCSE012 ) ",
            "degree": "Ph.D.",
            "institution": "Rensselaer Polytechnic Institute",
            "interests": ["Classification/Detection essential genes from microarray data"],
            "image": "avatar.webp"
        },
        {
            "name": "Monika Khandelwal",
            "title": "( 2021PHACSE001 )",
            "degree": "Ph.D.",
            "institution": "Rensselaer Polytechnic Institute",
            "interests": ["Artificial Intelligence/Machine Learning in Computational Biology"],
            "image": "avatar_girl.png"
        },
        {
            "name": "Ishrat Nazir",
            "title": "( 2023PHSCSE00 )",
            "degree": "Ph.D.",
            "institution": "Rensselaer Polytechnic Institute",
            "interests": ["Artificial Intelligence/Machine Learning in Computational Biology"],
            "image": "avatar.webp"
        },
        {
            "name": "Parveen kumar",
            "title": "",
            "degree": "M.Tech",
            "institution": "Rensselaer Polytechnic Institute",
            "interests": ["Reconstruction of DNA Sequence using Cellular Automata for Identification of Features"],
            "image": "avatar.webp"
        },
        {
            "name": "Jaiprakash Dhakar",
            "title": "",
            "degree": "M.Tech",
            "institution": "Rensselaer Polytechnic Institute",
            "interests": ["A Pattern Classification Model for vowel data using Fuzzy Nearest Neighbor"],
            "image": "avatar.webp"
        },
        {
            "name": "Pranay Sakhare",
            "title": "",
            "degree": "M.Tech",
            "institution": "Rensselaer Polytechnic Institute",
            "interests": ["Identification of Olfactory Receptors using a Parametric model"],
            "image": "avatar.webp"
        },
        {
            "name": " Shubham Jain ",
            "title": "",
            "degree": "M.Tech",
            "institution": "Rensselaer Polytechnic Institute",
            "interests": ["A Competent Algorithm to Detect Attractors in Gene Regulatory Networks (GRNs) Based On Divide and Conquer"],
            "image": "avatar.webp"
        },
        {
            "name": "Santosh Punase  ",
            "title": "",
            "degree": "M.Tech",
            "institution": "Rensselaer Polytechnic Institute",
            "interests": ["Identification of singleton attractors of Boolean Network using graph isomorphism"],
            "image": "avatar.webp"
        },
        {
            "name": "Sagar Mal Nitharwal",
            "title": "",
            "degree": "M.Tech",
            "institution": "Rensselaer Polytechnic Institute",
            "interests": ["A Boolean Based Multi –Secret Image Sharing scheme using bit-reversa"],
            "image": "avatar.webp"
        },
        # Add more as needed
    ]
    return render_template("people.html", people=people, active_page='people')

# Talks and Writings
@app.route('/talks_delivered')
def talks_delivered():
    """
    This route handles the stalks delivered route.
    """
    # Talks data categorized by year
    talks_data = {
        "2023": [
            {
                "title": "Fine-grained Image Analysis for Affective Computing using Deep CNNs in IoT Environment",
                "event": "CIoT-2023, 8th June",
                "location": "Bennett University, Greater Noida"
            },
            {
                "title": "Fine-grained Image Analysis for Emotion Recognition using Deep CNNs with Bilinear Pooling",
                "event": "AITHA-2023, 24th Feb",
                "location": "NIT Delhi"
            },
            {
                "title": "Facial Expression Recognition using Deep CNNs",
                "event": "STC on Advanced Deep Learning, 27 Feb – 3 Mar",
                "location": "NITTTR Chandigarh"
            },
            {
                "title": "AI and Agriculture (Fisheries Sector)",
                "event": "Workshop, 8 Aug",
                "location": "SKUAST-K, Jammu and Kashmir"
            }
        ],
        "2022": [
            {
                "title": "ML in Genomics",
                "event": "AI/ML in Animal Breeding, 22–28 Mar",
                "location": "SKUAST-K"
            },
            {
                "title": "Computer Vision on Linux Applications in Engineering",
                "event": "STC, 28 Nov – 2 Dec",
                "location": "NITTTR Chandigarh"
            }
        ],
        "2021": [
            {
                "title": "ML for Biometric Reorganization & Security",
                "event": "Webinar, 22–26 Feb",
                "location": "ITS Engineering College, Noida"
            },
            {
                "title": "Cancelable Biometrics using ML",
                "event": "Webinar, 26 Jun",
                "location": "ITS Engineering College, Noida"
            },
            {
                "title": "Session Chair, Confluence 2021",
                "event": "28–29 Jan",
                "location": "Amity University, Noida"
            }
        ],
        "2020": [
            {
                "title": "India International Science Festival (IISF)",
                "event": "Virtual, 22–25 Dec",
                "location": ""
            }
        ],
        "2019": [
            {
                "title": "Career Counseling",
                "event": "23rd Feb",
                "location": "SP Model Higher Secondary School, Srinagar"
            }
        ],
        "2018": [
            {
                "title": "3rd International Conference on Soft Computing: SoCTA-2018",
                "event": "21–23 Dec",
                "location": ""
            }
        ]
    }

    return render_template("talks_delivered.html", active_page='talks_delivered', talks_by_year=talks_data)


# Blogs
@app.route('/my_blogs')
def my_blogs():
    """
    This route handles the blogs route.
    """
    return render_template("my_blogs.html", active_page='my_blogs')

# Seminars
@app.route('/seminar_workshop')
def seminar_workshop():
    seminar_workshop_entries = [
        # Seminars
        {
            "title": "Guest Speaker on Machine Learning",
            "details": "Organized by Dept. of CSE, ITS Engineering College, Greater Noida on February 22-26, 2021.",
            "location": "Greater Noida",
            "type": "seminar"
        },
        {
            "title": "Coordinator - Applications of ML and DL",
            "details": "Organized by Dept. of CSE, NIT Srinagar on October 26-30, 2020.",
            "location": "NIT Srinagar",
            "type": "seminar"
        },
        {
            "title": "Jt. Organizing Secretary - International Conference on Digital Democracy - IT for Change",
            "details": "Held at KIIT Bhubaneswar, January 16-18, 2020. Organized by the Computer Society of India.",
            "location": "KIIT Bhubaneswar",
            "type": "seminar"
        },
        {
            "title": "Organizing Secretary - 8th International Symposium on Fusion of Science & Technology (ISFT-2020)",
            "details": "Held at J.C. Bose University of Science & Technology, YMCA, Faridabad, India on January 6-10, 2020.",
            "location": "YMCA, Faridabad",
            "type": "seminar"
        },
        {
            "title": "Coordinator - Exordium 2019",
            "details": "Second National Level Workshop Cum Coding Festival by Semicolon and Dept. of CSE, NIT Srinagar, April 3-7, 2019.",
            "location": "NIT Srinagar",
            "type": "seminar"
        },
        {
            "title": "Organized one-day coding competition Techno Crackers: Let's Codify",
            "details": "Dept. of CSE, NIT Srinagar, May 13, 2017.",
            "location": "NIT Srinagar",
            "type": "seminar"
        },

        # Academic Visits / Workshops
        {
            "title": "One Day Workshop on Cloud Computing and Big Data Analytics",
            "details": "Held on May 19, 2015 at NIT Jalandhar.",
            "location": "NIT Jalandhar, Punjab",
            "type": "visit"
        },
        {
            "title": "STC on Recent Trends in Software Engineering and Knowledge Mining",
            "details": "June 1-5, 2015 at NIT Jalandhar.",
            "location": "NIT Jalandhar, Punjab",
            "type": "visit"
        },
        {
            "title": "STC on Image and NLP",
            "details": "May 30 to June 3, 2016 at NIT Jalandhar.",
            "location": "NIT Jalandhar, Punjab",
            "type": "visit"
        },
        {
            "title": "STC on Advances in CS & IT Trends",
            "details": "January 2-6, 2017 at NIT Jalandhar.",
            "location": "NIT Jalandhar, Punjab",
            "type": "visit"
        },
        {
            "title": "TECHNO CRACKER: LET's CODIFY under CSI Banner",
            "details": "May 13, 2017.",
            "location": "NIT Jalandhar, Punjab",
            "type": "visit"
        },
        {
            "title": "Research Promotional Workshop on Digital Geometry",
            "details": "June 23-25, 2014.",
            "location": "IIEST Shibpur",
            "type": "visit"
        },
        {
            "title": "International Indo-US Workshop on Statistical Method on Bioinformatics",
            "details": "December 12-14, 2013.",
            "location": "IISc Bangalore",
            "type": "visit"
        },
        {
            "title": "Course on Mathematical Morphology and Fractal Informatics",
            "details": "June 29 - July 15, 2012.",
            "location": "ISI Bangalore",
            "type": "visit"
        },
        {
            "title": "International Workshop on Spatial Statistical Tools",
            "details": "November 26-30, 2012.",
            "location": "ISI Bangalore",
            "type": "visit"
        },
        {
            "title": "Course on Spatial Informatics from Image",
            "details": "November 30 - December 8, 2012.",
            "location": "ISI Bangalore",
            "type": "visit"
        },
        {
            "title": "CDSA-2014: 3rd International Symposium on Complex Dynamical Systems",
            "details": "March 10-12, 2014.",
            "location": "ISI Kolkata",
            "type": "visit"
        },
        {
            "title": "6th Workshop on Nano-Electronics and Biochips",
            "details": "December 22, 2012.",
            "location": "ISI Kolkata",
            "type": "visit"
        },
        {
            "title": "Workshop on Experiencing Data Mining using Statistica",
            "details": "March 25-26, 2013.",
            "location": "ISI Kolkata",
            "type": "visit"
        },
        {
            "title": "National Conference on Bioinformatics & Comp. Biology",
            "details": "March 14-15, 2014.",
            "location": "SMIT, Sikkim",
            "type": "visit"
        },
        {
            "title": "STC on Artificial Intelligence",
            "details": "December 10-14, 2007.",
            "location": "NITTR, Kolkata",
            "type": "visit"
        },
        {
            "title": "Staff Development Program on Data Mining",
            "details": "November 12-23, 2007.",
            "location": "SONA College of Technology, Tamil Nadu",
            "type": "visit"
        },
    ]

    return render_template('seminar_workshop.html', seminar_workshop_entries=seminar_workshop_entries, active_page='seminar_workshop')


# About Me
@app.route('/about-me')
def about_me():
    '''
    This is the dedicated page for professor's about section
    '''
    return render_template('about_me.html')

# Contact
@app.route('/contact')
def contact():
    '''
    This is the contact page
    '''
    return render_template('contact.html', active_page='contact')

if __name__ == '__main__':
    """
    Run the Flask application in debug mode for development purposes.
    This allows for automatic reloading and better error messages.
    """
    app.run(debug=True)
