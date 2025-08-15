# # from nicegui import ui, app
# # from nicegui.element import Element

# # # Portfolio data
# # projects = [
# #     {
# #         'title': 'E-commerce Platform',
# #         'description': 'Full-featured online shopping platform with payment integration',
# #         'image': 'https://via.placeholder.com/400x250',
# #         'technologies': ['Python', 'Django', 'PostgreSQL', 'Stripe'],
# #         'link': 'https://github.com/example/project1'
# #     },
# #     {
# #         'title': 'Data Visualization Dashboard',
# #         'description': 'Interactive dashboard for analyzing business metrics',
# #         'image': 'https://via.placeholder.com/400x250',
# #         'technologies': ['Python', 'Plotly', 'Pandas', 'FastAPI'],
# #         'link': 'https://github.com/example/project2'
# #     },
# #     {
# #         'title': 'Mobile Task Manager',
# #         'description': 'Cross-platform task management application',
# #         'image': 'https://via.placeholder.com/400x250',
# #         'technologies': ['Flutter', 'Firebase', 'Dart'],
# #         'link': 'https://github.com/example/project3'
# #     }
# # ]

# # @ui.page('/')
# # def portfolio():
# #     # Header with navigation
# #     with ui.header().classes('bg-blue-600 text-white p-4 sticky top-0 z-10'):
# #         with ui.row().classes('w-full max-w-6xl mx-auto justify-between items-center'):
# #             with ui.column().classes('items-start'):
# #                 ui.label('Abdulah Zia').classes('text-2xl font-bold')
# #                 ui.label('Full Stack Developer').classes('text-sm opacity-80')
            
# #             with ui.row().classes('gap-4'):
# #                 ui.button('Home', on_click=lambda: ui.navigate.to('/')).classes('text-white')
# #                 ui.button('About', on_click=lambda: ui.scroll_to('#about')).classes('text-white')
# #                 ui.button('Projects', on_click=lambda: ui.scroll_to('#projects')).classes('text-white')
# #                 ui.button('Contact', on_click=lambda: ui.scroll_to('#contact')).classes('text-white')

# #     # Hero Section
# #     with ui.column().classes('w-full min-h-screen flex items-center justify-center p-8 bg-gradient-to-br from-blue-50 to-indigo-100'):
# #         with ui.card().classes('max-w-2xl p-8 shadow-xl rounded-xl'):
# #             ui.label('Hello, I\'Abdullah Zia').classes('text-4xl font-bold text-blue-800')
# #             ui.label('Full Stack Developer & UI/UX Enthusiast').classes('text-xl text-blue-600 mt-2')
# #             ui.label('I create beautiful, functional web applications with modern technologies').classes('text-gray-600 mt-4')
            
# #             with ui.row().classes('mt-6 gap-4'):
# #                 ui.button('View Projects', on_click=lambda: ui.scroll_to('#projects')).classes('bg-blue-600 hover:bg-blue-700 text-white')
# #                 ui.button('Contact Me', on_click=lambda: ui.scroll_to('#contact')).classes('border-2 border-blue-600 text-blue-600 hover:bg-blue-50')

# #     # About Section
# #     with ui.column().classes('w-full p-8 bg-white').props('id="about"'):
# #         ui.label('About Me').classes('text-3xl font-bold text-center text-blue-800 mb-8')
        
# #         with ui.row().classes('max-w-6xl mx-auto gap-8 items-center'):
# #             with ui.column().classes('w-1/2'):
# #                 ui.label('I\'m a passionate developer with 5+ years of experience creating web applications. I specialize in Python ecosystems and modern JavaScript frameworks.').classes('text-gray-700')
# #                 ui.label('My focus is on creating intuitive user experiences while maintaining clean, efficient code. I enjoy solving complex problems and learning new technologies.').classes('text-gray-700 mt-4')
                
# #                 with ui.row().classes('mt-6 gap-2'):
# #                     ui.chip('Python').classes('bg-blue-100 text-blue-800')
# #                     ui.chip('JavaScript').classes('bg-blue-100 text-blue-800')
# #                     ui.chip('React').classes('bg-blue-100 text-blue-800')
# #                     ui.chip('Django').classes('bg-blue-100 text-blue-800')
# #                     ui.chip('AWS').classes('bg-blue-100 text-blue-800')
            
# #             with ui.column().classes('w-1/2'):
# #                 ui.image('https://via.placeholder.com/500x400').classes('rounded-xl shadow-lg')

# #     # Projects Section
# #     with ui.column().classes('w-full p-8 bg-gray-50').props('id="projects"'):
# #         ui.label('My Projects').classes('text-3xl font-bold text-center text-blue-800 mb-8')
        
# #         with ui.row().classes('max-w-6xl mx-auto gap-8 flex-wrap justify-center'):
# #             for project in projects:
# #                 with ui.card().classes('w-96 shadow-lg rounded-xl overflow-hidden transition-transform hover:scale-105'):
# #                     ui.image(project['image']).classes('w-full h-48 object-cover')
# #                     with ui.card_section().classes('p-4'):
# #                         ui.label(project['title']).classes('text-xl font-bold text-blue-800')
# #                         ui.label(project['description']).classes('text-gray-600 mt-2')
                        
# #                         with ui.row().classes('mt-3 gap-1 flex-wrap'):
# #                             for tech in project['technologies']:
# #                                 ui.chip(tech).classes('bg-blue-100 text-blue-800 text-xs')
                        
# #                         with ui.row().classes('mt-4 justify-end'):
# #                             ui.button('View Project', on_click=lambda url=project['link']: ui.open(url)).classes('bg-blue-600 hover:bg-blue-700 text-white')

# #     # Contact Section
# #     with ui.column().classes('w-full p-8 bg-white').props('id="contact"'):
# #         ui.label('Get In Touch').classes('text-3xl font-bold text-center text-blue-800 mb-8')
        
# #         with ui.card().classes('max-w-2xl mx-auto p-6 shadow-lg rounded-xl'):
# #             name = ui.input('Name', placeholder='Your name').classes('w-full')
# #             email = ui.input('Email', placeholder='your.email@example.com').classes('w-full')
# #             message = ui.textarea('Message', placeholder='Your message here...').classes('w-full')
            
# #             def send_message():
# #                 ui.notify(f'Thank you {name.value}! Your message has been sent.', position='top')
# #                 name.value = ''
# #                 email.value = ''
# #                 message.value = ''
            
# #             ui.button('Send Message', on_click=send_message).classes('mt-4 bg-blue-600 hover:bg-blue-700 text-white w-full')

# #     # Footer
# #     with ui.footer().classes('bg-blue-600 text-white p-4'):
# #         with ui.row().classes('max-w-6xl mx-auto justify-between items-center'):
# #             ui.label('© 2023 John Doe. All rights reserved.')
# #             with ui.row().classes('gap-4'):
# #                 ui.button('GitHub', on_click=lambda: ui.open('https://github.com')).classes('text-white')
# #                 ui.button('LinkedIn', on_click=lambda: ui.open('https://linkedin.com')).classes('text-white')
# #                 ui.button('Twitter', on_click=lambda: ui.open('https://twitter.com')).classes('text-white')

# # # Add custom styles
# # ui.add_head_html("""
# # <style>
# #     .nicegui-content {
# #         max-width: 100%;
# #         padding: 0;
# #     }
# #     body {
# #         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
# #         margin: 0;
# #         padding: 0;
# #     }
# # </style>
# # """)

# # # Run the app
# # ui.run(port=8000, reload=True)


# #################################################

# from progressive_py.ntbk_progbar import NotebookProgressBar
# from progressive_py.utils import gradient_colors
# from progressive_py.manager import AssetsManager
# import time
# style = AssetsManager().load('progress_bar', 'style', 'its_cool')
# pb = NotebookProgressBar({
#     **style,
#     'txt_lf': "I'm Fast... [{percent:.0f}%] | ",
#     'txt_rt': "| ETA {eta} | Elapsed {elapsed}",
#     'colors': gradient_colors('#00ff00', '#0000ff', 15),
#     'paint': 'bar-by-bar',
#     'text_color': ['#efa', '#afe'],
#     'length': 15,
# })

# total = 100
# for i in range(total + 1):
#     pb.update(i/ total, i, total)
#     time.sleep(0.03)
# print("Progress Complete!")

####################################################

# from nicegui import ui

# # Define color scheme
# colors = {
#     'primary': '#4F46E5',  # Indigo
#     'secondary': '#10B981',  # Emerald
#     'accent': '#F59E0B',  # Amber
#     'danger': '#EF4444',  # Red
#     'dark': '#1F2937',  # Dark gray
#     'light': '#F3F4F6',  # Light gray
#     'purple': '#8B5CF6',  # Purple
#     'pink': '#EC4899',  # Pink
#     'blue': '#3B82F6',  # Blue
# }

# # Function to scroll to element
# def scroll_to_element(element_id):
#     ui.run_javascript(f'document.getElementById("{element_id}").scrollIntoView({{behavior: "smooth"}})')

# # Header with navigation
# @ui.page('/')
# def portfolio():
#     # Hero Section with ID for navigation
#     with ui.row().classes('w-full bg-gradient-to-r from-blue-500 to-indigo-600 text-white p-16').id('home'):
#         with ui.column().classes('max-w-6xl mx-auto items-center text-center'):
#             ui.label('Hello, I\'m Abdullah Zia').classes('text-5xl font-bold mb-4')
#             ui.label('17-year-old AI & Machine Learning Enthusiast').classes('text-2xl mb-6')
#             ui.label('F.A Graduate | Web Developer | AI Specialist').classes('text-xl mb-8')
#             ui.button('View My Work', on_click=lambda: scroll_to_element('projects')).classes('bg-white text-indigo-600 px-6 py-3 rounded-lg font-bold hover:bg-opacity-90 transition')

#     # Header
#     with ui.header().classes('bg-gradient-to-r from-indigo-600 to-purple-600 text-white'):
#         with ui.row().classes('w-full max-w-6xl mx-auto p-4 items-center justify-between'):
#             with ui.column():
#                 ui.label('Abdullah Zia').classes('text-2xl font-bold')
#                 ui.label('AI Enthusiast & Web Developer').classes('text-sm opacity-80')
            
#             with ui.row().classes('gap-4'):
#                 ui.button('Home', on_click=lambda: scroll_to_element('home')).classes('text-white')
#                 ui.button('Skills', on_click=lambda: scroll_to_element('skills')).classes('text-white')
#                 ui.button('Projects', on_click=lambda: scroll_to_element('projects')).classes('text-white')
#                 ui.button('Testimonials', on_click=lambda: scroll_to_element('testimonials')).classes('text-white')
#                 ui.button('Contact', on_click=lambda: scroll_to_element('contact')).classes('text-white')

#     # About Section
#     with ui.row().classes('w-full p-16 bg-gray-50'):
#         with ui.column().classes('max-w-6xl mx-auto items-center'):
#             ui.label('About Me').classes('text-4xl font-bold mb-8 text-gray-800')
#             with ui.row().classes('w-full gap-8 items-center'):
#                 with ui.column().classes('w-1/2'):
#                     ui.label('I am a 17-year-old passionate developer with expertise in Artificial Intelligence, Machine Learning, and Web Development. Despite my young age, I have dedicated myself to mastering cutting-edge technologies and building innovative solutions.').classes('text-lg text-gray-700')
#                     ui.button('Download Resume').classes('mt-4 bg-indigo-600 text-white px-6 py-2 rounded-lg font-bold hover:bg-indigo-700 transition')
                
#                 with ui.column().classes('w-1/2 items-center'):
#                     ui.image('https://picsum.photos/seed/abdullah/400/400').classes('rounded-full shadow-lg w-64 h-64 object-cover')

#     # Skills Section
#     with ui.row().classes('w-full p-16').id('skills'):
#         with ui.column().classes('max-w-6xl mx-auto items-center'):
#             ui.label('My Skills').classes('text-4xl font-bold mb-12 text-gray-800')
            
#             with ui.row().classes('w-full gap-8 justify-center'):
#                 # AI Skill Card
#                 with ui.card().classes('w-64 p-6 shadow-lg hover:shadow-xl transition-shadow'):
#                     with ui.column().classes('items-center'):
#                         ui.icon('psychology', size='4rem').classes('text-indigo-600 mb-4')
#                         ui.label('Artificial Intelligence').classes('text-xl font-bold mb-2')
#                         ui.label('Machine learning, deep learning, neural networks').classes('text-center text-gray-600')
                
#                 # ML Skill Card
#                 with ui.card().classes('w-64 p-6 shadow-lg hover:shadow-xl transition-shadow'):
#                     with ui.column().classes('items-center'):
#                         ui.icon('data_object', size='4rem').classes('text-emerald-600 mb-4')
#                         ui.label('Machine Learning').classes('text-xl font-bold mb-2')
#                         ui.label('Data analysis, predictive modeling, algorithms').classes('text-center text-gray-600')
                
#                 # Web Dev Skill Card
#                 with ui.card().classes('w-64 p-6 shadow-lg hover:shadow-xl transition-shadow'):
#                     with ui.column().classes('items-center'):
#                         ui.icon('code', size='4rem').classes('text-blue-600 mb-4')
#                         ui.label('Web Development').classes('text-xl font-bold mb-2')
#                         ui.label('Frontend, backend, full-stack development').classes('text-center text-gray-600')
                
#                 # Web App Skill Card
#                 with ui.card().classes('w-64 p-6 shadow-lg hover:shadow-xl transition-shadow'):
#                     with ui.column().classes('items-center'):
#                         ui.icon('web', size='4rem').classes('text-purple-600 mb-4')
#                         ui.label('Web Applications').classes('text-xl font-bold mb-2')
#                         ui.label('Interactive applications, UI/UX design').classes('text-center text-gray-600')

#     # Projects Section
#     with ui.row().classes('w-full p-16 bg-gray-50').id('projects'):
#         with ui.column().classes('max-w-6xl mx-auto items-center'):
#             ui.label('My Projects').classes('text-4xl font-bold mb-12 text-gray-800')
            
#             with ui.row().classes('w-full gap-8 justify-center'):
#                 # Project 1
#                 with ui.card().classes('w-96 shadow-lg hover:shadow-xl transition-shadow'):
#                     ui.image('https://picsum.photos/seed/project1/400/250').classes('w-full h-48 object-cover')
#                     with ui.card_section():
#                         ui.label('AI Image Recognition System').classes('text-xl font-bold mb-2')
#                         ui.label('A machine learning model that identifies objects in images with high accuracy.').classes('text-gray-600 mb-4')
#                         with ui.row().classes('gap-2'):
#                             ui.chip('Python').classes('bg-blue-100 text-blue-800')
#                             ui.chip('TensorFlow').classes('bg-orange-100 text-orange-800')
#                             ui.chip('Computer Vision').classes('bg-purple-100 text-purple-800')
                
#                 # Project 2
#                 with ui.card().classes('w-96 shadow-lg hover:shadow-xl transition-shadow'):
#                     ui.image('https://picsum.photos/seed/project2/400/250').classes('w-full h-48 object-cover')
#                     with ui.card_section():
#                         ui.label('E-commerce Web Application').classes('text-xl font-bold mb-2')
#                         ui.label('A full-featured online shopping platform with payment integration.').classes('text-gray-600 mb-4')
#                         with ui.row().classes('gap-2'):
#                             ui.chip('React').classes('bg-blue-100 text-blue-800')
#                             ui.chip('Node.js').classes('bg-green-100 text-green-800')
#                             ui.chip('MongoDB').classes('bg-emerald-100 text-emerald-800')
                
#                 # Project 3
#                 with ui.card().classes('w-96 shadow-lg hover:shadow-xl transition-shadow'):
#                     ui.image('https://picsum.photos/seed/project3/400/250').classes('w-full h-48 object-cover')
#                     with ui.card_section():
#                         ui.label('Predictive Analytics Dashboard').classes('text-xl font-bold mb-2')
#                         ui.label('Data visualization tool for business forecasting and insights.').classes('text-gray-600 mb-4')
#                         with ui.row().classes('gap-2'):
#                             ui.chip('Python').classes('bg-blue-100 text-blue-800')
#                             ui.chip('D3.js').classes('bg-yellow-100 text-yellow-800')
#                             ui.chip('Pandas').classes('bg-indigo-100 text-indigo-800')

#     # Testimonials Section
#     with ui.row().classes('w-full p-16').id('testimonials'):
#         with ui.column().classes('max-w-6xl mx-auto items-center'):
#             ui.label('What People Say').classes('text-4xl font-bold mb-12 text-gray-800')
            
#             with ui.row().classes('w-full gap-8 justify-center'):
#                 # Testimonial 1
#                 with ui.card().classes('w-96 p-6 shadow-lg hover:shadow-xl transition-shadow'):
#                     with ui.row().classes('items-center mb-4'):
#                         ui.image('https://picsum.photos/seed/person1/60/60').classes('rounded-full w-16 h-16 object-cover')
#                         with ui.column().classes('ml-4'):
#                             ui.label('Ahmed Khan').classes('font-bold')
#                             ui.label('Tech Startup CEO').classes('text-gray-600')
#                     ui.label('Abdullah is an incredibly talented developer. His AI solutions helped our startup optimize processes and save costs. Impressed by his skills at such a young age!').classes('text-gray-700 italic')
                
