import json
from fastapi.responses import JSONResponse


class CustomJSONResponse(JSONResponse):
    def __init__(self, content, message: str = None, status_code: int = 200, **kwargs):
        self.message = message
        super().__init__(content=content, status_code=status_code, **kwargs)

    def render(self, content):
        is_success = 200 <= self.status_code < 300
        custom_content = {
            "success": is_success,
            "message": self.message or (is_success and 'Request Success') or 'Request Failed',
        }
        if isinstance(content, dict) and 'data' in content.keys():
            custom_content.update(**content)
        else:
            custom_content['data'] = content
        if isinstance(custom_content.get('data'), dict) and custom_content.get('data', {}).get('message'):
            custom_content['message'] = custom_content['data']['message']
        return super().render(custom_content)
