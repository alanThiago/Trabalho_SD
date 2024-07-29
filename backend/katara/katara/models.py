class Movie:
    def __init__(self, title: str):
        self.title = title

    def to_dict(self):
        return {
            'title': self.title
        }

    @staticmethod
    def from_dict(data):
        return Movie(
            title=data['title']
        )
