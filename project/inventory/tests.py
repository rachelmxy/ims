from django.http import response
from django.test import TestCase, Client
from .models import Inventory, Supplier

# Create your tests here.

class Inventory_App_Tests(TestCase):
    # test for "/inventory" page    
    def test_inventory_page(self):
        response = self.client.get('/inventory', follow=True)
        self.assertEqual(response.status_code, 200)

    # test for "/inventory/<id>" page
    def test_single_item_page(self):
        test_supp = Supplier.objects.create(supp_name="test supplier")
        test_model = Inventory.objects.create(inv_name="test", description="test", price=66, note="",stock=1, availability=True, supplier=test_supp)

        response = self.client.get('/inventory/id=1', follow=True)
        self.assertEqual(response.status_code, 200)

    # test for "/api/inventory" page
    def test_api(self):
        response = self.client.get('/api/inventory', follow=True)
        self.assertEqual(response.status_code, 200) 