#                 # Testimonial 2
#                 with ui.card().classes('w-96 p-6 shadow-lg hover:shadow-xl transition-shadow'):
#                     with ui.row().classes('items-center mb-4'):
#                         ui.image('https://picsum.photos/seed/person2/60/60').classes('rounded-full w-16 h-16 object-cover')
#                         with ui.column().classes('ml-4'):
#                             ui.label('Sara Javed').classes('font-bold')
#                             ui.label('Project Manager').classes('text-gray-600')
#                     ui.label('Working with Abdullah was a pleasure. He delivered our web application ahead of schedule with exceptional quality. His technical knowledge is impressive.').classes('text-gray-700 italic')
                
#                 # Testimonial 3
#                 with ui.card().classes('w-96 p-6 shadow-lg hover:shadow-xl transition-shadow'):
#                     with ui.row().classes('items-center mb-4'):
#                         ui.image('https://picsum.photos/seed/person3/60/60').classes('rounded-full w-16 h-16 object-cover')
#                         with ui.column().classes('ml-4'):
#                             ui.label('Muhammad Ali').classes('font-bold')
#                             ui.label('Data Scientist').classes('text-gray-600')
#                     ui.label('Abdullah\'s machine learning models are top-notch. He has a deep understanding of algorithms and their practical applications. A rising star in the tech field!').classes('text-gray-700 italic')

#     # Contact Section
#     with ui.row().classes('w-full p-16 bg-gradient-to-r from-indigo-600 to-purple-600 text-white').id('contact'):
#         with ui.column().classes('max-w-6xl mx-auto items-center'):
#             ui.label('Get In Touch').classes('text-4xl font-bold mb-12')
            
#             with ui.row().classes('w-full gap-12'):
#                 with ui.column().classes('w-1/2'):
#                     ui.label('Contact Information').classes('text-2xl font-bold mb-6')
#                     with ui.row().classes('items-center mb-4'):
#                         ui.icon('phone', size='1.5rem').classes('mr-4')
#                         ui.label('03132691012').classes('text-lg')
                    
#                     with ui.row().classes('items-center mb-4'):
#                         ui.icon('email', size='1.5rem').classes('mr-4')
#                         ui.label('@zia2691.com').classes('text-lg')
                    
#                     with ui.row().classes('items-center mb-4'):
#                         ui.icon('location_on', size='1.5rem').classes('mr-4')
#                         ui.label('Pakistan').classes('text-lg')
                    
#                     with ui.row().classes('gap-4 mt-8'):
#                         ui.button('GitHub', on_click=lambda: ui.open('https://github.com')).classes('bg-gray-800 text-white px-4 py-2 rounded-lg')
#                         ui.button('LinkedIn', on_click=lambda: ui.open('https://linkedin.com')).classes('bg-blue-700 text-white px-4 py-2 rounded-lg')
#                         ui.button('Twitter', on_click=lambda: ui.open('https://twitter.com')).classes('bg-blue-400 text-white px-4 py-2 rounded-lg')
                
#                 with ui.column().classes('w-1/2'):
#                     ui.label('Send Me a Message').classes('text-2xl font-bold mb-6')
#                     name_input = ui.input('Name').classes('w-full mb-4 text-gray-800')
#                     email_input = ui.input('Email').classes('w-full mb-4 text-gray-800')
#                     message_input = ui.textarea('Message').classes('w-full mb-4 text-gray-800')
                    
#                     def show_notification():
#                         ui.notify('Message sent successfully!', position='top', color='positive')
                    
#                     ui.button('Send Message', on_click=show_notification).classes('bg-white text-indigo-600 px-6 py-2 rounded-lg font-bold hover:bg-opacity-90 transition')

#     # Footer
#     with ui.footer().classes('bg-gray-900 text-white p-8'):
#         with ui.column().classes('max-w-6xl mx-auto items-center text-center'):
#             ui.label('© 2023 Abdullah Zia. All rights reserved.').classes('mb-2')
#             ui.label('Designed and built with ❤️ using NiceGUI').classes('text-gray-400')

# ui.run()


###################################33

# from nicegui import ui
# from nicegui.events import ValueChangeEventArguments

# # Define custom CSS for gradients and styling
# custom_css = """
# :root {
#   --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#   --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
#   --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
#   --dark-gradient: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
#   --card-gradient: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
#   --text-color: #e0e0e0;
#   --card-bg: rgba(30, 30, 45, 0.7);
#   --pattern-bg: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
# }

# body {
#   background: var(--dark-gradient);
#   color: var(--text-color);
#   font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#   margin: 0;
#   padding: 0;
# }

# .hero-section {
#   background: var(--primary-gradient), var(--pattern-bg);
#   background-blend-mode: overlay;
#   border-radius: 15px;
#   padding: 3rem;
#   margin-bottom: 2rem;
#   box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
#   position: relative;
#   overflow: hidden;
# }

# .hero-section::before {
#   content: '';
#   position: absolute;
#   top: -50%;
#   right: -50%;
#   width: 200%;
#   height: 200%;
#   background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
#   z-index: 0;
# }

# .hero-content {
#   position: relative;
#   z-index: 1;
# }

# .profile-image {
#   border-radius: 50%;
#   border: 4px solid rgba(255, 255, 255, 0.3);
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
#   width: 200px;
#   height: 200px;
#   object-fit: cover;
# }

# .card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }

# .card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }

# .card-image {
#   border-radius: 10px;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   width: 100%;
#   height: auto;
#   object-fit: cover;
# }

# .header, .footer {
#   background: rgba(30, 30, 45, 0.8);
#   backdrop-filter: blur(10px);
#   padding: 1rem;
#   border-radius: 10px;
#   margin-bottom: 1rem;
# }

# .header {
#   border-bottom: 1px solid rgba(255, 255, 255, 0.1);
# }

# .footer {
#   border-top: 1px solid rgba(255, 255, 255, 0.1);
#   margin-top: 2rem;
# }

# .rating {
#   color: #ffd700;
# }

# .btn-primary {
#   background: var(--primary-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }

# .btn-primary:hover {
#   transform: scale(1.05);
# }

# .skill-tag {
#   background: var(--accent-gradient);
#   border-radius: 20px;
#   padding: 0.3rem 0.8rem;
#   margin: 0.2rem;
#   display: inline-block;
#   font-size: 0.9rem;
#   font-weight: 500;
# }
# """

# @ui.page('/')
# def portfolio():
#     ui.add_head_html(f'<style>{custom_css}</style>')
    
#     # Header
#     with ui.header().classes('header w-full max-w-6xl mx-auto'):
#         with ui.row().classes('w-full justify-between items-center'):
#             with ui.column():
#                 ui.label('Ahsan Ali Portfolio').classes('text-2xl font-bold')
#             with ui.row().classes('gap-4'):
#                 ui.button('Home', on_click=lambda: ui.open('/')).classes('btn-primary')
#                 ui.button('Skills', on_click=lambda: ui.scroll_to('skills-section')).classes('btn-primary')
#                 ui.button('Contact', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary')
    
#     # Main content
#     with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
        
#         # Hero Section
#         with ui.column().classes('hero-section'):
#             with ui.row().classes('w-full justify-between items-center gap-8'):
#                 with ui.column().classes('hero-content w-full md:w-2/3'):
#                     ui.label('Ahsan Ali').classes('text-4xl md:text-5xl font-bold mb-2')
#                     ui.label('Computer Scientist, Web Developer & Python Programmer').classes('text-xl md:text-2xl mb-4')
#                     ui.label('BSCS Graduate | HND Punjab, Pakistan').classes('text-lg mb-6')
#                     with ui.row().classes('gap-2 items-center mb-4'):
#                         ui.label('Client Rating:').classes('text-lg')
#                         for _ in range(5):
#                             ui.icon('star', color='gold').classes('rating')
#                         ui.label('(5/5)').classes('text-lg')
#                     ui.button('Contact Me', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary mt-2')
#                 with ui.column().classes('w-full md:w-1/3 flex justify-center'):
#                     ui.image('https://picsum.photos/seed/ahsanali/400/400').classes('profile-image')
        
#         # Skills Section
#         with ui.column().classes('w-full').props('id="skills-section"'):
#             ui.label('Skills & Expertise').classes('text-3xl font-bold mb-6 text-center')
            
#             # Card 1 - Full Stack Development
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/fullstack/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Professional Full Stack Developer').classes('text-2xl font-bold mb-2')
#                         ui.label('Experienced in developing end-to-end web applications with modern frameworks and technologies. Proficient in both frontend and backend development to create seamless user experiences.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('React').classes('skill-tag')
#                             ui.label('Node.js').classes('skill-tag')
#                             ui.label('Django').classes('skill-tag')
#                             ui.label('MongoDB').classes('skill-tag')
            
#             # Card 2 - Problem Solver (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/problemsolving/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Problem Solver').classes('text-2xl font-bold mb-2')
#                         ui.label('Skilled at analyzing complex problems and developing efficient solutions. Strong analytical thinking combined with creativity to overcome challenges in software development and system design.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Critical Thinking').classes('skill-tag')
#                             ui.label('Algorithm Design').classes('skill-tag')
#                             ui.label('System Architecture').classes('skill-tag')
            
#             # Card 3 - Bug Hunter
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/bughunter/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Bug Hunter').classes('text-2xl font-bold mb-2')
#                         ui.label('Expertise in identifying, diagnosing, and resolving software defects. Meticulous attention to detail ensures robust and error-free applications that meet the highest quality standards.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Debugging').classes('skill-tag')
#                             ui.label('Testing').classes('skill-tag')
#                             ui.label('Code Review').classes('skill-tag')
            
#             # Card 4 - Python Programmer (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/pythondev/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('High-Level Python Programmer').classes('text-2xl font-bold mb-2')
#                         ui.label('Advanced proficiency in Python programming with expertise in developing scalable applications, data analysis, automation scripts, and machine learning models.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Python').classes('skill-tag')
#                             ui.label('Django').classes('skill-tag')
#                             ui.label('FastAPI').classes('skill-tag')
#                             ui.label('Data Science').classes('skill-tag')
        
#         # Contact Section
#         with ui.column().classes('w-full mt-8').props('id="contact-section"'):
#             ui.label('Get In Touch').classes('text-3xl font-bold mb-6 text-center')
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Contact Information').classes('text-2xl font-bold mb-4')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('person', color='primary')
#                             ui.label('Ahsan Ali').classes('text-lg')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('location_on', color='primary')
#                             ui.label('HND Punjab, Pakistan').classes('text-lg')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('phone', color='primary')
#                             ui.label('0305 0044532').classes('text-lg')
#                         with ui.row().classes('items-center gap-3'):
#                             ui.icon('email', color='primary')
#                             ui.label('contact@example.com').classes('text-lg')
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Send a Message').classes('text-2xl font-bold mb-4')
#                         name_input = ui.input('Name').classes('w-full mb-3')
#                         email_input = ui.input('Email').classes('w-full mb-3')
#                         message_input = ui.textarea('Message').classes('w-full mb-3')
#                         ui.button('Send Message', on_click=lambda: handle_form_submit(name_input.value, email_input.value, message_input.value)).classes('btn-primary')
    
#     # Footer
#     with ui.footer().classes('footer w-full max-w-6xl mx-auto mt-8'):
#         with ui.column.fix().classes('w-full items-center'):
#             ui.label('© 2023 Ahsan Ali - Computer Scientist & Web Developer').classes('text-center')
#             with ui.row().classes('gap-4 mt-2'):
#                 ui.button('LinkedIn').classes('btn-primary')
#                 ui.button('GitHub').classes('btn-primary')
#                 ui.button('Twitter').classes('btn-primary')

# def handle_form_submit(name, email, message):
#     if name and email and message:
#         ui.notify(f'Thank you {name}! Your message has been sent.', color='positive')
#     else:
#         ui.notify('Please fill in all fields.', color='negative')

# ui.run()
#3#3###########   ahsan
##########333333333333333333333

# from nicegui import ui
# from nicegui.events import ValueChangeEventArguments
# # Define custom CSS for gradients and styling
# custom_css = """
# :root {
#   --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#   --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
#   --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
#   --dark-gradient: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
#   --card-gradient: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
#   --text-color: #e0e0e0;
#   --card-bg: rgba(30, 30, 45, 0.7);
#   --pattern-bg: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
# }
# body {
#   background: var(--dark-gradient);
#   color: var(--text-color);
#   font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#   margin: 0;
#   padding: 0;
# }
# .hero-section {
#   background: var(--primary-gradient), var(--pattern-bg);
#   background-blend-mode: overlay;
#   border-radius: 15px;
#   padding: 3rem;
#   margin-bottom: 2rem;
#   box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
#   position: relative;
#   overflow: hidden;
# }
# .hero-section::before {
#   content: '';
#   position: absolute;
#   top: -50%;
#   right: -50%;
#   width: 200%;
#   height: 200%;
#   background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
#   z-index: 0;
# }
# .hero-content {
#   position: relative;
#   z-index: 1;
# }
# .profile-image {
#   border-radius: 50%;
#   border: 4px solid rgba(255, 255, 255, 0.3);
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
#   width: 200px;
#   height: 200px;
#   object-fit: cover;
# }
# .card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .card-image {
#   border-radius: 10px;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   width: 100%;
#   height: auto;
#   object-fit: cover;
# }
# .header, .footer {
#   background: rgba(30, 30, 45, 0.8);
#   backdrop-filter: blur(10px);
#   padding: 1rem;
#   border-radius: 10px;
#   margin-bottom: 1rem;
# }
# .header {
#   border-bottom: 1px solid rgba(255, 255, 255, 0.1);
# }
# .footer {
#   border-top: 1px solid rgba(255, 255, 255, 0.1);
#   margin-top: 2rem;
# }
# .rating {
#   color: #ffd700;
# }
# .btn-primary {
#   background: var(--primary-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-primary:hover {
#   transform: scale(1.05);
# }
# .skill-tag {
#   background: var(--accent-gradient);
#   border-radius: 20px;
#   padding: 0.3rem 0.8rem;
#   margin: 0.2rem;
#   display: inline-block;
#   font-size: 0.9rem;
#   font-weight: 500;
# }
# """

# @ui.page('/')
# def portfolio():
#     ui.add_head_html(f'<style>{custom_css}</style>')
    
#     # Header
#     with ui.header().classes('header w-full max-w-6xl mx-auto'):
#         with ui.row().classes('w-full justify-between items-center'):
#             with ui.column():
#                 ui.label('Ahsan Ali Portfolio').classes('text-2xl font-bold')
#             with ui.row().classes('gap-4'):
#                 ui.button('Home', on_click=lambda: ui.open('/')).classes('btn-primary')
#                 ui.button('Skills', on_click=lambda: ui.scroll_to('skills-section')).classes('btn-primary')
#                 ui.button('Contact', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary')
    
#     # Main content
#     with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
        
#         # Hero Section
#         with ui.column().classes('hero-section'):
#             with ui.row().classes('w-full justify-between items-center gap-8'):
#                 with ui.column().classes('hero-content w-full md:w-2/3'):
#                     ui.label('Ahsan Ali').classes('text-4xl md:text-5xl font-bold mb-2')
#                     ui.label('Computer Scientist, Web Developer & Python Programmer').classes('text-xl md:text-2xl mb-4')
#                     ui.label('BSCS Graduate | HND Punjab, Pakistan').classes('text-lg mb-6')
#                     with ui.row().classes('gap-2 items-center mb-4'):
#                         ui.label('Client Rating:').classes('text-lg')
#                         for _ in range(5):
#                             ui.icon('star', color='gold').classes('rating')
#                         ui.label('(5/5)').classes('text-lg')
#                     ui.button('Contact Me', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary mt-2')
#                 with ui.column().classes('w-full md:w-1/3 flex justify-center'):
#                     ui.image('https://picsum.photos/seed/ahsanali/400/400').classes('profile-image')
        
#         # Skills Section
#         with ui.column().classes('w-full').props('id="skills-section"'):
#             ui.label('Skills & Expertise').classes('text-3xl font-bold mb-6 text-center')
            
#             # Card 1 - Full Stack Development
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/fullstack/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Professional Full Stack Developer').classes('text-2xl font-bold mb-2')
#                         ui.label('Experienced in developing end-to-end web applications with modern frameworks and technologies. Proficient in both frontend and backend development to create seamless user experiences.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('React').classes('skill-tag')
#                             ui.label('Node.js').classes('skill-tag')
#                             ui.label('Django').classes('skill-tag')
#                             ui.label('MongoDB').classes('skill-tag')
            
#             # Card 2 - Problem Solver (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/problemsolving/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Problem Solver').classes('text-2xl font-bold mb-2')
#                         ui.label('Skilled at analyzing complex problems and developing efficient solutions. Strong analytical thinking combined with creativity to overcome challenges in software development and system design.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Critical Thinking').classes('skill-tag')
#                             ui.label('Algorithm Design').classes('skill-tag')
#                             ui.label('System Architecture').classes('skill-tag')
            
#             # Card 3 - Bug Hunter
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/bughunter/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Bug Hunter').classes('text-2xl font-bold mb-2')
#                         ui.label('Expertise in identifying, diagnosing, and resolving software defects. Meticulous attention to detail ensures robust and error-free applications that meet the highest quality standards.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Debugging').classes('skill-tag')
#                             ui.label('Testing').classes('skill-tag')
#                             ui.label('Code Review').classes('skill-tag')
            
#             # Card 4 - Python Programmer (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/pythondev/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('High-Level Python Programmer').classes('text-2xl font-bold mb-2')
#                         ui.label('Advanced proficiency in Python programming with expertise in developing scalable applications, data analysis, automation scripts, and machine learning models.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Python').classes('skill-tag')
#                             ui.label('Django').classes('skill-tag')
#                             ui.label('FastAPI').classes('skill-tag')
#                             ui.label('Data Science').classes('skill-tag')
        
