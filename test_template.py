import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.template import loader

try:
    template = loader.get_template('pages/home.html')
    print("✅ Template loaded successfully!")
except Exception as e:
    print(f"❌ Error loading template:")
    print(f"   {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
