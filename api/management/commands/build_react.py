import os
import shutil
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Builds the React app and moves the build files to the Django project'

    def handle(self, *args, **kwargs):
        # Define paths
        frontend_dir = os.path.join(os.path.dirname(__file__), '../../../../bluediamond')
        build_dir = os.path.join(frontend_dir, 'dist')  # Vite output folder (use `build` if React default)
        templates_dir = os.path.join(os.path.dirname(__file__), '../../../backend/templates')
        static_dir = os.path.join(os.path.dirname(__file__), '../../../backend/static/frontend')

        # Step 1: Run the React build command
        self.stdout.write(self.style.NOTICE('Building React app...'))
        os.system(f'cd {frontend_dir} && npm run build')

        # Step 2: Copy index.html to the templates folder
        self.stdout.write(self.style.NOTICE('Copying index.html to templates...'))
        index_html = os.path.join(build_dir, 'index.html')
        shutil.copy(index_html, templates_dir)

        # Step 3: Copy static files (JS, CSS) to the Django static folder
        self.stdout.write(self.style.NOTICE('Copying static files to Django static folder...'))
        if os.path.exists(static_dir):
            shutil.rmtree(static_dir)  # Remove old static files
        shutil.copytree(os.path.join(build_dir), static_dir)
        os.system(f'cd {os.path.join(os.path.dirname(__file__),'../../../')} && python manage.py collectstatic')
        self.stdout.write(self.style.SUCCESS('React app built and copied successfully!'))