#         # Contact Section
#         with ui.column().classes('w-full mt-8').props('id="contact-section"'):
#             ui.label('Get In Touch').classes('text-3xl font-bold mb-6 text-center')
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Contact Information').classes('text-2xl font-bold mb-4')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('person', color='primary')
#                             ui.label('Ahsan Ali').classes('text-lg')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('location_on', color='primary')
#                             ui.label('HND Punjab, Pakistan').classes('text-lg')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('phone', color='primary')
#                             ui.label('0305 0044532').classes('text-lg')
#                         with ui.row().classes('items-center gap-3'):
#                             ui.icon('email', color='primary')
#                             ui.label('contact@example.com').classes('text-lg')
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Send a Message').classes('text-2xl font-bold mb-4')
#                         name_input = ui.input('Name').classes('w-full mb-3')
#                         email_input = ui.input('Email').classes('w-full mb-3')
#                         message_input = ui.textarea('Message').classes('w-full mb-3')
#                         ui.button('Send Message', on_click=lambda: handle_form_submit(name_input.value, email_input.value, message_input.value)).classes('btn-primary')
    
#     # Footer
#     with ui.footer().classes('footer w-full max-w-6xl mx-auto mt-8'):
#         with ui.column().classes('w-full items-center'):  # Fixed: removed .fix()
#             ui.label('© 2023 Ahsan Ali - Computer Scientist & Web Developer').classes('text-center')
#             with ui.row().classes('gap-4 mt-2'):
#                 ui.button('LinkedIn').classes('btn-primary')
#                 ui.button('GitHub').classes('btn-primary')
#                 ui.button('Twitter').classes('btn-primary')

# def handle_form_submit(name, email, message):
#     if name and email and message:
#         ui.notify(f'Thank you {name}! Your message has been sent.', color='positive')
#     else:
#         ui.notify('Please fill in all fields.', color='negative')

# ui.run()

#####################################

# from nicegui import ui
# from nicegui.events import ValueChangeEventArguments

# # Define custom CSS for gradients and styling
# custom_css = """
# :root {
#   --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#   --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
#   --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
#   --success-gradient: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
#   --warning-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
#   --dark-gradient: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
#   --card-gradient: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
#   --text-color: #e0e0e0;
#   --card-bg: rgba(30, 30, 45, 0.7);
#   --pattern-bg: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
# }
# body {
#   background: var(--dark-gradient);
#   color: var(--text-color);
#   font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#   margin: 0;
#   padding: 0;
# }
# .hero-section {
#   background: var(--primary-gradient), var(--pattern-bg);
#   background-blend-mode: overlay;
#   border-radius: 15px;
#   padding: 3rem;
#   margin-bottom: 2rem;
#   box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
#   position: relative;
#   overflow: hidden;
# }
# .hero-section::before {
#   content: '';
#   position: absolute;
#   top: -50%;
#   right: -50%;
#   width: 200%;
#   height: 200%;
#   background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
#   z-index: 0;
# }
# .hero-content {
#   position: relative;
#   z-index: 1;
# }
# .profile-image {
#   border-radius: 50%;
#   border: 4px solid rgba(255, 255, 255, 0.3);
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
#   width: 200px;
#   height: 200px;
#   object-fit: cover;
# }
# .card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .card-image {
#   border-radius: 10px;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   width: 100%;
#   height: auto;
#   object-fit: cover;
# }
# .header, .footer {
#   background: rgba(30, 30, 45, 0.8);
#   backdrop-filter: blur(10px);
#   padding: 1rem;
#   border-radius: 10px;
#   margin-bottom: 1rem;
# }
# .header {
#   border-bottom: 1px solid rgba(255, 255, 255, 0.1);
# }
# .footer {
#   border-top: 1px solid rgba(255, 255, 255, 0.1);
#   margin-top: 2rem;
# }
# .rating {
#   color: #ffd700;
# }
# .btn-primary {
#   background: var(--primary-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-primary:hover {
#   transform: scale(1.05);
# }
# .skill-tag {
#   border-radius: 20px;
#   padding: 0.3rem 0.8rem;
#   margin: 0.2rem;
#   display: inline-block;
#   font-size: 0.9rem;
#   font-weight: 500;
# }
# .ai-tag {
#   background: var(--secondary-gradient);
# }
# .ml-tag {
#   background: var(--accent-gradient);
# }
# .web-tag {
#   background: var(--success-gradient);
# }
# .app-tag {
#   background: var(--warning-gradient);
# }
# .testimonial-card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .testimonial-card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .project-card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .project-card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# """

# @ui.page('/')
# def portfolio():
#     ui.add_head_html(f'<style>{custom_css}</style>')
    
#     # Header
#     with ui.header().classes('header w-full max-w-6xl mx-auto'):
#         with ui.row().classes('w-full justify-between items-center'):
#             with ui.column():
#                 ui.label('Abdullah Zia Portfolio').classes('text-2xl font-bold')
#             with ui.row().classes('gap-4'):
#                 ui.button('Home', on_click=lambda: ui.open('/')).classes('btn-primary')
#                 ui.button('Skills', on_click=lambda: ui.scroll_to('skills-section')).classes('btn-primary')
#                 ui.button('Projects', on_click=lambda: ui.scroll_to('projects-section')).classes('btn-primary')
#                 ui.button('Testimonials', on_click=lambda: ui.scroll_to('testimonials-section')).classes('btn-primary')
#                 ui.button('Contact', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary')
    
#     # Main content
#     with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
        
#         # Hero Section
#         with ui.column().classes('hero-section'):
#             with ui.row().classes('w-full justify-between items-center gap-8'):
#                 with ui.column().classes('hero-content w-full md:w-2/3'):
#                     ui.label('Abdullah Zia').classes('text-4xl md:text-5xl font-bold mb-2')
#                     ui.label('AI Enthusiast & Web Developer').classes('text-xl md:text-2xl mb-4')
#                     ui.label('F.A Graduate ').classes('text-lg mb-6')
#                     with ui.row().classes('gap-2 items-center mb-4'):
#                         ui.label('Client Rating:').classes('text-lg')
#                         for _ in range(5):
#                             ui.icon('star', color='gold').classes('rating')
#                         ui.label('(5/5)').classes('text-lg')
#                     ui.button('Contact Me', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary mt-2')
#                 with ui.column().classes('w-full md:w-1/3 flex justify-center'):
#                     ui.image('ab.zia.jpg/abdullahzia/400/400').classes('profile-image')
        
#         # Skills Section
#         with ui.column().classes('w-full').props('id="skills-section"'):
#             ui.label('Skills & Expertise').classes('text-3xl font-bold mb-6 text-center')
            
#             # Card 1 - AI
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/ai/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Artificial Intelligence').classes('text-2xl font-bold mb-2')
#                         ui.label('Passionate about AI technologies and their applications in solving real-world problems. Continuously learning and exploring new AI frameworks and methodologies.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Machine Learning').classes('skill-tag ai-tag')
#                             ui.label('Neural Networks').classes('skill-tag ai-tag')
#                             ui.label('Deep Learning').classes('skill-tag ai-tag')
            
#             # Card 2 - Machine Learning (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/ml/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Machine Learning').classes('text-2xl font-bold mb-2')
#                         ui.label('Developing predictive models and algorithms to extract insights from data. Experienced in various ML techniques and data preprocessing methods.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Data Analysis').classes('skill-tag ml-tag')
#                             ui.label('Predictive Modeling').classes('skill-tag ml-tag')
#                             ui.label('Algorithms').classes('skill-tag ml-tag')
            
#             # Card 3 - Web Developer
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/webdev/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Web Developer').classes('text-2xl font-bold mb-2')
#                         ui.label('Creating responsive and user-friendly websites with modern technologies. Focused on clean code, performance optimization, and cross-browser compatibility.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('HTML/CSS').classes('skill-tag web-tag')
#                             ui.label('JavaScript').classes('skill-tag web-tag')
#                             ui.label('React').classes('skill-tag web-tag')
            
#             # Card 4 - Web Applications (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/webapp/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Web Applications').classes('text-2xl font-bold mb-2')
#                         ui.label('Building interactive and dynamic web applications with robust backend systems. Experienced in full-stack development and database management.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Frontend').classes('skill-tag app-tag')
#                             ui.label('Backend').classes('skill-tag app-tag')
#                             ui.label('Database').classes('skill-tag app-tag')
        
#         # Projects Section
#         with ui.column().classes('w-full mt-8').props('id="projects-section"'):
#             ui.label('My Projects').classes('text-3xl font-bold mb-6 text-center')
            
#             with ui.row().classes('w-full gap-6 justify-center'):
#                 # Project 1
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project1/400/250').classes('card-image w-full')
#                     ui.label('AI Image Recognition').classes('text-xl font-bold mt-4')
#                     ui.label('A machine learning model that identifies objects in images with high accuracy.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
                
#                 # Project 2
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project2/400/250').classes('card-image w-full')
#                     ui.label('E-commerce Website').classes('text-xl font-bold mt-4')
#                     ui.label('A full-featured online shopping platform with payment integration.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
                
#                 # Project 3
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project3/400/250').classes('card-image w-full')
#                     ui.label('Data Visualization Dashboard').classes('text-xl font-bold mt-4')
#                     ui.label('Interactive dashboard for visualizing complex datasets and trends.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
        
#         # Testimonials Section
#         with ui.column().classes('w-full mt-8').props('id="testimonials-section"'):
#             ui.label('What People Say').classes('text-3xl font-bold mb-6 text-center')
            
#             with ui.row().classes('w-full gap-6 justify-center'):
#                 # Testimonial 1
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person1/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Ahmed Khan').classes('font-bold')
#                             ui.label('Tech Startup CEO').classes('text-sm')
#                     ui.label('Abdullah is an incredibly talented developer. His AI solutions helped our startup optimize processes and save costs. Impressed by his skills at such a young age!').classes('text-sm italic')
                
#                 # Testimonial 2
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person2/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Sara Javed').classes('font-bold')
#                             ui.label('Project Manager').classes('text-sm')
#                     ui.label('Working with Abdullah was a pleasure. He delivered our web application ahead of schedule with exceptional quality. His technical knowledge is impressive.').classes('text-sm italic')
                
#                 # Testimonial 3
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person3/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Muhammad Ali').classes('font-bold')
#                             ui.label('Data Scientist').classes('text-sm')
#                     ui.label('Abdullah\'s machine learning models are top-notch. He has a deep understanding of algorithms and their practical applications. A rising star in the tech field!').classes('text-sm italic')
        
#         # Contact Section
#         with ui.column().classes('w-full mt-8').props('id="contact-section"'):
#             ui.label('Get In Touch').classes('text-3xl font-bold mb-6 text-center')
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Contact Information').classes('text-2xl font-bold mb-4')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('person', color='primary')
#                             ui.label('Abdullah Zia').classes('text-lg')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('cake', color='primary')
#                             ui.label('Age: 17').classes('text-lg')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('school', color='primary')
#                             ui.label('F.A Graduate').classes('text-lg')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('phone', color='primary')
#                             ui.label('03132691012').classes('text-lg')
#                         with ui.row().classes('items-center gap-3'):
#                             ui.icon('email', color='primary')
#                             ui.label('@zia2691.com').classes('text-lg')
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Send a Message').classes('text-2xl font-bold mb-4')
#                         name_input = ui.input('Name').classes('w-full mb-3')
#                         email_input = ui.input('Email').classes('w-full mb-3')
#                         message_input = ui.textarea('Message').classes('w-full mb-3')
#                         ui.button('Send Message', on_click=lambda: handle_form_submit(name_input.value, email_input.value, message_input.value)).classes('btn-primary')
    
#     # Footer
#     with ui.footer().classes('footer w-full max-w-6xl mx-auto mt-8'):
#         with ui.column().classes('w-full items-center'):
#             ui.label('© 2023 Abdullah Zia - AI Enthusiast & Web Developer').classes('text-center')
#             with ui.row().classes('gap-4 mt-2'):
#                 ui.button('LinkedIn').classes('btn-primary')
#                 ui.button('GitHub').classes('btn-primary')
#                 ui.button('Twitter').classes('btn-primary')

# def handle_form_submit(name, email, message):
#     if name and email and message:
#         ui.notify(f'Thank you {name}! Your message has been sent.', color='positive')
#     else:
#         ui.notify('Please fill in all fields.', color='negative')

# ui.run()

###################################

# from nicegui import ui
# from nicegui.events import ValueChangeEventArguments
# # Define custom CSS for gradients and styling
# custom_css = """
# :root {
#   --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#   --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
#   --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
#   --success-gradient: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
#   --warning-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
#   --dark-gradient: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
#   --card-gradient: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
#   --text-color: #e0e0e0;
#   --card-bg: rgba(30, 30, 45, 0.7);
#   --pattern-bg: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
# }
# body {
#   background: var(--dark-gradient);
#   color: var(--text-color);
#   font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#   margin: 0;
#   padding: 0;
# }
# .hero-section {
#   background: var(--primary-gradient), var(--pattern-bg);
#   background-blend-mode: overlay;
#   border-radius: 15px;
#   padding: 3rem;
#   margin-bottom: 2rem;
#   box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
#   position: relative;
#   overflow: hidden;
# }
# .hero-section::before {
#   content: '';
#   position: absolute;
#   top: -50%;
#   right: -50%;
#   width: 200%;
#   height: 200%;
#   background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
#   z-index: 0;
# }
# .hero-content {
#   position: relative;
#   z-index: 1;
# }
# .profile-image {
#   border-radius: 50%;
#   border: 4px solid rgba(255, 255, 255, 0.3);
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
#   width: 200px;
#   height: 200px;
#   object-fit: cover;
# }
# .card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .card-image {
#   border-radius: 10px;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   width: 100%;
#   height: auto;
#   object-fit: cover;
# }
# .header, .footer {
#   background: rgba(30, 30, 45, 0.8);
#   backdrop-filter: blur(10px);
#   padding: 1rem;
#   border-radius: 10px;
#   margin-bottom: 1rem;
# }
# .header {
#   border-bottom: 1px solid rgba(255, 255, 255, 0.1);
# }
# .footer {
#   border-top: 1px solid rgba(255, 255, 255, 0.1);
#   margin-top: 2rem;
# }
# .rating {
#   color: #ffd700;
# }
# .btn-primary {
#   background: var(--primary-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-primary:hover {
#   transform: scale(1.05);
# }
# .skill-tag {
#   border-radius: 20px;
#   padding: 0.3rem 0.8rem;
#   margin: 0.2rem;
#   display: inline-block;
#   font-size: 0.9rem;
#   font-weight: 500;
# }
# .ai-tag {
#   background: var(--secondary-gradient);
# }
# .ml-tag {
#   background: var(--accent-gradient);
# }
# .web-tag {
#   background: var(--success-gradient);
# }
# .app-tag {
#   background: var(--warning-gradient);
# }
# .testimonial-card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .testimonial-card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .project-card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .project-card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .example-card {
#   background: rgba(255, 255, 255, 0.05);
#   border-radius: 10px;
#   padding: 1rem;
#   margin-top: 1rem;
#   border-left: 3px solid;
# }
# .ai-example {
#   border-left-color: #f093fb;
# }
# .ml-example {
#   border-left-color: #4facfe;
# }
# .web-example {
#   border-left-color: #43e97b;
# }
# .app-example {
#   border-left-color: #fa709a;
# }
# """
# @ui.page('/')
# def portfolio():
#     ui.add_head_html(f'<style>{custom_css}</style>')
    
#     # Header
#     with ui.header().classes('header w-full max-w-6xl mx-auto'):
#         with ui.row().classes('w-full justify-between items-center'):
#             with ui.column():
#                 ui.label('Abdullah Zia Portfolio').classes('text-2xl font-bold')
#             with ui.row().classes('gap-4'):
#                 ui.button('Home', on_click=lambda: ui.open('/')).classes('btn-primary')
#                 ui.button('Skills', on_click=lambda: ui.scroll_to('skills-section')).classes('btn-primary')
#                 ui.button('Projects', on_click=lambda: ui.scroll_to('projects-section')).classes('btn-primary')
#                 ui.button('Testimonials', on_click=lambda: ui.scroll_to('testimonials-section')).classes('btn-primary')
#                 ui.button('Contact', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary')
    
#     # Main content
#     with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
        
#         # Hero Section
#         with ui.column().classes('hero-section'):
#             with ui.row().classes('w-full justify-between items-center gap-8'):
#                 with ui.column().classes('hero-content w-full md:w-2/3'):
#                     ui.label('Abdullah Zia').classes('text-4xl md:text-5xl font-bold mb-2')
#                     ui.label('AI Enthusiast & Web Developer').classes('text-xl md:text-2xl mb-4')
#                     ui.label('F.A Graduate ').classes('text-lg mb-6')
#                     with ui.row().classes('gap-2 items-center mb-4'):
#                         ui.label('Client Rating:').classes('text-lg')
#                         for _ in range(5):
#                             ui.icon('star', color='gold').classes('rating')
#                         ui.label('(5/5)').classes('text-lg')
#                     ui.button('Contact Me', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary mt-2')
#                 with ui.column().classes('w-full md:w-1/3 flex justify-center'):
#                     ui.image('https://picsum.photos/seed/abdullahzia/400/400').classes('profile-image')
        
