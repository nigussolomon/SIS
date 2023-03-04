from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccTest(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('testsuper@gmail.com', 'password')
        self.assertEqual(super_user.email, 'testsuper@gmail.com')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "testsuper@gmail.com")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="testsuper@gmail.com", is_superuser=False, password = "password"
            )
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email="testsuper@gmail.com", is_staff=False, password = "password"
            )

    def test_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'test@gmail.com', 'password', 'Student'
        )
        self.assertEquals(user.email, "test@gmail.com")
        self.assertEquals(user.user_type, "Student")
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)
        self.assertEqual(str(user), "test@gmail.com")

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email="", is_active=False, password = "password", user_type = "Student"
            )