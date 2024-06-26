from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.models import Post, User
import random

#SQLALCHEMY_DATABASE_URL = 'postgressql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:mysecretpassword@localhost/social-media'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
db = sessionmaker(autoflush=False, bind=engine, autocommit=False)()

def insert_random_posts():
    posts = [
        {"owner_id": random.choice([1, 2]), "title": "The Wonders of Space Exploration", "content": "Space exploration has led to numerous discoveries about our solar system and beyond.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "How to Bake the Perfect Chocolate Cake", "content": "Follow these easy steps to bake a moist and delicious chocolate cake.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Benefits of Yoga", "content": "Yoga can improve flexibility, strength, and mental clarity.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "Top 10 Programming Languages in 2024", "content": "Python, JavaScript, and Java are among the most popular programming languages this year.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "Secrets to a Successful Morning Routine", "content": "Start your day with a healthy breakfast, exercise, and meditation.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "Exploring the Amazon Rainforest", "content": "The Amazon is home to a vast array of biodiversity and indigenous cultures.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Rise of Electric Vehicles", "content": "Electric vehicles are becoming more popular due to their environmental benefits.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "How to Improve Your Photography Skills", "content": "Experiment with lighting, angles, and composition to enhance your photos.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "Understanding Quantum Computing", "content": "Quantum computing could revolutionize fields like cryptography and medicine.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "Tips for Effective Time Management", "content": "Prioritize tasks, avoid multitasking, and take regular breaks to boost productivity.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The History of the Internet", "content": "The internet has evolved from a simple network to a global information superhighway.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "Gardening for Beginners", "content": "Start with easy-to-grow plants like tomatoes and herbs to get started with gardening.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Future of Artificial Intelligence", "content": "AI is expected to advance in areas like healthcare, autonomous vehicles, and natural language processing.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "Exploring the Depths of the Ocean", "content": "The ocean's depths remain largely unexplored, holding many mysteries and undiscovered species.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "How to Write a Bestselling Novel", "content": "Focus on compelling characters, a gripping plot, and engaging dialogue.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Science Behind Climate Change", "content": "Human activities are significantly contributing to global warming and climate change.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "Traveling on a Budget: Tips and Tricks", "content": "Look for deals, travel during off-peak times, and stay in hostels to save money.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Impact of Social Media on Society", "content": "Social media has transformed communication, but also raises concerns about privacy and mental health.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "Understanding Blockchain Technology", "content": "Blockchain technology offers decentralized and secure transactions, revolutionizing various industries.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Benefits of Meditation", "content": "Meditation can reduce stress, improve concentration, and enhance overall well-being.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "How to Train for a Marathon", "content": "A well-structured training plan, proper nutrition, and recovery are key to marathon preparation.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Evolution of Video Games", "content": "Video games have evolved from simple arcade games to immersive virtual reality experiences.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Art of Public Speaking", "content": "Effective public speaking involves preparation, confidence, and engaging your audience.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Role of Genetics in Health", "content": "Genetics play a crucial role in determining susceptibility to various diseases and health conditions.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "Exploring the World of Cryptocurrencies", "content": "Cryptocurrencies are digital currencies that operate on blockchain technology, offering decentralized transactions.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Benefits of Reading Daily", "content": "Reading daily can improve brain function, increase knowledge, and reduce stress.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "How to Start a Successful Blog", "content": "Choose a niche, create quality content, and promote your blog to attract readers.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The History of Ancient Civilizations", "content": "Ancient civilizations like Egypt, Greece, and Rome have left a lasting legacy on modern society.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Impact of Technology on Education", "content": "Technology has transformed education through online learning, digital tools, and interactive resources.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "How to Develop a Growth Mindset", "content": "Embrace challenges, learn from criticism, and persist in the face of setbacks to develop a growth mindset.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Role of Artificial Intelligence in Healthcare", "content": "AI can enhance diagnostic accuracy, personalize treatment plans, and improve patient care.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Secrets to a Healthy Diet", "content": "Incorporate a variety of fruits, vegetables, whole grains, and lean proteins into your diet.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Benefits of Traveling Solo", "content": "Solo travel offers freedom, self-discovery, and the opportunity to meet new people.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Science Behind Happiness", "content": "Happiness is influenced by genetics, life circumstances, and intentional activities.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Evolution of Music Genres", "content": "Music genres have evolved over time, blending styles and creating new forms of expression.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "How to Build a Successful Startup", "content": "Identify a market need, develop a solid business plan, and secure funding to launch your startup.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Role of Women in History", "content": "Women have made significant contributions throughout history, often overcoming great challenges.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "Understanding Cryptocurrency Mining", "content": "Cryptocurrency mining involves using computer power to solve complex mathematical problems and validate transactions.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Benefits of Regular Exercise", "content": "Exercise improves cardiovascular health, boosts mood, and enhances overall physical fitness.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The History and Culture of Japan", "content": "Japan's rich history and vibrant culture are reflected in its traditions, art, and cuisine.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Future of Renewable Energy", "content": "Renewable energy sources like solar and wind power are crucial for a sustainable future.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Psychology of Color in Marketing", "content": "Colors can influence consumer behavior and brand perception in marketing and advertising.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "How to Start a Successful YouTube Channel", "content": "Create engaging content, optimize your videos for SEO, and interact with your audience to grow your channel.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Benefits of Volunteering", "content": "Volunteering can boost mental health, build community, and provide new skills and experiences.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Science of Sleep", "content": "Good sleep hygiene and a consistent sleep schedule are essential for overall health and well-being.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The History of the Roman Empire", "content": "The Roman Empire's influence on law, architecture, and governance is still evident today.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Rise of E-Sports", "content": "E-sports has grown into a global phenomenon, with professional players competing for millions in prize money.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "How to Practice Mindfulness", "content": "Mindfulness involves paying full attention to the present moment, which can reduce stress and improve focus.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Role of Technology in Modern Medicine", "content": "Technology advancements, such as telemedicine and robotic surgery, are transforming healthcare delivery.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Importance of Financial Literacy", "content": "Understanding financial principles can help you make informed decisions and achieve financial stability.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Cultural Significance of Festivals", "content": "Festivals celebrate cultural heritage, traditions, and community, fostering unity and joy.", "published": True},
        {"owner_id": random.choice([1, 2]), "title": "The Science of Climate Change", "content": "Climate change is driven by greenhouse gas emissions, leading to global warming and environmental impacts.", "published": True},
    ]
    counter = 0
    for post in posts:
        p = Post(**post)
        db.add(p)
        db.commit()
        print("Post number", counter, "is added .")
        counter += 1

def insert_some_users():
    dummy_users = [
        {
            "email": "admin@site.com",
            "password": "password"
        },
        {
            "email": "user1@site.com",
            "password": "password"
        },
        {
            "email": "user2@site.com",
            "password": "password"
        }
    ]
    counter = 0

    for user in dummy_users:
        user = User(**user)
        db.add(user)
        db.commit()
        print("User number", counter, "is added .")
        counter += 1