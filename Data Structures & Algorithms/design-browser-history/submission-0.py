class Webpage:
    def __init__(self, back=None, url="", forward=None): 
        self.back = back
        self.url = url
        self.forward = forward

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = Webpage(None, homepage, None)

    def visit(self, url: str) -> None:
        new_webpage = Webpage(self.current, url, None)
        self.current.forward = new_webpage
        self.current = new_webpage

    def back(self, steps: int):
        while (steps > 0) and self.current.back: 
            self.current = self.current.back
            steps -= 1
        return str(self.current.url)

    def forward(self, steps: int):
        while (steps > 0) and self.current.forward: 
            self.current = self.current.forward
            steps -= 1
        return str(self.current.url)