#         # Skills Section
#         with ui.column().classes('w-full').props('id="skills-section"'):
#             ui.label('Skills & Expertise').classes('text-3xl font-bold mb-6 text-center')
            
#             # Card 1 - AI
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/ai/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Artificial Intelligence').classes('text-2xl font-bold mb-2')
#                         ui.label('Passionate about AI technologies and their applications in solving real-world problems. Continuously learning and exploring new AI frameworks and methodologies.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Machine Learning').classes('skill-tag ai-tag')
#                             ui.label('Neural Networks').classes('skill-tag ai-tag')
#                             ui.label('Deep Learning').classes('skill-tag ai-tag')
                        
#                         # AI Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card ai-example'):
#                                 ui.label('Chatbot Development').classes('font-bold mb-1')
#                                 ui.label('Created an intelligent chatbot using NLP techniques that can understand and respond to user queries with 85% accuracy.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card ai-example'):
#                                 ui.label('Image Classification').classes('font-bold mb-1')
#                                 ui.label('Developed a CNN model that classifies images into 10 categories with 92% accuracy using TensorFlow and Keras.').classes('text-sm')
            
#             # Card 2 - Machine Learning (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/ml/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Machine Learning').classes('text-2xl font-bold mb-2')
#                         ui.label('Developing predictive models and algorithms to extract insights from data. Experienced in various ML techniques and data preprocessing methods.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Data Analysis').classes('skill-tag ml-tag')
#                             ui.label('Predictive Modeling').classes('skill-tag ml-tag')
#                             ui.label('Algorithms').classes('skill-tag ml-tag')
                        
#                         # ML Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card ml-example'):
#                                 ui.label('Sales Prediction Model').classes('font-bold mb-1')
#                                 ui.label('Built a regression model to predict monthly sales based on historical data, achieving 94% accuracy and helping business planning.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card ml-example'):
#                                 ui.label('Customer Segmentation').classes('font-bold mb-1')
#                                 ui.label('Implemented K-means clustering to segment customers into 5 distinct groups based on purchasing behavior for targeted marketing.').classes('text-sm')
            
#             # Card 3 - Web Developer
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/webdev/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Web Developer').classes('text-2xl font-bold mb-2')
#                         ui.label('Creating responsive and user-friendly websites with modern technologies. Focused on clean code, performance optimization, and cross-browser compatibility.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('HTML/CSS').classes('skill-tag web-tag')
#                             ui.label('JavaScript').classes('skill-tag web-tag')
#                             ui.label('React').classes('skill-tag web-tag')
                        
#                         # Web Dev Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card web-example'):
#                                 ui.label('Portfolio Website').classes('font-bold mb-1')
#                                 ui.label('Designed and developed a responsive portfolio website with modern UI/UX, animations, and mobile-first design approach.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card web-example'):
#                                 ui.label('Blog Platform').classes('font-bold mb-1')
#                                 ui.label('Created a dynamic blog platform with content management system, user authentication, and SEO optimization features.').classes('text-sm')
            
#             # Card 4 - Web Applications (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/webapp/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Web Applications').classes('text-2xl font-bold mb-2')
#                         ui.label('Building interactive and dynamic web applications with robust backend systems. Experienced in full-stack development and database management.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Frontend').classes('skill-tag app-tag')
#                             ui.label('Backend').classes('skill-tag app-tag')
#                             ui.label('Database').classes('skill-tag app-tag')
                        
#                         # Web App Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card app-example'):
#                                 ui.label('Task Management App').classes('font-bold mb-1')
#                                 ui.label('Developed a full-stack task management application with real-time updates, drag-and-drop functionality, and team collaboration features.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card app-example'):
#                                 ui.label('E-commerce Platform').classes('font-bold mb-1')
#                                 ui.label('Built a complete e-commerce solution with product catalog, shopping cart, payment integration, and order management system.').classes('text-sm')
        
#         # Projects Section
#         with ui.column().classes('w-full mt-8').props('id="projects-section"'):
#             ui.label('My Projects').classes('text-3xl font-bold mb-6 text-center')
            
#             with ui.row().classes('w-full gap-6 justify-center'):
#                 # Project 1
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project1/400/250').classes('card-image w-full')
#                     ui.label('AI Image Recognition').classes('text-xl font-bold mt-4')
#                     ui.label('A machine learning model that identifies objects in images with high accuracy.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
                
#                 # Project 2
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project2/400/250').classes('card-image w-full')
#                     ui.label('E-commerce Website').classes('text-xl font-bold mt-4')
#                     ui.label('A full-featured online shopping platform with payment integration.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
                
#                 # Project 3
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project3/400/250').classes('card-image w-full')
#                     ui.label('Data Visualization Dashboard').classes('text-xl font-bold mt-4')
#                     ui.label('Interactive dashboard for visualizing complex datasets and trends.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
        
#         # Testimonials Section
#         with ui.column().classes('w-full mt-8').props('id="testimonials-section"'):
#             ui.label('What People Say').classes('text-3xl font-bold mb-6 text-center')
            
#             with ui.row().classes('w-full gap-6 justify-center'):
#                 # Testimonial 1
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person1/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Ahmed Khan').classes('font-bold')
#                             ui.label('Tech Startup CEO').classes('text-sm')
#                     ui.label('Abdullah is an incredibly talented developer. His AI solutions helped our startup optimize processes and save costs. Impressed by his skills at such a young age!').classes('text-sm italic')
                
#                 # Testimonial 2
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person2/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Sara Javed').classes('font-bold')
#                             ui.label('Project Manager').classes('text-sm')
#                     ui.label('Working with Abdullah was a pleasure. He delivered our web application ahead of schedule with exceptional quality. His technical knowledge is impressive.').classes('text-sm italic')
                
#                 # Testimonial 3
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person3/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Muhammad Ali').classes('font-bold')
#                             ui.label('Data Scientist').classes('text-sm')
#                     ui.label('Abdullah\'s machine learning models are top-notch. He has a deep understanding of algorithms and their practical applications. A rising star in the tech field!').classes('text-sm italic')
        
#         # Contact Section
#         with ui.column().classes('w-full mt-8').props('id="contact-section"'):
#             ui.label('Get In Touch').classes('text-3xl font-bold mb-6 text-center')
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Contact Information').classes('text-2xl font-bold mb-4')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('person', color='primary')
#                             ui.label('Abdullah Zia').classes('text-lg')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('phone', color='primary')
#                             ui.label('03132691012').classes('text-lg')
#                         with ui.row().classes('items-center gap-3'):
#                             ui.icon('email', color='primary')
#                             ui.label('@zia2691.com').classes('text-lg')
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Send a Message').classes('text-2xl font-bold mb-4')
#                         name_input = ui.input('Name').classes('w-full mb-3')
#                         email_input = ui.input('Email').classes('w-full mb-3')
#                         message_input = ui.textarea('Message').classes('w-full mb-3')
#                         ui.button('Send Message', on_click=lambda: handle_form_submit(name_input.value, email_input.value, message_input.value)).classes('btn-primary')
    
#     # Footer
#     with ui.footer().classes('footer w-full max-w-6xl mx-auto mt-8'):
#         with ui.column().classes('w-full items-center'):
#             ui.label('© 2023 Abdullah Zia - AI Enthusiast & Web Developer').classes('text-center')
#             with ui.row().classes('gap-4 mt-2'):
#                 ui.button('LinkedIn').classes('btn-primary')
#                 ui.button('GitHub').classes('btn-primary')
#                 ui.button('Twitter').classes('btn-primary')

# def handle_form_submit(name, email, message):
#     if name and email and message:
#         ui.notify(f'Thank you {name}! Your message has been sent.', color='positive')
#     else:
#         ui.notify('Please fill in all fields.', color='negative')

# ui.run()

##########################

# from nicegui import ui
# from nicegui.events import ValueChangeEventArguments
# # Define custom CSS for gradients and styling
# custom_css = """
# :root {
#   --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#   --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
#   --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
#   --success-gradient: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
#   --warning-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
#   --dark-gradient: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
#   --card-gradient: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
#   --text-color: #e0e0e0;
#   --card-bg: rgba(30, 30, 45, 0.7);
#   --pattern-bg: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
# }
# body {
#   background: var(--dark-gradient);
#   color: var(--text-color);
#   font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#   margin: 0;
#   padding: 0;
# }
# .hero-section {
#   background: var(--primary-gradient), var(--pattern-bg);
#   background-blend-mode: overlay;
#   border-radius: 15px;
#   padding: 3rem;
#   margin-bottom: 2rem;
#   box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
#   position: relative;
#   overflow: hidden;
# }
# .hero-section::before {
#   content: '';
#   position: absolute;
#   top: -50%;
#   right: -50%;
#   width: 200%;
#   height: 200%;
#   background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
#   z-index: 0;
# }
# .hero-content {
#   position: relative;
#   z-index: 1;
# }
# .profile-image {
#   border-radius: 50%;
#   border: 4px solid rgba(255, 255, 255, 0.3);
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
#   width: 200px;
#   height: 200px;
#   object-fit: cover;
# }
# .card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .card-image {
#   border-radius: 10px;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   width: 100%;
#   height: auto;
#   object-fit: cover;
# }
# .header, .footer {
#   background: rgba(30, 30, 45, 0.8);
#   backdrop-filter: blur(10px);
#   padding: 1rem;
#   border-radius: 10px;
#   margin-bottom: 1rem;
# }
# .header {
#   border-bottom: 1px solid rgba(255, 255, 255, 0.1);
# }
# .footer {
#   border-top: 1px solid rgba(255, 255, 255, 0.1);
#   margin-top: 2rem;
# }
# .rating {
#   color: #ffd700;
# }
# .btn-primary {
#   background: var(--primary-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-primary:hover {
#   transform: scale(1.05);
# }
# .skill-tag {
#   border-radius: 20px;
#   padding: 0.3rem 0.8rem;
#   margin: 0.2rem;
#   display: inline-block;
#   font-size: 0.9rem;
#   font-weight: 500;
# }
# .ai-tag {
#   background: var(--secondary-gradient);
# }
# .ml-tag {
#   background: var(--accent-gradient);
# }
# .web-tag {
#   background: var(--success-gradient);
# }
# .app-tag {
#   background: var(--warning-gradient);
# }
# .testimonial-card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .testimonial-card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .project-card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .project-card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .example-card {
#   background: rgba(255, 255, 255, 0.05);
#   border-radius: 10px;
#   padding: 1rem;
#   margin-top: 1rem;
#   border-left: 3px solid;
# }
# .ai-example {
#   border-left-color: #f093fb;
# }
# .ml-example {
#   border-left-color: #4facfe;
# }
# .web-example {
#   border-left-color: #43e97b;
# }
# .app-example {
#   border-left-color: #fa709a;
# }
# """
# @ui.page('/')
# def portfolio():
#     ui.add_head_html(f'<style>{custom_css}</style>')
    
#     # Header
#     with ui.header().classes('header w-full max-w-6xl mx-auto'):
#         with ui.row().classes('w-full justify-between items-center'):
#             with ui.column():
#                 ui.label('Abdullah Zia Portfolio').classes('text-2xl font-bold')
#             with ui.row().classes('gap-4'):
#                 ui.button('Home', on_click=lambda: ui.open('/')).classes('btn-primary')
#                 ui.button('Skills', on_click=lambda: ui.scroll_to('skills-section')).classes('btn-primary')
#                 ui.button('Projects', on_click=lambda: ui.scroll_to('projects-section')).classes('btn-primary')
#                 ui.button('Testimonials', on_click=lambda: ui.scroll_to('testimonials-section')).classes('btn-primary')
#                 ui.button('Contact', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary')
    
#     # Main content
#     with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
        
#         # Hero Section
#         with ui.column().classes('hero-section'):
#             with ui.row().classes('w-full justify-between items-center gap-8'):
#                 with ui.column().classes('hero-content w-full md:w-2/3'):
#                     ui.label('Abdullah Zia').classes('text-4xl md:text-5xl font-bold mb-2')
#                     ui.label('AI Enthusiast & Web Developer').classes('text-xl md:text-2xl mb-4')
#                     ui.label('F.A Graduate ').classes('text-lg mb-6')
#                     with ui.row().classes('gap-2 items-center mb-4'):
#                         ui.label('Client Rating:').classes('text-lg')
#                         for _ in range(5):
#                             ui.icon('star', color='gold').classes('rating')
#                         ui.label('(5/5)').classes('text-lg')
#                     ui.button('Contact Me', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary mt-2')
#                 with ui.column().classes('w-full md:w-1/3 flex justify-center'):
#                     # Updated: Using the local profile image
#                     ui.image('ab.zia.jpg').classes('profile-image')
        
#         # Skills Section
#         with ui.column().classes('w-full').props('id="skills-section"'):
#             ui.label('Skills & Expertise').classes('text-3xl font-bold mb-6 text-center')
            
#             # Card 1 - AI
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/ai/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Artificial Intelligence').classes('text-2xl font-bold mb-2')
#                         ui.label('Passionate about AI technologies and their applications in solving real-world problems. Continuously learning and exploring new AI frameworks and methodologies.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Machine Learning').classes('skill-tag ai-tag')
#                             ui.label('Neural Networks').classes('skill-tag ai-tag')
#                             ui.label('Deep Learning').classes('skill-tag ai-tag')
                        
#                         # AI Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card ai-example'):
#                                 ui.label('Chatbot Development').classes('font-bold mb-1')
#                                 ui.label('Created an intelligent chatbot using NLP techniques that can understand and respond to user queries with 85% accuracy.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card ai-example'):
#                                 ui.label('Image Classification').classes('font-bold mb-1')
#                                 ui.label('Developed a CNN model that classifies images into 10 categories with 92% accuracy using TensorFlow and Keras.').classes('text-sm')
            
#             # Card 2 - Machine Learning (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/ml/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Machine Learning').classes('text-2xl font-bold mb-2')
#                         ui.label('Developing predictive models and algorithms to extract insights from data. Experienced in various ML techniques and data preprocessing methods.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Data Analysis').classes('skill-tag ml-tag')
#                             ui.label('Predictive Modeling').classes('skill-tag ml-tag')
#                             ui.label('Algorithms').classes('skill-tag ml-tag')
                        
#                         # ML Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card ml-example'):
#                                 ui.label('Sales Prediction Model').classes('font-bold mb-1')
#                                 ui.label('Built a regression model to predict monthly sales based on historical data, achieving 94% accuracy and helping business planning.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card ml-example'):
#                                 ui.label('Customer Segmentation').classes('font-bold mb-1')
#                                 ui.label('Implemented K-means clustering to segment customers into 5 distinct groups based on purchasing behavior for targeted marketing.').classes('text-sm')
            
#             # Card 3 - Web Developer
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/webdev/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Web Developer').classes('text-2xl font-bold mb-2')
#                         ui.label('Creating responsive and user-friendly websites with modern technologies. Focused on clean code, performance optimization, and cross-browser compatibility.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('HTML/CSS').classes('skill-tag web-tag')
#                             ui.label('JavaScript').classes('skill-tag web-tag')
#                             ui.label('React').classes('skill-tag web-tag')
                        
#                         # Web Dev Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card web-example'):
#                                 ui.label('Portfolio Website').classes('font-bold mb-1')
#                                 ui.label('Designed and developed a responsive portfolio website with modern UI/UX, animations, and mobile-first design approach.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card web-example'):
#                                 ui.label('Blog Platform').classes('font-bold mb-1')
#                                 ui.label('Created a dynamic blog platform with content management system, user authentication, and SEO optimization features.').classes('text-sm')
            
#             # Card 4 - Web Applications (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/webapp/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Web Applications').classes('text-2xl font-bold mb-2')
#                         ui.label('Building interactive and dynamic web applications with robust backend systems. Experienced in full-stack development and database management.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Frontend').classes('skill-tag app-tag')
#                             ui.label('Backend').classes('skill-tag app-tag')
#                             ui.label('Database').classes('skill-tag app-tag')
                        
#                         # Web App Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card app-example'):
#                                 ui.label('Task Management App').classes('font-bold mb-1')
#                                 ui.label('Developed a full-stack task management application with real-time updates, drag-and-drop functionality, and team collaboration features.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card app-example'):
#                                 ui.label('E-commerce Platform').classes('font-bold mb-1')
#                                 ui.label('Built a complete e-commerce solution with product catalog, shopping cart, payment integration, and order management system.').classes('text-sm')
        
#         # Projects Section
#         with ui.column().classes('w-full mt-8').props('id="projects-section"'):
#             ui.label('My Projects').classes('text-3xl font-bold mb-6 text-center')
            
#             with ui.row().classes('w-full gap-6 justify-center'):
#                 # Project 1
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project1/400/250').classes('card-image w-full')
#                     ui.label('AI Image Recognition').classes('text-xl font-bold mt-4')
#                     ui.label('A machine learning model that identifies objects in images with high accuracy.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
                
#                 # Project 2
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project2/400/250').classes('card-image w-full')
#                     ui.label('E-commerce Website').classes('text-xl font-bold mt-4')
#                     ui.label('A full-featured online shopping platform with payment integration.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
                
#                 # Project 3
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project3/400/250').classes('card-image w-full')
#                     ui.label('Data Visualization Dashboard').classes('text-xl font-bold mt-4')
#                     ui.label('Interactive dashboard for visualizing complex datasets and trends.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
        
#         # Testimonials Section
#         with ui.column().classes('w-full mt-8').props('id="testimonials-section"'):
#             ui.label('What People Say').classes('text-3xl font-bold mb-6 text-center')
            
