from util.reseller import ResellerUtil

class TestDatetime:

    def test_get_reseller_by_tokeny(self):

        reseller_util = ResellerUtil()
        reseller_util.resellers_file_path = "test/resellers_test.json"

        token = "1111111111111111111111111111111111111111111111111111111111111111"
        reseller = reseller_util.get_reseller_by_token(token=token)

        expected_reseller = {
            "name": "Sophie",
            "token": "1111111111111111111111111111111111111111111111111111111111111111"
        }

        assert reseller == expected_reseller