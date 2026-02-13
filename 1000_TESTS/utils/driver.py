class DummyWebDriver:
    def get(self,url):
        if "fail-url" in url:
            raise Exception("NavigationException")
    def find(self,sel):
        if "missing" in sel:
            raise Exception("ElementNotFoundException")
        return True