#             with ui.row().classes('w-full gap-6 justify-center'):
#                 # Testimonial 1
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person1/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Ahmed Khan').classes('font-bold')
#                             ui.label('Tech Startup CEO').classes('text-sm')
#                     ui.label('Abdullah is an incredibly talented developer. His AI solutions helped our startup optimize processes and save costs. Impressed by his skills at such a young age!').classes('text-sm italic')
                
#                 # Testimonial 2
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person2/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Sara Javed').classes('font-bold')
#                             ui.label('Project Manager').classes('text-sm')
#                     ui.label('Working with Abdullah was a pleasure. He delivered our web application ahead of schedule with exceptional quality. His technical knowledge is impressive.').classes('text-sm italic')
                
#                 # Testimonial 3
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person3/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Muhammad Ali').classes('font-bold')
#                             ui.label('Data Scientist').classes('text-sm')
#                     ui.label('Abdullah\'s machine learning models are top-notch. He has a deep understanding of algorithms and their practical applications. A rising star in the tech field!').classes('text-sm italic')
            
#             # Additional testimonials in a second row
#             with ui.row().classes('w-full gap-6 justify-center mt-6'):
#                 # Testimonial 4
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person4/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Fatima Ahmed').classes('font-bold')
#                             ui.label('Marketing Director').classes('text-sm')
#                     ui.label('Abdullah developed a data analysis tool for our marketing team that transformed how we understand customer behavior. His insights led to a 30% increase in campaign effectiveness.').classes('text-sm italic')
                
#                 # Testimonial 5
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person5/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Usman Malik').classes('font-bold')
#                             ui.label('CTO at TechInnovate').classes('text-sm')
#                     ui.label('I hired Abdullah for a complex AI project and was blown away by his problem-solving abilities. He not only delivered an excellent solution but also documented everything thoroughly. Highly recommended!').classes('text-sm italic')
                
#                 # Testimonial 6
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person6/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Ayesha Siddiqui').classes('font-bold')
#                             ui.label('UI/UX Designer').classes('text-sm')
#                     ui.label('As a designer, I\'ve worked with many developers, but Abdullah stands out for his attention to detail and commitment to bringing design visions to life. His frontend skills are exceptional!').classes('text-sm italic')
        
#         # Contact Section
#         with ui.column().classes('w-full mt-8').props('id="contact-section"'):
#             ui.label('Get In Touch').classes('text-3xl font-bold mb-6 text-center')
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Contact Information').classes('text-2xl font-bold mb-4')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('person', color='primary')
#                             ui.label('Abdullah Zia').classes('text-lg')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('phone', color='primary')
#                             ui.label('03132691012').classes('text-lg')
#                         with ui.row().classes('items-center gap-3'):
#                             ui.icon('email', color='primary')
#                             ui.label('@zia2691.com').classes('text-lg')
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Send a Message').classes('text-2xl font-bold mb-4')
#                         name_input = ui.input('Name').classes('w-full mb-3')
#                         email_input = ui.input('Email').classes('w-full mb-3')
#                         message_input = ui.textarea('Message').classes('w-full mb-3')
#                         ui.button('Send Message', on_click=lambda: handle_form_submit(name_input.value, email_input.value, message_input.value)).classes('btn-primary')
    
#     # Footer
#     with ui.footer().classes('footer w-full max-w-6xl mx-auto mt-8'):
#         with ui.column().classes('w-full items-center'):
#             ui.label('© 2023 Abdullah Zia - AI Enthusiast & Web Developer').classes('text-center')
#             with ui.row().classes('gap-4 mt-2'):
#                 ui.button('LinkedIn').classes('btn-primary')
#                 ui.button('GitHub').classes('btn-primary')
#                 ui.button('Twitter').classes('btn-primary')

# def handle_form_submit(name, email, message):
#     if name and email and message:
#         ui.notify(f'Thank you {name}! Your message has been sent.', color='positive')
#     else:
#         ui.notify('Please fill in all fields.', color='negative')

# ui.run()

##333333333############

# from nicegui import ui
# from nicegui.events import ValueChangeEventArguments
# # Define custom CSS for gradients and styling
# custom_css = """
# :root {
#   --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#   --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
#   --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
#   --success-gradient: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
#   --warning-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
#   --dark-gradient: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
#   --card-gradient: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
#   --text-color: #e0e0e0;
#   --card-bg: rgba(30, 30, 45, 0.7);
#   --pattern-bg: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
# }
# body {
#   background: var(--dark-gradient);
#   color: var(--text-color);
#   font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#   margin: 0;
#   padding: 0;
# }
# .hero-section {
#   background: var(--primary-gradient), var(--pattern-bg);
#   background-blend-mode: overlay;
#   border-radius: 15px;
#   padding: 3rem;
#   margin-bottom: 2rem;
#   box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
#   position: relative;
#   overflow: hidden;
# }
# .hero-section::before {
#   content: '';
#   position: absolute;
#   top: -50%;
#   right: -50%;
#   width: 200%;
#   height: 200%;
#   background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
#   z-index: 0;
# }
# .hero-content {
#   position: relative;
#   z-index: 1;
# }
# .profile-image {
#   border-radius: 50%;
#   border: 4px solid rgba(255, 255, 255, 0.3);
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
#   width: 200px;
#   height: 200px;
#   object-fit: cover;
# }
# .card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .card-image {
#   border-radius: 10px;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   width: 100%;
#   height: auto;
#   object-fit: cover;
# }
# .header, .footer {
#   background: rgba(30, 30, 45, 0.8);
#   backdrop-filter: blur(10px);
#   padding: 1rem;
#   border-radius: 10px;
#   margin-bottom: 1rem;
# }
# .header {
#   border-bottom: 1px solid rgba(255, 255, 255, 0.1);
# }
# .footer {
#   border-top: 1px solid rgba(255, 255, 255, 0.1);
#   margin-top: 2rem;
# }
# .rating {
#   color: #ffd700;
# }
# .btn-primary {
#   background: var(--primary-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-primary:hover {
#   transform: scale(1.05);
# }
# .skill-tag {
#   border-radius: 20px;
#   padding: 0.3rem 0.8rem;
#   margin: 0.2rem;
#   display: inline-block;
#   font-size: 0.9rem;
#   font-weight: 500;
# }
# .ai-tag {
#   background: var(--secondary-gradient);
# }
# .ml-tag {
#   background: var(--accent-gradient);
# }
# .web-tag {
#   background: var(--success-gradient);
# }
# .app-tag {
#   background: var(--warning-gradient);
# }
# .testimonial-card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .testimonial-card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .project-card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .project-card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .example-card {
#   background: rgba(255, 255, 255, 0.05);
#   border-radius: 10px;
#   padding: 1rem;
#   margin-top: 1rem;
#   border-left: 3px solid;
# }
# .ai-example {
#   border-left-color: #f093fb;
# }
# .ml-example {
#   border-left-color: #4facfe;
# }
# .web-example {
#   border-left-color: #43e97b;
# }
# .app-example {
#   border-left-color: #fa709a;
# }
# """
# @ui.page('/')
# def portfolio():
#     ui.add_head_html(f'<style>{custom_css}</style>')
    
#     # Header
#     with ui.header().classes('header w-full max-w-6xl mx-auto'):
#         with ui.row().classes('w-full justify-between items-center'):
#             with ui.column():
#                 ui.label('Abdullah Zia Portfolio').classes('text-2xl font-bold')
#             with ui.row().classes('gap-4'):
#                 ui.button('Home', on_click=lambda: ui.open('/')).classes('btn-primary')
#                 ui.button('Skills', on_click=lambda: ui.scroll_to('skills-section')).classes('btn-primary')
#                 ui.button('Projects', on_click=lambda: ui.scroll_to('projects-section')).classes('btn-primary')
#                 ui.button('Testimonials', on_click=lambda: ui.scroll_to('testimonials-section')).classes('btn-primary')
#                 ui.button('Contact', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary')
    
#     # Main content
#     with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
        
#         # Hero Section
#         with ui.column().classes('hero-section'):
#             with ui.row().classes('w-full justify-between items-center gap-8'):
#                 with ui.column().classes('hero-content w-full md:w-2/3'):
#                     ui.label('Abdullah Zia').classes('text-4xl md:text-5xl font-bold mb-2')
#                     ui.label('AI Enthusiast & Web Developer & Python Programmer').classes('text-xl md:text-2xl mb-4')
#                     ui.label('F.A Graduate ').classes('text-lg mb-6')
#                     with ui.row().classes('gap-2 items-center mb-4'):
#                         ui.label('Client Rating:').classes('text-lg')
#                         for _ in range(5):
#                             ui.icon('star', color='gold').classes('rating')
#                         ui.label('(5/5)').classes('text-lg')
#                     ui.button('Contact Me', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary mt-2')
#                 with ui.column().classes('w-full md:w-1/3 flex justify-center'):
#                     # Fixed: Using the static folder to serve the image
#                     ui.image('/static/ab.zia.jpg').classes('profile-image')
        
#         # Skills Section
#         with ui.column().classes('w-full').props('id="skills-section"'):
#             ui.label('Skills & Expertise').classes('text-3xl font-bold mb-6 text-center')
            
#             # Card 1 - AI
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/ai/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Artificial Intelligence').classes('text-2xl font-bold mb-2')
#                         ui.label('Passionate about AI technologies and their applications in solving real-world problems. Continuously learning and exploring new AI frameworks and methodologies.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Machine Learning').classes('skill-tag ai-tag')
#                             ui.label('Neural Networks').classes('skill-tag ai-tag')
#                             ui.label('Deep Learning').classes('skill-tag ai-tag')
                        
#                         # AI Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card ai-example'):
#                                 ui.label('Chatbot Development').classes('font-bold mb-1')
#                                 ui.label('Created an intelligent chatbot using NLP techniques that can understand and respond to user queries with 85% accuracy.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card ai-example'):
#                                 ui.label('Image Classification').classes('font-bold mb-1')
#                                 ui.label('Developed a CNN model that classifies images into 10 categories with 92% accuracy using TensorFlow and Keras.').classes('text-sm')
            
#             # Card 2 - Machine Learning (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/ml/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Machine Learning').classes('text-2xl font-bold mb-2')
#                         ui.label('Developing predictive models and algorithms to extract insights from data. Experienced in various ML techniques and data preprocessing methods.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Data Analysis').classes('skill-tag ml-tag')
#                             ui.label('Predictive Modeling').classes('skill-tag ml-tag')
#                             ui.label('Algorithms').classes('skill-tag ml-tag')
                        
#                         # ML Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card ml-example'):
#                                 ui.label('Sales Prediction Model').classes('font-bold mb-1')
#                                 ui.label('Built a regression model to predict monthly sales based on historical data, achieving 94% accuracy and helping business planning.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card ml-example'):
#                                 ui.label('Customer Segmentation').classes('font-bold mb-1')
#                                 ui.label('Implemented K-means clustering to segment customers into 5 distinct groups based on purchasing behavior for targeted marketing.').classes('text-sm')
            
#             # Card 3 - Web Developer
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/webdev/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Web Developer').classes('text-2xl font-bold mb-2')
#                         ui.label('Creating responsive and user-friendly websites with modern technologies. Focused on clean code, performance optimization, and cross-browser compatibility.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('HTML/CSS').classes('skill-tag web-tag')
#                             ui.label('JavaScript').classes('skill-tag web-tag')
#                             ui.label('React').classes('skill-tag web-tag')
                        
#                         # Web Dev Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card web-example'):
#                                 ui.label('Portfolio Website').classes('font-bold mb-1')
#                                 ui.label('Designed and developed a responsive portfolio website with modern UI/UX, animations, and mobile-first design approach.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card web-example'):
#                                 ui.label('Blog Platform').classes('font-bold mb-1')
#                                 ui.label('Created a dynamic blog platform with content management system, user authentication, and SEO optimization features.').classes('text-sm')
            
#             # Card 4 - Web Applications (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/webapp/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Web Applications').classes('text-2xl font-bold mb-2')
#                         ui.label('Building interactive and dynamic web applications with robust backend systems. Experienced in full-stack development and database management.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Frontend').classes('skill-tag app-tag')
#                             ui.label('Backend').classes('skill-tag app-tag')
#                             ui.label('Database').classes('skill-tag app-tag')
                        
#                         # Web App Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card app-example'):
#                                 ui.label('Task Management App').classes('font-bold mb-1')
#                                 ui.label('Developed a full-stack task management application with real-time updates, drag-and-drop functionality, and team collaboration features.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card app-example'):
#                                 ui.label('E-commerce Platform').classes('font-bold mb-1')
#                                 ui.label('Built a complete e-commerce solution with product catalog, shopping cart, payment integration, and order management system.').classes('text-sm')
        
#         # Projects Section
#         with ui.column().classes('w-full mt-8').props('id="projects-section"'):
#             ui.label('My Projects').classes('text-3xl font-bold mb-6 text-center')
            
#             with ui.row().classes('w-full gap-6 justify-center'):
#                 # Project 1
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project1/400/250').classes('card-image w-full')
#                     ui.label('AI Image Recognition').classes('text-xl font-bold mt-4')
#                     ui.label('A machine learning model that identifies objects in images with high accuracy.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
                
#                 # Project 2
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project2/400/250').classes('card-image w-full')
#                     ui.label('E-commerce Website').classes('text-xl font-bold mt-4')
#                     ui.label('A full-featured online shopping platform with payment integration.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
                
#                 # Project 3
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project3/400/250').classes('card-image w-full')
#                     ui.label('Data Visualization Dashboard').classes('text-xl font-bold mt-4')
#                     ui.label('Interactive dashboard for visualizing complex datasets and trends.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
        
#         # Testimonials Section
#         with ui.column().classes('w-full mt-8').props('id="testimonials-section"'):
#             ui.label('What People Say').classes('text-3xl font-bold mb-6 text-center')
            
#             with ui.row().classes('w-full gap-6 justify-center'):
#                 # Testimonial 1
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person1/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Ahmed Khan').classes('font-bold')
#                             ui.label('Tech Startup CEO').classes('text-sm')
#                     ui.label('Abdullah is an incredibly talented developer. His AI solutions helped our startup optimize processes and save costs. Impressed by his skills at such a young age!').classes('text-sm italic')
                
#                 # Testimonial 2
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person2/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Sara Javed').classes('font-bold')
#                             ui.label('Project Manager').classes('text-sm')
#                     ui.label('Working with Abdullah was a pleasure. He delivered our web application ahead of schedule with exceptional quality. His technical knowledge is impressive.').classes('text-sm italic')
                
#                 # Testimonial 3
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person3/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Muhammad Ali').classes('font-bold')
#                             ui.label('Data Scientist').classes('text-sm')
#                     ui.label('Abdullah\'s machine learning models are top-notch. He has a deep understanding of algorithms and their practical applications. A rising star in the tech field!').classes('text-sm italic')
            
#             # Additional testimonials in a second row
#             with ui.row().classes('w-full gap-6 justify-center mt-6'):
#                 # Testimonial 4
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person4/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Fatima Ahmed').classes('font-bold')
#                             ui.label('Marketing Director').classes('text-sm')
#                     ui.label('Abdullah developed a data analysis tool for our marketing team that transformed how we understand customer behavior. His insights led to a 30% increase in campaign effectiveness.').classes('text-sm italic')
                
#                 # Testimonial 5
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person5/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Usman Malik').classes('font-bold')
#                             ui.label('CTO at TechInnovate').classes('text-sm')
#                     ui.label('I hired Abdullah for a complex AI project and was blown away by his problem-solving abilities. He not only delivered an excellent solution but also documented everything thoroughly. Highly recommended!').classes('text-sm italic')
                
#                 # Testimonial 6
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person6/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Ayesha Siddiqui').classes('font-bold')
#                             ui.label('UI/UX Designer').classes('text-sm')
#                     ui.label('As a designer, I\'ve worked with many developers, but Abdullah stands out for his attention to detail and commitment to bringing design visions to life. His frontend skills are exceptional!').classes('text-sm italic')
        
#         # Contact Section
#         with ui.column().classes('w-full mt-8').props('id="contact-section"'):
#             ui.label('Get In Touch').classes('text-3xl font-bold mb-6 text-center')
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Contact Information').classes('text-2xl font-bold mb-4')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('person', color='primary')
#                             ui.label('Abdullah Zia').classes('text-lg')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('phone', color='primary')
#                             ui.label('03132691012').classes('text-lg')
#                         with ui.row().classes('items-center gap-3'):
#                             ui.icon('email', color='primary')
#                             ui.label('@zia2691.com').classes('text-lg')
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Send a Message').classes('text-2xl font-bold mb-4')
#                         name_input = ui.input('Name').classes('w-full mb-3')
#                         email_input = ui.input('Email').classes('w-full mb-3')
#                         message_input = ui.textarea('Message').classes('w-full mb-3')
#                         ui.button('Send Message', on_click=lambda: handle_form_submit(name_input.value, email_input.value, message_input.value)).classes('btn-primary')
    
#     # Footer
#     with ui.footer().classes('footer w-full max-w-6xl mx-auto mt-8'):
#         with ui.column().classes('w-full items-center'):
#             ui.label('© 2023 Abdullah Zia - AI Enthusiast & Web Developer').classes('text-center')
#             with ui.row().classes('gap-4 mt-2'):
#                 ui.button('LinkedIn').classes('btn-primary')
#                 ui.button('GitHub').classes('btn-primary')
#                 ui.button('Twitter').classes('btn-primary')

