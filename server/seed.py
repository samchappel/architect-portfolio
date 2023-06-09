# from random import randint, choice
# from faker import Faker
# from app import app
# from models import db, User, PortfolioGrid, ProjectDetail

# if __name__ == '__main__':
#     fake = Faker()

#     with app.app_context():
#         print("Deleting all records...")
#         User.query.delete()
#         PortfolioGrid.query.delete()
#         ProjectDetail.query.delete()

#         print('Creating users...')
#         users_list = [
#             {"username": "judd1037", "password": "jUDD1037!", "first_name": "Garrett", "last_name": "Akol", "access_code": None, "admin": True}
#         ]

#         def make_users():
#             users = []

#             for user_dict in users_list:
#                 user = User(
#                     username=user_dict["username"],
#                     first_name=user_dict["first_name"],
#                     last_name=user_dict["last_name"],
#                     admin=True
#                 )
#                 user.password_hash = user_dict["password"]
#                 users.append(user)

#             db.session.add_all(users)
#             db.session.commit()

#         make_users()
#         print('Users created and committed')

#         def generate_portfolio_grid_data(num_grids):
#             portfolio_grid_data = []
#             image_url = "https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg"
            
#             for _ in range(num_grids):
#             title_words = fake.words(nb=randint(1, 3), ext_word_list=None)
#             title = ' '.join(title_words).title()
#             preview = fake.paragraph()
#             portfolio_grid_data.append({
#                 'title': title,
#                 'highlight_image': image_url,
#                 'preview': preview
#             })
#         return portfolio_grid_data

#         print('Generating portfolio grid data...')
#         portfolio_grid_data = generate_portfolio_grid_data(10)
#         for record in portfolio_grid_data:
#             grid = PortfolioGrid(**record)
#             db.session.add(grid)

#         db.session.commit()
#         print('Portfolio grid data generated and committed')

#         def generate_project_details_data(num_records, portfolio_grid_ids, portfolio_grid_titles):
#             project_details_data = []
#             image_url = "https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg"

#             for _ in range(num_records):
#                 grid_id = choice(portfolio_grid_ids)
#                 title = portfolio_grid_titles[grid_id]
#                 full_description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
#                 additional_images = [image_url] * randint(1, 10)

#                 project_details_data.append({
#                     "grid_id": grid_id,
#                     "title": title,
#                     "full_description": full_description,
#                     "thumbnails": additional_images
#                 })

#             return project_details_data

#         print('Generating project details data...')
#         portfolio_grid_ids = [1, 2, 3, 4, 5]  # Example portfolio grid IDs
#         portfolio_grid_titles = {
#             1: "Title 1",
#             2: "Title 2",
#             3: "Title 3",
#             4: "Title 4",
#             5: "Title 5"
#         }  # Example portfolio grid titles

#         project_details_data = generate_project_details_data(10, portfolio_grid_ids, portfolio_grid_titles)
#         for record in project_details_data:
#             detail = ProjectDetail(**record)
#             db.session.add(detail)

#         db.session.commit()
#         print('Project details data generated and committed')

from random import choice as rc, randint
#from faker import Faker
import random
from app import app
from models import db, User, PortfolioGrid, ProjectDetail

def make_users():
    users_list = [
        {"username": "judd1037", "password": "jUDD1037!", "first_name": "Garrett", "last_name": "Akol", "access_code": None, "admin": True}
    ]

    users = []
    for user_dict in users_list:
        user = User(
            username=user_dict["username"],
            first_name=user_dict["first_name"],
            last_name=user_dict["last_name"],
            admin=True
        )
        user.password_hash = user_dict["password"]
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

