import json

class ResellerUtil:

    resellers_file_path = "resellers.json"

    def get_reseller_by_token(self, token: str) -> dict:

        with open(file=self.resellers_file_path, mode="r") as resellers_file:
            resellers = json.loads(resellers_file.read())

            for reseller in resellers:
                if reseller["token"] == token:
                    return reseller