# def handle_form_submit(name, email, message):
#     if name and email and message:
#         ui.notify(f'Thank you {name}! Your message has been sent.', color='positive')
#     else:
#         ui.notify('Please fill in all fields.', color='negative')

# ui.run()

######33333333#3333###############33

# from nicegui import ui
# from nicegui.events import ValueChangeEventArguments
# # Define custom CSS for gradients and styling
# custom_css = """
# :root {
#   --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#   --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
#   --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
#   --success-gradient: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
#   --warning-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
#   --dark-gradient: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
#   --card-gradient: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
#   --text-color: #e0e0e0;
#   --card-bg: rgba(30, 30, 45, 0.7);
#   --pattern-bg: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
# }
# body {
#   background: var(--dark-gradient);
#   color: var(--text-color);
#   font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#   margin: 0;
#   padding: 0;
# }
# .hero-section {
#   background: var(--primary-gradient), var(--pattern-bg);
#   background-blend-mode: overlay;
#   border-radius: 15px;
#   padding: 3rem;
#   margin-bottom: 2rem;
#   box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
#   position: relative;
#   overflow: hidden;
# }
# .hero-section::before {
#   content: '';
#   position: absolute;
#   top: -50%;
#   right: -50%;
#   width: 200%;
#   height: 200%;
#   background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
#   z-index: 0;
# }
# .hero-content {
#   position: relative;
#   z-index: 1;
# }
# .profile-image {
#   border-radius: 50%;
#   border: 4px solid rgba(255, 255, 255, 0.3);
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
#   width: 200px;
#   height: 200px;
#   object-fit: cover;
# }
# .card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .card-image {
#   border-radius: 10px;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   width: 100%;
#   height: auto;
#   object-fit: cover;
# }
# .header, .footer {
#   background: rgba(30, 30, 45, 0.8);
#   backdrop-filter: blur(10px);
#   padding: 1rem;
#   border-radius: 10px;
#   margin-bottom: 1rem;
# }
# .header {
#   border-bottom: 1px solid rgba(255, 255, 255, 0.1);
# }
# .footer {
#   border-top: 1px solid rgba(255, 255, 255, 0.1);
#   margin-top: 2rem;
# }
# .rating {
#   color: #ffd700;
# }
# .btn-primary {
#   background: var(--primary-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-primary:hover {
#   transform: scale(1.05);
# }
# .skill-tag {
#   border-radius: 20px;
#   padding: 0.3rem 0.8rem;
#   margin: 0.2rem;
#   display: inline-block;
#   font-size: 0.9rem;
#   font-weight: 500;
# }
# .ai-tag {
#   background: var(--secondary-gradient);
# }
# .ml-tag {
#   background: var(--accent-gradient);
# }
# .web-tag {
#   background: var(--success-gradient);
# }
# .app-tag {
#   background: var(--warning-gradient);
# }
# .testimonial-card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .testimonial-card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .project-card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .project-card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .example-card {
#   background: rgba(255, 255, 255, 0.05);
#   border-radius: 10px;
#   padding: 1rem;
#   margin-top: 1rem;
#   border-left: 3px solid;
# }
# .ai-example {
#   border-left-color: #f093fb;
# }
# .ml-example {
#   border-left-color: #4facfe;
# }
# .web-example {
#   border-left-color: #43e97b;
# }
# .app-example {
#   border-left-color: #fa709a;
# }
# """
# @ui.page('/')
# def portfolio():
#     ui.add_head_html(f'<style>{custom_css}</style>')
    
#     # Header
#     with ui.header().classes('header w-full max-w-6xl mx-auto'):
#         with ui.row().classes('w-full justify-between items-center'):
#             with ui.column():
#                 ui.label('Abdullah Zia Portfolio').classes('text-2xl font-bold')
#             with ui.row().classes('gap-4'):
#                 ui.button('Home', on_click=lambda: ui.open('/')).classes('btn-primary')
#                 ui.button('Skills', on_click=lambda: ui.scroll_to('skills-section')).classes('btn-primary')
#                 ui.button('Projects', on_click=lambda: ui.scroll_to('projects-section')).classes('btn-primary')
#                 ui.button('Testimonials', on_click=lambda: ui.scroll_to('testimonials-section')).classes('btn-primary')
#                 ui.button('Contact', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary')
    
#     # Main content
#     with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
        
#         # Hero Section
#         with ui.column().classes('hero-section'):
#             with ui.row().classes('w-full justify-between items-center gap-8'):
#                 with ui.column().classes('hero-content w-full md:w-2/3'):
#                     ui.label('Abdullah Zia').classes('text-4xl md:text-5xl font-bold mb-2')
#                     ui.label('AI Enthusiast & Web Developer').classes('text-xl md:text-2xl mb-4')
#                     ui.label('F.A Graduate ').classes('text-lg mb-6')
#                     with ui.row().classes('gap-2 items-center mb-4'):
#                         ui.label('Client Rating:').classes('text-lg')
#                         for _ in range(5):
#                             ui.icon('star', color='gold').classes('rating')
#                         ui.label('(5/5)').classes('text-lg')
#                     ui.button('Contact Me', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-primary mt-2')
#                 with ui.column().classes('w-full md:w-1/3 flex justify-center'):
#                     # Updated: Using a beautiful galaxy image from NASA
#                     ui.image('https://apod.nasa.gov/apod/image/1801/M74_Hubble_960.jpg').classes('profile-image')
        
#         # Skills Section
#         with ui.column().classes('w-full').props('id="skills-section"'):
#             ui.label('Skills & Expertise').classes('text-3xl font-bold mb-6 text-center')
            
#             # Card 1 - AI
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/ai/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Artificial Intelligence').classes('text-2xl font-bold mb-2')
#                         ui.label('Passionate about AI technologies and their applications in solving real-world problems. Continuously learning and exploring new AI frameworks and methodologies.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Machine Learning').classes('skill-tag ai-tag')
#                             ui.label('Neural Networks').classes('skill-tag ai-tag')
#                             ui.label('Deep Learning').classes('skill-tag ai-tag')
                        
#                         # AI Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card ai-example'):
#                                 ui.label('Chatbot Development').classes('font-bold mb-1')
#                                 ui.label('Created an intelligent chatbot using NLP techniques that can understand and respond to user queries with 85% accuracy.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card ai-example'):
#                                 ui.label('Image Classification').classes('font-bold mb-1')
#                                 ui.label('Developed a CNN model that classifies images into 10 categories with 92% accuracy using TensorFlow and Keras.').classes('text-sm')
            
#             # Card 2 - Machine Learning (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/ml/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Machine Learning').classes('text-2xl font-bold mb-2')
#                         ui.label('Developing predictive models and algorithms to extract insights from data. Experienced in various ML techniques and data preprocessing methods.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Data Analysis').classes('skill-tag ml-tag')
#                             ui.label('Predictive Modeling').classes('skill-tag ml-tag')
#                             ui.label('Algorithms').classes('skill-tag ml-tag')
                        
#                         # ML Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card ml-example'):
#                                 ui.label('Sales Prediction Model').classes('font-bold mb-1')
#                                 ui.label('Built a regression model to predict monthly sales based on historical data, achieving 94% accuracy and helping business planning.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card ml-example'):
#                                 ui.label('Customer Segmentation').classes('font-bold mb-1')
#                                 ui.label('Implemented K-means clustering to segment customers into 5 distinct groups based on purchasing behavior for targeted marketing.').classes('text-sm')
            
#             # Card 3 - Web Developer
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/webdev/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Web Developer').classes('text-2xl font-bold mb-2')
#                         ui.label('Creating responsive and user-friendly websites with modern technologies. Focused on clean code, performance optimization, and cross-browser compatibility.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('HTML/CSS').classes('skill-tag web-tag')
#                             ui.label('JavaScript').classes('skill-tag web-tag')
#                             ui.label('React').classes('skill-tag web-tag')
                        
#                         # Web Dev Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card web-example'):
#                                 ui.label('Portfolio Website').classes('font-bold mb-1')
#                                 ui.label('Designed and developed a responsive portfolio website with modern UI/UX, animations, and mobile-first design approach.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card web-example'):
#                                 ui.label('Blog Platform').classes('font-bold mb-1')
#                                 ui.label('Created a dynamic blog platform with content management system, user authentication, and SEO optimization features.').classes('text-sm')
            
#             # Card 4 - Web Applications (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/webapp/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Web Applications').classes('text-2xl font-bold mb-2')
#                         ui.label('Building interactive and dynamic web applications with robust backend systems. Experienced in full-stack development and database management.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Frontend').classes('skill-tag app-tag')
#                             ui.label('Backend').classes('skill-tag app-tag')
#                             ui.label('Database').classes('skill-tag app-tag')
                        
#                         # Web App Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card app-example'):
#                                 ui.label('Task Management App').classes('font-bold mb-1')
#                                 ui.label('Developed a full-stack task management application with real-time updates, drag-and-drop functionality, and team collaboration features.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card app-example'):
#                                 ui.label('E-commerce Platform').classes('font-bold mb-1')
#                                 ui.label('Built a complete e-commerce solution with product catalog, shopping cart, payment integration, and order management system.').classes('text-sm')
        
#         # Projects Section
#         with ui.column().classes('w-full mt-8').props('id="projects-section"'):
#             ui.label('My Projects').classes('text-3xl font-bold mb-6 text-center')
            
#             with ui.row().classes('w-full gap-6 justify-center'):
#                 # Project 1
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project1/400/250').classes('card-image w-full')
#                     ui.label('AI Image Recognition').classes('text-xl font-bold mt-4')
#                     ui.label('A machine learning model that identifies objects in images with high accuracy.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
                
#                 # Project 2
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project2/400/250').classes('card-image w-full')
#                     ui.label('E-commerce Website').classes('text-xl font-bold mt-4')
#                     ui.label('A full-featured online shopping platform with payment integration.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
                
#                 # Project 3
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project3/400/250').classes('card-image w-full')
#                     ui.label('Data Visualization Dashboard').classes('text-xl font-bold mt-4')
#                     ui.label('Interactive dashboard for visualizing complex datasets and trends.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-primary mt-3')
        
#         # Testimonials Section
#         with ui.column().classes('w-full mt-8').props('id="testimonials-section"'):
#             ui.label('What People Say').classes('text-3xl font-bold mb-6 text-center')
            
#             with ui.row().classes('w-full gap-6 justify-center'):
#                 # Testimonial 1
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person1/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Ahmed Khan').classes('font-bold')
#                             ui.label('Tech Startup CEO').classes('text-sm')
#                     ui.label('Abdullah is an incredibly talented developer. His AI solutions helped our startup optimize processes and save costs. Impressed by his skills at such a young age!').classes('text-sm italic')
                
#                 # Testimonial 2
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person2/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Sara Javed').classes('font-bold')
#                             ui.label('Project Manager').classes('text-sm')
#                     ui.label('Working with Abdullah was a pleasure. He delivered our web application ahead of schedule with exceptional quality. His technical knowledge is impressive.').classes('text-sm italic')
                
#                 # Testimonial 3
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person3/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Muhammad Ali').classes('font-bold')
#                             ui.label('Data Scientist').classes('text-sm')
#                     ui.label('Abdullah\'s machine learning models are top-notch. He has a deep understanding of algorithms and their practical applications. A rising star in the tech field!').classes('text-sm italic')
            
#             # Additional testimonials in a second row
#             with ui.row().classes('w-full gap-6 justify-center mt-6'):
#                 # Testimonial 4
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person4/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Fatima Ahmed').classes('font-bold')
#                             ui.label('Marketing Director').classes('text-sm')
#                     ui.label('Abdullah developed a data analysis tool for our marketing team that transformed how we understand customer behavior. His insights led to a 30% increase in campaign effectiveness.').classes('text-sm italic')
                
#                 # Testimonial 5
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person5/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Usman Malik').classes('font-bold')
#                             ui.label('CTO at TechInnovate').classes('text-sm')
#                     ui.label('I hired Abdullah for a complex AI project and was blown away by his problem-solving abilities. He not only delivered an excellent solution but also documented everything thoroughly. Highly recommended!').classes('text-sm italic')
                
#                 # Testimonial 6
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person6/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Ayesha Siddiqui').classes('font-bold')
#                             ui.label('UI/UX Designer').classes('text-sm')
#                     ui.label('As a designer, I\'ve worked with many developers, but Abdullah stands out for his attention to detail and commitment to bringing design visions to life. His frontend skills are exceptional!').classes('text-sm italic')
        
#         # Contact Section
#         with ui.column().classes('w-full mt-8').props('id="contact-section"'):
#             ui.label('Get In Touch').classes('text-3xl font-bold mb-6 text-center')
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Contact Information').classes('text-2xl font-bold mb-4')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('person', color='primary')
#                             ui.label('Abdullah Zia').classes('text-lg')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('phone', color='primary')
#                             ui.label('03132691012').classes('text-lg')
#                         with ui.row().classes('items-center gap-3'):
#                             ui.icon('email', color='primary')
#                             ui.label('@zia2691.com').classes('text-lg')
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Send a Message').classes('text-2xl font-bold mb-4')
#                         name_input = ui.input('Name').classes('w-full mb-3')
#                         email_input = ui.input('Email').classes('w-full mb-3')
#                         message_input = ui.textarea('Message').classes('w-full mb-3')
#                         ui.button('Send Message', on_click=lambda: handle_form_submit(name_input.value, email_input.value, message_input.value)).classes('btn-primary')
    
#     # Footer
#     with ui.footer().classes('footer w-full max-w-6xl mx-auto mt-8'):
#         with ui.column().classes('w-full items-center'):
#             ui.label('© 2023 Abdullah Zia - AI Enthusiast & Web Developer').classes('text-center')
#             with ui.row().classes('gap-4 mt-2'):
#                 ui.button('LinkedIn').classes('btn-primary')
#                 ui.button('GitHub').classes('btn-primary')
#                 ui.button('Twitter').classes('btn-primary')

# def handle_form_submit(name, email, message):
#     if name and email and message:
#         ui.notify(f'Thank you {name}! Your message has been sent.', color='positive')
#     else:
#         ui.notify('Please fill in all fields.', color='negative')

# ui.run()

# #####################################

# from nicegui import ui
# from nicegui.events import ValueChangeEventArguments
# # Define custom CSS for gradients and styling with more colors
# custom_css = """
# :root {
#   --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#   --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
#   --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
#   --success-gradient: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
#   --warning-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
#   --info-gradient: linear-gradient(135deg, #30cfd0 0%, #330867 100%);
#   --purple-gradient: linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%);
#   --orange-gradient: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
#   --teal-gradient: linear-gradient(135deg, #0ba360 0%, #3cba92 100%);
#   --dark-gradient: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
#   --card-gradient: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
#   --text-color: #e0e0e0;
#   --card-bg: rgba(30, 30, 45, 0.7);
#   --pattern-bg: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
# }
# body {
#   background: var(--dark-gradient);
#   color: var(--text-color);
#   font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#   margin: 0;
#   padding: 0;
# }
# .hero-section {
#   background: var(--primary-gradient), var(--pattern-bg);
#   background-blend-mode: overlay;
#   border-radius: 15px;
#   padding: 3rem;
#   margin-bottom: 2rem;
#   box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
#   position: relative;
#   overflow: hidden;
# }
# .hero-section::before {
#   content: '';
#   position: absolute;
#   top: -50%;
#   right: -50%;
#   width: 200%;
#   height: 200%;
#   background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
#   z-index: 0;
# }
# .hero-content {
#   position: relative;
#   z-index: 1;
# }
# .profile-image {
#   border-radius: 50%;
#   border: 4px solid rgba(255, 255, 255, 0.3);
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
#   width: 200px;
#   height: 200px;
#   object-fit: cover;
# }
# .card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .card-image {
#   border-radius: 10px;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   width: 100%;
#   height: auto;
#   object-fit: cover;
# }
# .header, .footer {
#   background: rgba(30, 30, 45, 0.8);
#   backdrop-filter: blur(10px);
#   padding: 1rem;
#   border-radius: 10px;
#   margin-bottom: 1rem;
# }
# .header {
#   border-bottom: 1px solid rgba(255, 255, 255, 0.1);
# }
# .footer {
#   border-top: 1px solid rgba(255, 255, 255, 0.1);
#   margin-top: 2rem;
# }
# .rating {
#   color: #ffd700;
# }
# .btn-primary {
#   background: var(--primary-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-primary:hover {
#   transform: scale(1.05);
# }
# .btn-secondary {
#   background: var(--secondary-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-secondary:hover {
#   transform: scale(1.05);
# }
# .btn-accent {
#   background: var(--accent-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-accent:hover {
#   transform: scale(1.05);
# }
# .btn-success {
#   background: var(--success-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-success:hover {
#   transform: scale(1.05);
# }
# .btn-warning {
#   background: var(--warning-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-warning:hover {
#   transform: scale(1.05);
# }
# .btn-info {
#   background: var(--info-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-info:hover {
#   transform: scale(1.05);
# }
# .btn-purple {
#   background: var(--purple-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-purple:hover {
#   transform: scale(1.05);
# }
# .btn-orange {
#   background: var(--orange-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-orange:hover {
#   transform: scale(1.05);
# }
# .btn-teal {
#   background: var(--teal-gradient);
#   border: none;
#   border-radius: 8px;
#   padding: 0.5rem 1.5rem;
#   color: white;
#   font-weight: bold;
#   cursor: pointer;
#   transition: transform 0.2s ease;
# }
# .btn-teal:hover {
#   transform: scale(1.05);
# }
# .skill-tag {
#   border-radius: 20px;
#   padding: 0.3rem 0.8rem;
#   margin: 0.2rem;
#   display: inline-block;
#   font-size: 0.9rem;
#   font-weight: 500;
# }
# .ai-tag {
#   background: var(--secondary-gradient);
# }
# .ml-tag {
#   background: var(--accent-gradient);
# }
# .web-tag {
#   background: var(--success-gradient);
# }
# .app-tag {
#   background: var(--warning-gradient);
# }
# .testimonial-card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .testimonial-card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .project-card {
#   background: var(--card-gradient), var(--card-bg);
#   border-radius: 15px;
#   padding: 1.5rem;
#   margin-bottom: 1.5rem;
#   box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
#   backdrop-filter: blur(10px);
#   border: 1px solid rgba(255, 255, 255, 0.1);
#   transition: transform 0.3s ease, box-shadow 0.3s ease;
# }
# .project-card:hover {
#   transform: translateY(-5px);
#   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
# }
# .example-card {
#   background: rgba(255, 255, 255, 0.05);
#   border-radius: 10px;
#   padding: 1rem;
#   margin-top: 1rem;
#   border-left: 3px solid;
# }
# .ai-example {
#   border-left-color: #f093fb;
# }
# .ml-example {
#   border-left-color: #4facfe;
# }
# .web-example {
#   border-left-color: #43e97b;
# }
# .app-example {
#   border-left-color: #fa709a;
# }
# .section-title {
#   background: var(--info-gradient);
#   -webkit-background-clip: text;
#   background-clip: text;
#   color: transparent;
#   text-shadow: 0 2px 4px rgba(0,0,0,0.2);
# }
# """