def make_portfolio_grids():
    portfolio_grid_list = [
        {
            'highlight_image': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg',
            'title': 'Sustainable Urban Housing Complex',
            'preview': 'A residential development designed to minimize environmental impact and promote sustainable living in urban areas.'
        },
        {
            'highlight_image': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg',
            'title': 'Revitalizing Historic Landmark: City Library Renovation',
            'preview': 'A transformative renovation project aimed at preserving the historical significance of a city library while integrating modern amenities and flexible spaces.'
        },
        {
            'highlight_image': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg',
            'title': 'Innovative Office Tower: The Future of Workplace Design',
            'preview': 'A cutting-edge office tower that redefines traditional workplace design by incorporating advanced technologies, sustainable features, and flexible workspaces.'
        },
        {
            'highlight_image': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg',
            'title': 'Iconic Sports Arena: Fusion of Modernity and Tradition',
            'preview': 'An iconic sports arena that blends contemporary design elements with traditional architectural influences, creating a unique and memorable venue.'
        },
        {
            'highlight_image': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg',
            'title': 'Eco-Friendly Resort: Harmonizing Luxury and Sustainability',
            'preview': 'A luxurious resort that sets new standards for sustainability in the hospitality industry, offering guests a unique eco-friendly experience.'
        },
        {
            'highlight_image': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg',
            'title': 'Community Wellness Center: Nurturing Mind, Body, and Soul',
            'preview': 'A community wellness center designed to promote holistic well-being through fitness, recreation, therapy, and educational programs.'
        },
        {
            'highlight_image': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg',
            'title': 'Modern Art Museum: Showcasing Contemporary Masterpieces',
            'preview': 'A modern art museum designed to provide an immersive and interactive experience for visitors, featuring a diverse collection of contemporary masterpieces.'
        },
        {
            'highlight_image': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg',
            'title': 'Sustainable Office Campus: Redefining Corporate Spaces',
            'preview': 'A sustainable office campus that prioritizes energy efficiency, green spaces, and employee well-being, revolutionizing the concept of corporate environments.'
        },
        {
            'highlight_image': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg',
            'title': 'Cultural Heritage Center: Preserving Rich History',
            'preview': 'A cultural heritage center dedicated to preserving and celebrating the rich history, traditions, and cultural diversity of the community through exhibits, workshops, and performances.'
        },
        {
            'highlight_image': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg',
            'title': 'Innovative Educational Facility: Inspiring the Next Generation',
            'preview': 'An innovative educational facility designed to foster creativity, collaboration, and critical thinking, providing students with an inspiring and interactive learning environment.'
        }
    ]

    portfolio_grids = []
    for grid_dict in portfolio_grid_list:
        grid = PortfolioGrid(
            highlight_image=grid_dict["highlight_image"],
            title=grid_dict["title"],
            preview=grid_dict["preview"]
        )
        portfolio_grids.append(grid)

    db.session.add_all(portfolio_grids)
    db.session.commit()

