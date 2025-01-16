class Document:
    def __init__(self, name, text, upload_date):
        self.name = name
        self.text = text
        self.upload_date = upload_date

    def to_dict(self):
        return {
            "name": self.name,
            "text": self.text,
            "upload_date": self.upload_date
        }
