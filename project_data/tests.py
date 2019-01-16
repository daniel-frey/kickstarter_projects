from django.test import TestCase, RequestFactory
from .models import Kickstarter


class TestKickstarterViews(TestCase):
    """Test the kickstarter views page"""
    def setUp(self):
        self.request = RequestFactory()
        """Test the setup of the kickstarter view page"""
        self.kickstarter = Kickstarter.objects.create(
            id_data=1000002330,
            name='The Songs of Adelaide & Abullah',
            category='Poetry',
            main_category='Publishing',
            currency='GBP',
            deadline='2015-10-09',
            goal=1000,
            launched='2015-08-11 12:12:28',
            pledged=0,
            state='failed',
            backers=0,
            country='GB',
            usd_pledged=0.00,
            usd_pledged_real=0.00,
            usd_goal_real=1533.95,
        )

    def test_list_view_context(self):
        """Test that the list view shows the correct context"""
        from .views import kickstarter_list_view
        request = self.request.get('')
        response = kickstarter_list_view(request)
        self.assertIn(b'The Songs', response.content)

    def test_list_view_status(self):
        """Test that the status code is correct"""
        from .views import kickstarter_list_view
        request = self.request.get('')
        response = kickstarter_list_view(request)
        self.assertEqual(200, response.status_code)

    def test_detail_view_context(self):
        """Test that the kickstarter detail view is correct"""
        from .views import kickstarter_detail_view
        request = self.request.get('')
        response = kickstarter_detail_view(request, self.kickstarter.id)
        self.assertIn(b'The Songs', response.content)

    def test_detail_view_status_code_failure(self):
        """Test that the status code of 404 is received"""
        from .views import kickstarter_detail_view
        from django.http import Http404
        request = self.request.get('')
        with self.assertRaises(Http404):
            kickstarter_detail_view(request, '0')