# from PIL import Image
# import base64
# import io
# image = Image.open('porfolio\ab.zia.jpg')
# buffer = io.BytesIO()
# image.save(buffer, 'jpg')
# image = buffer.getbuffer()
# image = base64.b64encode(image)
# @ui.page('/')
# def portfolio():
#     ui.add_head_html(f'<style>{custom_css}</style>')
    
#     # Header
#     with ui.header().classes('header w-full max-w-6xl mx-auto'):
#         with ui.row().classes('w-full justify-between items-center'):
#             with ui.column():
#                 ui.label('Abdullah Zia Portfolio').classes('text-2xl font-bold')
#             with ui.row().classes('gap-4'):
#                 ui.button('Home', on_click=lambda: ui.open('/')).classes('btn-primary')
#                 ui.button('Skills', on_click=lambda: ui.scroll_to('skills-section')).classes('btn-secondary')
#                 ui.button('Projects', on_click=lambda: ui.scroll_to('projects-section')).classes('btn-accent')
#                 ui.button('Testimonials', on_click=lambda: ui.scroll_to('testimonials-section')).classes('btn-success')
#                 ui.button('Contact', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-warning')
    
#     # Main content
#     with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
        
#         # Hero Section
#         with ui.column().classes('hero-section'):
#             with ui.row().classes('w-full justify-between items-center gap-8'):
#                 with ui.column().classes('hero-content w-full md:w-2/3'):
#                     ui.label('Abdullah Zia').classes('text-4xl md:text-5xl font-bold mb-2')
#                     ui.label('AI Enthusiast & Web Developer & python programmer').classes('text-xl md:text-2xl mb-4')
#                     ui.label('F.A Graduate ').classes('text-lg mb-6')
#                     with ui.row().classes('gap-2 items-center mb-4'):
#                         ui.label('Client Rating:').classes('text-lg')
#                         for _ in range(5):
#                             ui.icon('star', color='gold').classes('rating')
#                         ui.label('(5/5)').classes('text-lg')
#                     ui.button('Contact Me', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-info mt-2')
#                 with ui.column().classes('w-full md:w-1/3 flex justify-center'):
#                     # Fixed: Using a reliable galaxy image from Picsum
#                     ui.image('./ab.zia.jpg').classes('profile-image')
        
#         # Skills Section
#         with ui.column().classes('w-full').props('id="skills-section"'):
#             ui.label('Skills & Expertise').classes('text-3xl font-bold mb-6 text-center section-title')
            
#             # Card 1 - AI
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/ai/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Artificial Intelligence').classes('text-2xl font-bold mb-2')
#                         ui.label('Passionate about AI technologies and their applications in solving real-world problems. Continuously learning and exploring new AI frameworks and methodologies.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Machine Learning').classes('skill-tag ai-tag')
#                             ui.label('Neural Networks').classes('skill-tag ai-tag')
#                             ui.label('Deep Learning').classes('skill-tag ai-tag')
                        
#                         # AI Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card ai-example'):
#                                 ui.label('Chatbot Development').classes('font-bold mb-1')
#                                 ui.label('Created an intelligent chatbot using NLP techniques that can understand and respond to user queries with 85% accuracy.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card ai-example'):
#                                 ui.label('Image Classification').classes('font-bold mb-1')
#                                 ui.label('Developed a CNN model that classifies images into 10 categories with 92% accuracy using TensorFlow and Keras.').classes('text-sm')
            
#             # Card 2 - Machine Learning (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/ml/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Machine Learning').classes('text-2xl font-bold mb-2')
#                         ui.label('Developing predictive models and algorithms to extract insights from data. Experienced in various ML techniques and data preprocessing methods.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Data Analysis').classes('skill-tag ml-tag')
#                             ui.label('Predictive Modeling').classes('skill-tag ml-tag')
#                             ui.label('Algorithms').classes('skill-tag ml-tag')
                        
#                         # ML Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card ml-example'):
#                                 ui.label('Sales Prediction Model').classes('font-bold mb-1')
#                                 ui.label('Built a regression model to predict monthly sales based on historical data, achieving 94% accuracy and helping business planning.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card ml-example'):
#                                 ui.label('Customer Segmentation').classes('font-bold mb-1')
#                                 ui.label('Implemented K-means clustering to segment customers into 5 distinct groups based on purchasing behavior for targeted marketing.').classes('text-sm')
            
#             # Card 3 - Web Developer
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/webdev/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Web Developer').classes('text-2xl font-bold mb-2')
#                         ui.label('Creating responsive and user-friendly websites with modern technologies. Focused on clean code, performance optimization, and cross-browser compatibility.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('HTML/CSS').classes('skill-tag web-tag')
#                             ui.label('JavaScript').classes('skill-tag web-tag')
#                             ui.label('React').classes('skill-tag web-tag')
                        
#                         # Web Dev Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card web-example'):
#                                 ui.label('Portfolio Website').classes('font-bold mb-1')
#                                 ui.label('Designed and developed a responsive portfolio website with modern UI/UX, animations, and mobile-first design approach.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card web-example'):
#                                 ui.label('Blog Platform').classes('font-bold mb-1')
#                                 ui.label('Created a dynamic blog platform with content management system, user authentication, and SEO optimization features.').classes('text-sm')
            
#             # Card 4 - Web Applications (Image on right)
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
#                     with ui.column().classes('w-full md:w-1/3'):
#                         ui.image('https://picsum.photos/seed/webapp/400/300').classes('card-image')
#                     with ui.column().classes('w-full md:w-2/3'):
#                         ui.label('Web Applications').classes('text-2xl font-bold mb-2')
#                         ui.label('Building interactive and dynamic web applications with robust backend systems. Experienced in full-stack development and database management.').classes('text-lg')
#                         with ui.row().classes('flex-wrap mt-2'):
#                             ui.label('Frontend').classes('skill-tag app-tag')
#                             ui.label('Backend').classes('skill-tag app-tag')
#                             ui.label('Database').classes('skill-tag app-tag')
                        
#                         # Web App Examples
#                         with ui.column().classes('w-full mt-4'):
#                             ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
#                             # Example 1
#                             with ui.card().classes('example-card app-example'):
#                                 ui.label('Task Management App').classes('font-bold mb-1')
#                                 ui.label('Developed a full-stack task management application with real-time updates, drag-and-drop functionality, and team collaboration features.').classes('text-sm')
                            
#                             # Example 2
#                             with ui.card().classes('example-card app-example'):
#                                 ui.label('E-commerce Platform').classes('font-bold mb-1')
#                                 ui.label('Built a complete e-commerce solution with product catalog, shopping cart, payment integration, and order management system.').classes('text-sm')
        
#         # Projects Section
#         with ui.column().classes('w-full mt-8').props('id="projects-section"'):
#             ui.label('My Projects').classes('text-3xl font-bold mb-6 text-center section-title')
            
#             with ui.row().classes('w-full gap-6 justify-center'):
#                 # Project 1
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project1/400/250').classes('card-image w-full')
#                     ui.label('AI Image Recognition').classes('text-xl font-bold mt-4')
#                     ui.label('A machine learning model that identifies objects in images with high accuracy.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-purple mt-3')
                
#                 # Project 2
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project2/400/250').classes('card-image w-full')
#                     ui.label('E-commerce Website').classes('text-xl font-bold mt-4')
#                     ui.label('A full-featured online shopping platform with payment integration.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-orange mt-3')
                
#                 # Project 3
#                 with ui.card().classes('project-card w-full md:w-1/3'):
#                     ui.image('https://picsum.photos/seed/project3/400/250').classes('card-image w-full')
#                     ui.label('Data Visualization Dashboard').classes('text-xl font-bold mt-4')
#                     ui.label('Interactive dashboard for visualizing complex datasets and trends.').classes('text-sm mt-2')
#                     ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-teal mt-3')
        
#         # Testimonials Section
#         with ui.column().classes('w-full mt-8').props('id="testimonials-section"'):
#             ui.label('What People Say').classes('text-3xl font-bold mb-6 text-center section-title')
            
#             with ui.row().classes('w-full gap-6 justify-center'):
#                 # Testimonial 1
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person1/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Ahmed Khan').classes('font-bold')
#                             ui.label('Tech Startup CEO').classes('text-sm')
#                     ui.label('Abdullah is an incredibly talented developer. His AI solutions helped our startup optimize processes and save costs. Impressed by his skills at such a young age!').classes('text-sm italic')
                
#                 # Testimonial 2
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person2/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Sara Javed').classes('font-bold')
#                             ui.label('Project Manager').classes('text-sm')
#                     ui.label('Working with Abdullah was a pleasure. He delivered our web application ahead of schedule with exceptional quality. His technical knowledge is impressive.').classes('text-sm italic')
                
#                 # Testimonial 3
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person3/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Muhammad Ali').classes('font-bold')
#                             ui.label('Data Scientist').classes('text-sm')
#                     ui.label('Abdullah\'s machine learning models are top-notch. He has a deep understanding of algorithms and their practical applications. A rising star in the tech field!').classes('text-sm italic')
            
#             # Additional testimonials in a second row
#             with ui.row().classes('w-full gap-6 justify-center mt-6'):
#                 # Testimonial 4
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person4/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Fatima Ahmed').classes('font-bold')
#                             ui.label('Marketing Director').classes('text-sm')
#                     ui.label('Abdullah developed a data analysis tool for our marketing team that transformed how we understand customer behavior. His insights led to a 30% increase in campaign effectiveness.').classes('text-sm italic')
                
#                 # Testimonial 5
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person5/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Usman Malik').classes('font-bold')
#                             ui.label('CTO at TechInnovate').classes('text-sm')
#                     ui.label('I hired Abdullah for a complex AI project and was blown away by his problem-solving abilities. He not only delivered an excellent solution but also documented everything thoroughly. Highly recommended!').classes('text-sm italic')
                
#                 # Testimonial 6
#                 with ui.card().classes('testimonial-card w-full md:w-1/3'):
#                     with ui.row().classes('items-center mb-3'):
#                         ui.image('https://picsum.photos/seed/person6/60/60').classes('rounded-full w-12 h-12 object-cover')
#                         with ui.column().classes('ml-3'):
#                             ui.label('Ayesha Siddiqui').classes('font-bold')
#                             ui.label('UI/UX Designer').classes('text-sm')
#                     ui.label('As a designer, I\'ve worked with many developers, but Abdullah stands out for his attention to detail and commitment to bringing design visions to life. His frontend skills are exceptional!').classes('text-sm italic')
        
#         # Contact Section
#         with ui.column().classes('w-full mt-8').props('id="contact-section"'):
#             ui.label('Get In Touch').classes('text-3xl font-bold mb-6 text-center section-title')
#             with ui.card().classes('card w-full'):
#                 with ui.row().classes('w-full gap-6 items-center'):
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Contact Information').classes('text-2xl font-bold mb-4')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('person', color='primary')
#                             ui.label('Abdullah Zia').classes('text-lg')
#                         with ui.row().classes('items-center gap-3 mb-3'):
#                             ui.icon('phone', color='primary')
#                             ui.label('03132691012').classes('text-lg')
#                         with ui.row().classes('items-center gap-3'):
#                             ui.icon('email', color='primary')
#                             ui.label('@zia2691.com').classes('text-lg')
#                     with ui.column().classes('w-full md:w-1/2'):
#                         ui.label('Send a Message').classes('text-2xl font-bold mb-4')
#                         name_input = ui.input('Name').classes('w-full mb-3')
#                         email_input = ui.input('Email').classes('w-full mb-3')
#                         message_input = ui.textarea('Message').classes('w-full mb-3')
#                         ui.button('Send Message', on_click=lambda: handle_form_submit(name_input.value, email_input.value, message_input.value)).classes('btn-info')
    
#     # Footer
#     with ui.footer().classes('footer w-full max-w-6xl mx-auto mt-8'):
#         with ui.column().classes('w-full items-center'):
#             ui.label('© 2023 Abdullah Zia - AI Enthusiast & Web Developer').classes('text-center')
#             with ui.row().classes('gap-4 mt-2'):
#                 ui.button('LinkedIn', on_click=lambda: ui.open('https://linkedin.com')).classes('btn-primary')
#                 ui.button('GitHub', on_click=lambda: ui.open('https://github.com')).classes('btn-secondary')
#                 ui.button('Twitter', on_click=lambda: ui.open('https://twitter.com')).classes('btn-accent')

# def handle_form_submit(name, email, message):
#     if name and email and message:
#         ui.notify(f'Thank you {name}! Your message has been sent.', color='positive')
#     else:
#         ui.notify('Please fill in all fields.', color='negative')

# ui.run()

####################
######################
####################

from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from PIL import Image
import base64
import io

# Function to convert image to data URL
def get_image_data_url(image_path):
    try:
        # Open the image
        image = Image.open(image_path)
        
        # Create a BytesIO buffer
        buffer = io.BytesIO()
        
        # Save the image to the buffer in JPEG format
        image.save(buffer, format='JPEG')
        
        # Get the byte value from the buffer
        image_bytes = buffer.getvalue()
        
        # Encode the bytes to base64
        base64_bytes = base64.b64encode(image_bytes)
        
        # Convert base64 bytes to string for HTML use
        base64_string = base64_bytes.decode('ascii')
        
        # Create the data URL for HTML
        return f"data:image/jpeg;base64,{base64_string}"
    
    except Exception as e:
        print(f"Error loading image: {e}")
        # Fallback to a placeholder image
        return "https://picsum.photos/seed/galaxy/400/400"

