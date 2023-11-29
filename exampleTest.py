import unittest
import requests
import json

class Numbers(unittest.TestCase):

    
    def test_products_list_get(self):
        payload = {"key1":"value1"}
        cevap = requests.get("https://automationexercise.com/api/productsList", data=payload)
        print (cevap.text)
        
    def test_products_list_post(self):
        payload = {"key1":"value1"}
        gonder = requests.post("https://automationexercise.com/api/productsList", data=payload)
        print (gonder.text)

    def test_brands_list_get(self):
        cevap = requests.get("https://automationexercise.com/api/brandsList")
        #print(cevap.text)
        icerik = json.loads(cevap.text)
        icerik_id = icerik["brands"][1]["id"]
        self.assertEqual(2,icerik_id)

    def test_brands_list_put(self):
        gonder = requests.put("https://automationexercise.com/api/brandsList")
        print(gonder.text)

    def test_search_product_post(self):
        payload = {"search_product":"jean"}
        gonder = requests.post("https://automationexercise.com/api/searchProduct", data=payload)
        #print(gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual("Jeans", icerik["products"][0]["category"]["category"]) 

    def test_search_product_post2(self):
        gonder = requests.post("https://automationexercise.com/api/searchProduct")
        print(gonder.text)
    
    def test_verify_login_post(self):
        payload = {"email":"hasan1@email.com","password":"123456789"}
        gonder = requests.post("https://automationexercise.com/api/verifyLogin",data=payload)
        print(gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual(200, icerik["responseCode"]) 

    def test_verify_login_post2(self):
        payload = {"password":"password"}
        gonder = requests.post("https://automationexercise.com/api/verifyLogin",data=payload)
        print(gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual(400, icerik["responseCode"]) 

    def test_verify_login_delete(self):
        payload = {"password":"password"}
        gonder = requests.delete("https://automationexercise.com/api/verifyLogin",data=payload)
        print(gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual(405, icerik["responseCode"])

        
    def test_create_account_post(self):
        payload = {"name":"Hasan","email":"hasanevin@email.com","password":"hasan123a","title":"Mr","birth_date":"15","birth_month":"03","birth_year":"1999","firstname":"Hasan","lastname":"Evin","company":"ISU","address1":"Istanbul","address2":"Bahcelievler","country":"Turkey","zipcode":"34180","state":"Bahceli","city":"Istanbul","mobile_number":"5318619590"}
        gonder = requests.post("https://automationexercise.com/api/createAccount",data=payload)
        print(gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual("User created!",icerik["message"])

    def test_user_account_delete(self):
        payload = {"email":"hasan1@email.com","password":"123456789"}
        gonder = requests.delete("https://automationexercise.com/api/deleteAccount",data=payload)
        print(gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual("Account deleted!",icerik["message"])

    def test_user_account_update_put(self):
        payload = {"name":"Hasan","email":"hasanevin@email.com","password":"hasan123a","title":"Mr","birth_date":"15","birth_month":"03","birth_year":"1999","firstname":"Hasan","lastname":"Evin","company":"ISU","address1":"Istanbul","address2":"Bahcelievler","country":"Turkey","zipcode":"34180","state":"Bahceli","city":"Istanbul","mobile_number":"5318619590"}
        gonder = requests.put("https://automationexercise.com/api/updateAccount",data=payload)
        print(gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual("User updated!",icerik["message"])

    def test_user_account_detail_get(self):
        payload = {"email":"hasan1@email.com"}
        cevap = requests.get("https://automationexercise.com/api/getUserDetailByEmail")
        print(cevap.text)

 

if __name__ == '__main__':
    unittest.main()
