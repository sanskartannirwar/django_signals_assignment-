from django.test import TestCase

# Create your tests here.

import threading
from .models import MyModel

def test_signal():
    print(f"Caller function running in thread: {threading.current_thread().name}")
    instance = MyModel.objects.create(name="Test Instance")
