from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.models import Post, User

#SQLALCHEMY_DATABASE_URL = 'postgressql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:mysecretpassword@localhost/social-media'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
db = sessionmaker(autoflush=False, bind=engine, autocommit=False)()

def insert_random_posts():
    dummy_posts = [{'title': 'Cybersecurity CPEs: Unraveling the What, Why & How', 'content': 'Perhaps even more so than in other professional domains, cybersecurity professionals constantly face new threats. To ensure you stay on top of your game, many certification programs require earning Continuing Professional Education (CPE) credits.', 'published': True}, {'title': 'Experts Uncover New Evasive SquidLoader Malware', 'content': 'Cybersecurity researchers have uncovered a new evasive malware loader named SquidLoader that spreads via phishing campaigns targeting Chinese organizations.\n', 'published': True}, {'title': 'New Rust-based Fickle Malware Uses PowerShell', 'content': 'A new Rust-based information stealer malware called Fickle Stealer has been observed being delivered via multiple attack chains with the goal of harvesting sensitive information from compromised hosts.', 'published': True}, {'title': 'Chinese Cyber Espionage Targets Telecom Operators', 'content': 'Cyber espionage groups associated with China have been linked to a long-running campaign that has infiltrated several telecom operators located in a single Asian country at least since 2021.', 'published': True}, {'title': 'Tool Overload: Why MSPs Are Still Drowning with Countless', 'content': 'As MSPs continue to be the backbone of IT security for numerous businesses, the array of tools at their disposal has grown exponentially. ', 'published': True}, {'title': 'French Diplomatic Entities Targeted in Russian-Linked', 'content': "State-sponsored actors with ties to Russia have been linked to targeted cyber attacks aimed at French diplomatic entities, the country's information security agency ANSSI said in an advisory.", 'published': True}, {'title': 'Researchers Uncover UEFI Vulnerability Affecting Multiple Intel CPUs', 'content': 'Cybersecurity researchers have disclosed details of a now-patched security flaw in Phoenix SecureCore UEFI firmware that affects multiple families of Intel Core desktop and mobile processors.', 'published': True}, {'title': 'U.S. Bans Kaspersky Software, Citing National Security Risks', 'content': 'The U.S. Department of Commerce\'s Bureau of Industry and Security (BIS) on Thursday announced a "first of its kind" ban that prohibits Kaspersky Lab\'s U.S. subsidiary from directly or indirectly offering its security software in the country.', 'published': True}, {'title': 'This is post 14 !', 'content': 'Hello friend and welcome to post number 14, here i wanna teach you how to be a robber .', 'published': True}, {'title': 'programming with python, how to do it ?', 'content': 'Python programming language, one of the best programming language in the world with the largest community .', 'published': True}, {'title': 'Stop jerking off bro :|', 'content': "It's not easy to stop jerking off but it is necessary . Just stop it and get some help from a girl .", 'published': True}]
    counter = 0
    for post in dummy_posts:
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