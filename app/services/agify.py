from requests import Session


class Agify(Session):
    def __init__(self, base_url: str, **kwargs):
        super(Agify, self).__init__()
        self.url = base_url

    def build_url(self, name: str):
        return self.url + f"?name={name}"

    def retrieve(self, name: str) -> dict:
        ''' return age object '''
        url = self.build_url(name)
        response = self.get(url)
        return response.json()
       