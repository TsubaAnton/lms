from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self,field):
        self.field = field

    def __call__(self, url):
        youtube = 'https://youtube.com/'

        if url.get('link'):
            if youtube not in url.get('url'):
                raise ValidationError('You should use youtube url')
        else:
            return None