# Define custom CSS for gradients and styling
custom_css = """
:root {
  --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  --success-gradient: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  --warning-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
  --info-gradient: linear-gradient(135deg, #30cfd0 0%, #330867 100%);
  --purple-gradient: linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%);
  --orange-gradient: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
  --teal-gradient: linear-gradient(135deg, #0ba360 0%, #3cba92 100%);
  --dark-gradient: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
  --card-gradient: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
}
 --text-color: #e0e0e0;
  --card-bg: rgba(30, 30, 45, 0.7);
  --pattern-bg: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
body {
  background: var(--dark-gradient);
  color: var(--text-color);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
}
.hero-section {
  background: var(--primary-gradient), var(--pattern-bg);
  background-blend-mode: overlay;
  border-radius: 15px;
  padding: 3rem;
  margin-bottom: 2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
);
  position: relative;
  overflow: hidden;
}
.hero-section::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
  z-index: 0;
}
.hero-content {
  position: relative;
  z-index: 1;
}
.profile-image {
  border-radius: 50%;
  border: 4px solid rgba(255, 255, 255,0.3);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  width: 200px;
  height: 200px;
  object-fit: cover;
}
.card {
  background: var(--card-gradient), var(--card-bg);
  border-radius: 15px;
 padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}
.card-image {
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  width: 100%;
  height: auto;
  object-fit: cover;
}
.header, .footer {
  background: rgba(30, 30, 45, 0.8);
  backdrop-filter: blur(10px);
  padding: 1rem;
  border-radius: 10px;
  margin-bottom: 1rem;
}
.header {
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
.footer {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  margin-top: 2rem;
}
.rating {
  color: #ffd700;
}
.btn-primary {
  background: var(--primary-gradient);
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1.5rem;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.btn-primary:hover {
  transform: scale(1.05);
}
.btn-secondary {
  background: var(--secondary-gradient);
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1.5rem;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.btn-secondary:hover {
  transform: scale(1.05);
}
.btn-accent {
  background: var(--accent-gradient);
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1.5rem;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.btn-accent:hover {
  transform: scale(1.05);
}
.btn-success {
  background: var(--success-gradient);
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1.5rem;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.btn-success:hover {
  transform: scale(1.05);
}
.btn-warning {
  background: var(--warning-gradient);
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1.5rem;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.btn-warning:hover {
  transform: scale(1.05);
}
.btn-info {
  background: var(--info-gradient);
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1.5rem;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.btn-info:hover {
  transform: scale(1.05);
}
.btn-purple {
  background: var(--purple-gradient);
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1.5rem;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.btn-purple:hover {
  transform: scale(1.05);
}
.btn-orange {
  background: var(--orange-gradient);
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1.5rem;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.btn-orange:hover {
  transform: scale(1.05);
}
.btn-teal {
  background: var(--teal-gradient);
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1.5rem;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.btn-teal:hover {
  transform: scale(1.05);
}
.skill-tag {
  border-radius: 20px;
  padding: 0.3rem 0.8rem;
  margin: 0.2rem;
  display: inline-block;
  font-size: 0.9rem;
  font-weight: 500;
}
.ai-tag {
  background: var(--secondary-gradient);
}
.ml-tag {
  background: var(--accent-gradient);
}
.web-tag {
  background: var(--success-gradient);
}
.app-tag {
  background: var(--warning-gradient);
}
.testimonial-card {
  background: var(--card-gradient), var(--card-bg);
  border-radius: 15px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.testimonial-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}
.project-card {
  background: var(--card-gradient), var(--card-bg);
  border-radius: 15px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}
.example-card {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
  padding: 1rem;
  margin-top: 1rem;
  border-left: 3px solid;
}
.ai-example {
  border-left-color: #f093fb;
}
.ml-example {
  border-left-color: #4facfe;
}
.web-example {
  border-left-color: #43e97b;
}
.app-example {
  border-left-color: #fa709a;
}
.section-title {
  background: var(--info-gradient);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  text-shadow: 0 2px 4px rgba(0,0,0,0.2);
}
"""
@ui.page('/')
def portfolio():
    ui.add_head_html(f'<style>{custom_css}</style>')
    
    # Get the profile image as data URL
    profile_image_url = get_image_data_url('portfolio/ab.zia.jpg')
    
    # Header
    with ui.header().classes('header w-full max-w-6xl mx-auto'):
        with ui.row().classes('w-full justify-between items-center'):
            with ui.column():
                ui.label('Abdullah Zia Portfolio').classes('text-2xl font-bold')
            with ui.row().classes('gap-4'):
                ui.button('Home', on_click=lambda: ui.open('/')).classes('btn-primary')
                ui.button('Skills', on_click=lambda: ui.scroll_to('skills-section')).classes('btn-secondary')
                ui.button('Projects', on_click=lambda: ui.scroll_to('projects-section')).classes('btn-accent')
                ui.button('Testimonials', on_click=lambda: ui.scroll_to('testimonials-section')).classes('btn-success')
                ui.button('Contact', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-warning')
    
    # Main content
    with ui.column().classes('w-full max-w-6xl mx-auto p-4'):
        
        # Hero Section
        with ui.column().classes('hero-section'):
            with ui.row().classes('w-full justify-between items-center gap-8'):
                with ui.column().classes('hero-content w-full md:w-2/3'):
                    ui.label('Abdullah Zia').classes('text-4xl md:text-5xl font-bold mb-2')
                    ui.label('AI Enthusiast & Web Developer').classes('text-xl md:text-2xl mb-4')
                    ui.label('F.A Graduate ').classes('text-lg mb-6')
                    with ui.row().classes('gap-2 items-center mb-4'):
                        ui.label('Client Rating:').classes('text-lg')
                        for _ in range(5):
                            ui.icon('star', color='gold').classes('rating')
                        ui.label('(5/5)').classes('text-lg')
                    ui.button('Contact Me', on_click=lambda: ui.scroll_to('contact-section')).classes('btn-info mt-2')
                with ui.column().classes('w-full md:w-1/3 flex justify-center'):
                    # Use the data URL for the profile image
                    ui.image(profile_image_url).classes('profile-image')
        
        # Skills Section
        with ui.column().classes('w-full').props('id="skills-section"'):
            ui.label('Skills & Expertise').classes('text-3xl font-bold mb-6 text-center section-title')
            
            # Card 1 - AI
            with ui.card().classes('card w-full'):
                with ui.row().classes('w-full gap-6 items-center'):
                    with ui.column().classes('w-full md:w-1/3'):
                        ui.image('https://picsum.photos/seed/ai/400/300').classes('card-image')
                    with ui.column().classes('w-full md:w-2/3'):
                        ui.label('Artificial Intelligence').classes('text-2xl font-bold mb-2')
                        ui.label('Passionate about AI technologies and their applications in solving real-world problems. Continuously learning and exploring new AI frameworks and methodologies.').classes('text-lg')
                        with ui.row().classes('flex-wrap mt-2'):
                            ui.label('Machine Learning').classes('skill-tag ai-tag')
                            ui.label('Neural Networks').classes('skill-tag ai-tag')
                            ui.label('Deep Learning').classes('skill-tag ai-tag')
                        
                        # AI Examples
                        with ui.column().classes('w-full mt-4'):
                            ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
                            # Example 1
                            with ui.card().classes('example-card ai-example'):
                                ui.label('Chatbot Development').classes('font-bold mb-1')
                                ui.label('Created an intelligent chatbot using NLP techniques that can understand and respond to user queries with 85% accuracy.').classes('text-sm')
                            
                            # Example 2
                            with ui.card().classes('example-card ai-example'):
                                ui.label('Image Classification').classes('font-bold mb-1')
                                ui.label('Developed a CNN model that classifies images into 10 categories with 92% accuracy using TensorFlow and Keras.').classes('text-sm')
            
            # Card 2 - Machine Learning (Image on right)
            with ui.card().classes('card w-full'):
                with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
                    with ui.column().classes('w-full md:w-1/3'):
                        ui.image('https://picsum.photos/seed/ml/400/300').classes('card-image')
                    with ui.column().classes('w-full md:w-2/3'):
                        ui.label('Machine Learning').classes('text-2xl font-bold mb-2')
                        ui.label('Developing predictive models and algorithms to extract insights from data. Experienced in various ML techniques and data preprocessing methods.').classes('text-lg')
                        with ui.row().classes('flex-wrap mt-2'):
                            ui.label('Data Analysis').classes('skill-tag ml-tag')
                            ui.label('Predictive Modeling').classes('skill-tag ml-tag')
                            ui.label('Algorithms').classes('skill-tag ml-tag')
                        
                        # ML Examples
                        with ui.column().classes('w-full mt-4'):
                            ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
                            # Example 1
                            with ui.card().classes('example-card ml-example'):
                                ui.label('Sales Prediction Model').classes('font-bold mb-1')
                                ui.label('Built a regression model to predict monthly sales based on historical data, achieving 94% accuracy and helping business planning.').classes('text-sm')
                            
                            # Example 2
                            with ui.card().classes('example-card ml-example'):
                                ui.label('Customer Segmentation').classes('font-bold mb-1')
                                ui.label('Implemented K-means clustering to segment customers into 5 distinct groups based on purchasing behavior for targeted marketing.').classes('text-sm')
            
            # Card 3 - Web Developer
            with ui.card().classes('card w-full'):
                with ui.row().classes('w-full gap-6 items-center'):
                    with ui.column().classes('w-full md:w-1/3'):
                        ui.image('https://picsum.photos/seed/webdev/400/300').classes('card-image')
                    with ui.column().classes('w-full md:w-2/3'):
                        ui.label('Web Developer').classes('text-2xl font-bold mb-2')
                        ui.label('Creating responsive and user-friendly websites with modern technologies. Focused on clean code, performance optimization, and cross-browser compatibility.').classes('text-lg')
                        with ui.row().classes('flex-wrap mt-2'):
                            ui.label('HTML/CSS').classes('skill-tag web-tag')
                            ui.label('JavaScript').classes('skill-tag web-tag')
                            ui.label('React').classes('skill-tag web-tag')
                        
                        # Web Dev Examples
                        with ui.column().classes('w-full mt-4'):
                            ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
                            # Example 1
                            with ui.card().classes('example-card web-example'):
                                ui.label('Portfolio Website').classes('font-bold mb-1')
                                ui.label('Designed and developed a responsive portfolio website with modern UI/UX, animations, and mobile-first design approach.').classes('text-sm')
                            
                            # Example 2
                            with ui.card().classes('example-card web-example'):
                                ui.label('Blog Platform').classes('font-bold mb-1')
                                ui.label('Created a dynamic blog platform with content management system, user authentication, and SEO optimization features.').classes('text-sm')
            
            # Card 4 - Web Applications (Image on right)
            with ui.card().classes('card w-full'):
                with ui.row().classes('w-full gap-6 items-center flex-row-reverse'):
                    with ui.column().classes('w-full md:w-1/3'):
                        ui.image('https://picsum.photos/seed/webapp/400/300').classes('card-image')
                    with ui.column().classes('w-full md:w-2/3'):
                        ui.label('Web Applications').classes('text-2xl font-bold mb-2')
                        ui.label('Building interactive and dynamic web applications with robust backend systems. Experienced in full-stack development and database management.').classes('text-lg')
                        with ui.row().classes('flex-wrap mt-2'):
                            ui.label('Frontend').classes('skill-tag app-tag')
                            ui.label('Backend').classes('skill-tag app-tag')
                            ui.label('Database').classes('skill-tag app-tag')
                        
                        # Web App Examples
                        with ui.column().classes('w-full mt-4'):
                            ui.label('Examples:').classes('text-lg font-bold mb-2')
                            
                            # Example 1
                            with ui.card().classes('example-card app-example'):
                                ui.label('Task Management App').classes('font-bold mb-1')
                                ui.label('Developed a full-stack task management application with real-time updates, drag-and-drop functionality, and team collaboration features.').classes('text-sm')
                            
                            # Example 2
                            with ui.card().classes('example-card app-example'):
                                ui.label('E-commerce Platform').classes('font-bold mb-1')
                                ui.label('Built a complete e-commerce solution with product catalog, shopping cart, payment integration, and order management system.').classes('text-sm')
        
        # Projects Section
        with ui.column().classes('w-full mt-8').props('id="projects-section"'):
            ui.label('My Projects').classes('text-3xl font-bold mb-6 text-center section-title')
            
            with ui.row().classes('w-full gap-6 justify-center'):
                # Project 1
                with ui.card().classes('project-card w-full md:w-1/3'):
                    ui.image('https://picsum.photos/seed/project1/400/250').classes('card-image w-full')
                    ui.label('AI Image Recognition').classes('text-xl font-bold mt-4')
                    ui.label('A machine learning model that identifies objects in images with high accuracy.').classes('text-sm mt-2')
                    ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-purple mt-3')
                
                # Project 2
                with ui.card().classes('project-card w-full md:w-1/3'):
                    ui.image('https://picsum.photos/seed/project2/400/250').classes('card-image w-full')
                    ui.label('E-commerce Website').classes('text-xl font-bold mt-4')
                    ui.label('A full-featured online shopping platform with payment integration.').classes('text-sm mt-2')
                    ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-orange mt-3')
                
                # Project 3
                with ui.card().classes('project-card w-full md:w-1/3'):
                    ui.image('https://picsum.photos/seed/project3/400/250').classes('card-image w-full')
                    ui.label('Data Visualization Dashboard').classes('text-xl font-bold mt-4')
                    ui.label('Interactive dashboard for visualizing complex datasets and trends.').classes('text-sm mt-2')
                    ui.button('View Project', on_click=lambda: ui.notify('Project details coming soon!')).classes('btn-teal mt-3')
        
        # Testimonials Section
        with ui.column().classes('w-full mt-8').props('id="testimonials-section"'):
            ui.label('What People Say').classes('text-3xl font-bold mb-6 text-center section-title')
            
            with ui.row().classes('w-full gap-6 justify-center'):
                # Testimonial 1
                with ui.card().classes('testimonial-card w-full md:w-1/3'):
                    with ui.row().classes('items-center mb-3'):
                        ui.image('https://picsum.photos/seed/person1/60/60').classes('rounded-full w-12 h-12 object-cover')
                        with ui.column().classes('ml-3'):
                            ui.label('Ahmed Khan').classes('font-bold')
                            ui.label('Tech Startup CEO').classes('text-sm')
                    ui.label('Abdullah is an incredibly talented developer. His AI solutions helped our startup optimize processes and save costs. Impressed by his skills at such a young age!').classes('text-sm italic')
                
                # Testimonial 2
                with ui.card().classes('testimonial-card w-full md:w-1/3'):
                    with ui.row().classes('items-center mb-3'):
                        ui.image('https://picsum.photos/seed/person2/60/60').classes('rounded-full w-12 h-12 object-cover')
                        with ui.column().classes('ml-3'):
                            ui.label('Sara Javed').classes('font-bold')
                            ui.label('Project Manager').classes('text-sm')
                    ui.label('Working with Abdullah was a pleasure. He delivered our web application ahead of schedule with exceptional quality. His technical knowledge is impressive.').classes('text-sm italic')
                
                # Testimonial 3
                with ui.card().classes('testimonial-card w-full md:w-1/3'):
                    with ui.row().classes('items-center mb-3'):
                        ui.image('https://picsum.photos/seed/person3/60/60').classes('rounded-full w-12 h-12 object-cover')
                        with ui.column().classes('ml-3'):
                            ui.label('Muhammad Ali').classes('font-bold')
                            ui.label('Data Scientist').classes('text-sm')
                    ui.label('Abdullah\'s machine learning models are top-notch. He has a deep understanding of algorithms and their practical applications. A rising star in the tech field!').classes('text-sm italic')
            
            # Additional testimonials in a second row
            with ui.row().classes('w-full gap-6 justify-center mt-6'):
                # Testimonial 4
                with ui.card().classes('testimonial-card w-full md:w-1/3'):
                    with ui.row().classes('items-center mb-3'):
                        ui.image('https://picsum.photos/seed/person4/60/60').classes('rounded-full w-12 h-12 object-cover')
                        with ui.column().classes('ml-3'):
                            ui.label('Fatima Ahmed').classes('font-bold')
                            ui.label('Marketing Director').classes('text-sm')
                    ui.label('Abdullah developed a data analysis tool for our marketing team that transformed how we understand customer behavior. His insights led to a 30% increase in campaign effectiveness.').classes('text-sm italic')
                
                # Testimonial 5
                with ui.card().classes('testimonial-card w-full md:w-1/3'):
                    with ui.row().classes('items-center mb-3'):
                        ui.image('https://picsum.photos/seed/person5/60/60').classes('rounded-full w-12 h-12 object-cover')
                        with ui.column().classes('ml-3'):
                            ui.label('Usman Malik').classes('font-bold')
                            ui.label('CTO at TechInnovate').classes('text-sm')
                    ui.label('I hired Abdullah for a complex AI project and was blown away by his problem-solving abilities. He not only delivered an excellent solution but also documented everything thoroughly. Highly recommended!').classes('text-sm italic')
                
                # Testimonial 6
                with ui.card().classes('testimonial-card w-full md:w-1/3'):
                    with ui.row().classes('items-center mb-3'):
                        ui.image('https://picsum.photos/seed/person6/60/60').classes('rounded-full w-12 h-12 object-cover')
                        with ui.column().classes('ml-3'):
                            ui.label('Ayesha Siddiqui').classes('font-bold')
                            ui.label('UI/UX Designer').classes('text-sm')
                    ui.label('As a designer, I\'ve worked with many developers, but Abdullah stands out for his attention to detail and commitment to bringing design visions to life. His frontend skills are exceptional!').classes('text-sm italic')
        
        # Contact Section
        with ui.column().classes('w-full mt-8').props('id="contact-section"'):
            ui.label('Get In Touch').classes('text-3xl font-bold mb-6 text-center section-title')
            with ui.card().classes('card w-full'):
                with ui.row().classes('w-full gap-6 items-center'):
                    with ui.column().classes('w-full md:w-1/2'):
                        ui.label('Contact Information').classes('text-2xl font-bold mb-4')
                        with ui.row().classes('items-center gap-3 mb-3'):
                            ui.icon('person', color='primary')
                            ui.label('Abdullah Zia').classes('text-lg')
                        with ui.row().classes('items-center gap-3 mb-3'):
                            ui.icon('phone', color='primary')
                            ui.label('03132691012').classes('text-lg')
                        with ui.row().classes('items-center gap-3'):
                            ui.icon('email', color='primary')
                            ui.label('@zia2691.com').classes('text-lg')
                    with ui.column().classes('w-full md:w-1/2'):
                        ui.label('Send a Message').classes('text-2xl font-bold mb-4')
                        name_input = ui.input('Name').classes('w-full mb-3')
                        email_input = ui.input('Email').classes('w-full mb-3')
                        message_input = ui.textarea('Message').classes('w-full mb-3')
                        ui.button('Send Message', on_click=lambda: handle_form_submit(name_input.value, email_input.value, message_input.value)).classes('btn-info')
    
    # Footer
    with ui.footer().classes('footer w-full max-w-6xl mx-auto mt-8'):
        with ui.column().classes('w-full items-center'):
            ui.label('© 2023 Abdullah Zia - AI Enthusiast & Web Developer').classes('text-center')
            with ui.row().classes('gap-4 mt-2'):
                ui.button('LinkedIn', on_click=lambda: ui.open('https://linkedin.com')).classes('btn-primary')
                ui.button('GitHub', on_click=lambda: ui.open('https://github.com')).classes('btn-secondary')
                ui.button('Twitter', on_click=lambda: ui.open('https://twitter.com')).classes('btn-accent')

def handle_form_submit(name, email, message):
    if name and email and message:
        ui.notify(f'Thank you {name}! Your message has been sent.', color='positive')
    else:
        ui.notify('Please fill in all fields.', color='negative')

ui.run()