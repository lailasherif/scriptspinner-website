from datetime import date, datetime, timedelta
from django.test import TestCase
from django.contrib.auth import get_user_model
from user.models import ScriptSpinnerUser


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('super@user.com', 'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)


class PaymentUnitTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(
            email="test@email.com"
        )
        self.user.save()

    def test_has_paid(self):
        self.assertFalse(
            self.user.has_paid(),
            "Initial user should have empty paid_until attr"
        )

    def test_different_date_values(self):
        current_date = date(2020, 1, 4)
        _30days = timedelta(days=30)

        self.user.set_paid_until(current_date + _30days)

        self.assertTrue(
            self.user.has_paid(
                current_date=current_date
            )
        )

        self.user.set_paid_until(current_date - _30days)

        self.assertFalse(
            self.user.has_paid(
                current_date=current_date
            )
        )

    def test_different_input_types(self):
        current_date = datetime(2020, 4, 1)
        _30days = timedelta(days=30)

        ts_in_future = datetime.timestamp(current_date + _30days)

        self.user.set_paid_until(
            int(ts_in_future)
        )

        self.user.set_paid_until(
            '1212344545'
        )