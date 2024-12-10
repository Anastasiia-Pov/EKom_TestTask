from beanie import Document


class FormTemplates(Document):
    name: str

    class Settings:
        name = "FormTemplates"

    class Config:
        extra = "allow"