def make_project_details():
    project_details_list = [
        {
            'grid_id': 1,
            'title': 'Sustainable Urban Housing Complex',
            'description': 'The Sustainable Urban Housing Complex is a visionary residential project that addresses the pressing need for sustainable living in densely populated cities. Through innovative design and advanced eco-friendly technologies, the complex offers a harmonious blend of comfortable living spaces, green landscapes, and renewable energy solutions. It aims to create a sustainable community that promotes a healthier and more environmentally conscious lifestyle.',
            'images': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg'
        },
        {
            'grid_id': 2,
            'title': 'Revitalizing Historic Landmark: City Library Renovation',
            'description': 'The City Library Renovation project is an ambitious undertaking to preserve the rich history and architectural heritage of a beloved landmark while adapting it to the evolving needs of the community. The renovation includes the restoration of the library\'s façade, revitalization of the interior spaces with state-of-the-art technology, flexible study areas, interactive learning zones, and community event spaces. The project seeks to create a dynamic and inviting environment that embraces the past while embracing the future.',
            'images': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg'
        },
        {
            'grid_id': 3,
            'title': 'Innovative Office Tower: The Future of Workplace Design',
            'description': 'The Innovative Office Tower project represents a paradigm shift in workplace design, where collaboration, well-being, and technological advancements converge. With its striking architecture, smart infrastructure, and energy-efficient systems, the tower offers a dynamic and productive environment for businesses of all sizes. From open-plan workstations to collaborative zones, quiet pods, and leisure areas, the design fosters a flexible and adaptable workspace that promotes employee engagement, creativity, and work-life balance.',
            'images': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg'
        },
        {
            'grid_id': 4,
            'title': 'Iconic Sports Arena: Fusion of Modernity and Tradition',
            'description': 'The Iconic Sports Arena project combines the best of modern design and timeless architectural aesthetics to create a venue that captivates both sports enthusiasts and architecture aficionados. The arena\'s sleek lines, innovative structural engineering, and advanced technology offer a state-of-the-art experience, while its nod to traditional architectural elements pays homage to the region\'s cultural heritage. The result is a striking and functional sports facility that becomes a symbol of pride for the community.',
            'images': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg'
        },
        {
            'grid_id': 5,
            'title': 'Eco-Friendly Resort: Harmonizing Luxury and Sustainability',
            'description': 'The Eco-Friendly Resort project redefines luxury hospitality by seamlessly integrating sustainability practices into every aspect of the guest experience. From energy-efficient design and renewable energy sources to locally sourced materials and eco-conscious amenities, the resort exemplifies responsible tourism. With lush landscapes, breathtaking views, and impeccable service, guests can indulge in a luxurious getaway while knowing their stay has a minimal ecological footprint.',
            'images': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg'
        },
        {
            'grid_id': 6,
            'title': 'Community Wellness Center: Nurturing Mind, Body, and Soul',
            'description': 'The Community Wellness Center project aims to create a haven for health and wellness, catering to the physical, mental, and emotional well-being of individuals and the community at large. The center offers a range of facilities, including fitness studios, indoor and outdoor sports areas, therapy rooms, educational spaces, and serene gardens. By providing accessible and comprehensive wellness programs, the center fosters a holistic approach to nurturing mind, body, and soul.',
            'images': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg'
        },
        {
            'grid_id': 7,
            'title': 'Modern Art Museum: Showcasing Contemporary Masterpieces',
            'description': 'The Modern Art Museum is a dynamic space that celebrates contemporary art in all its forms. Through innovative exhibition spaces, immersive installations, and interactive galleries, the museum offers visitors a unique and engaging experience. Showcasing a diverse collection of contemporary masterpieces, the museum serves as a platform for artists to express their creativity and for visitors to explore and appreciate the ever-evolving world of modern art.',
            'images': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg'
        },
        {
            'grid_id': 8,
            'title': 'Sustainable Office Campus: Redefining Corporate Spaces',
            'description': 'The Sustainable Office Campus project revolutionizes the concept of corporate environments by prioritizing energy efficiency, green spaces, and employee well-being. With its innovative design and sustainable features, the campus creates a productive and healthy work environment. From smart building systems to collaborative workspaces and recreational areas, the campus fosters a sense of community, creativity, and inspiration. It sets new standards for sustainable and people-centric corporate spaces.',
            'images': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg'
        },
        {
            'grid_id': 9,
            'title': 'Cultural Heritage Center: Preserving Rich History',
            'description': 'The Cultural Heritage Center is a tribute to the rich history, traditions, and cultural diversity of the community. Through immersive exhibits, interactive workshops, and captivating performances, the center brings the past to life and celebrates the vibrant heritage of the region. With its modern architecture and versatile spaces, the center serves as a hub for cultural exchange, education, and preservation, fostering a sense of pride and connection among residents and visitors alike.',
            'images': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg'
        },
        {
            'grid_id': 10,
            'title': 'Innovative Educational Facility: Inspiring the Next Generation',
            'description': 'The Innovative Educational Facility is designed to inspire and empower the next generation of learners. With its innovative architecture, flexible learning spaces, and cutting-edge technology, the facility creates an environment that fosters creativity, collaboration, and critical thinking. From interactive classrooms to state-of-the-art labs and maker spaces, the facility encourages hands-on exploration and personalized learning experiences. It aims to equip students with the skills and mindset needed to thrive in a rapidly evolving world.',
            'images': 'https://ssl.cdn-redfin.com/photo/91/mbphoto/988/genMid.988988_1_0.jpg'
        }
    ]

    project_details = []
    for project_detail_dict in project_details_list:
        project_detail = ProjectDetail(
            grid_id=project_detail_dict['grid_id'],
            title=project_detail_dict['title'],
            description=project_detail_dict['description'],
            images=project_detail_dict['images']
        )
        project_details.append(project_detail)

    db.session.add_all(project_details)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        make_users()
        make_portfolio_grids()
        make_project_details()
        print('Data creation completed.')