from pydantic import BaseModel, ConfigDict, model_serializer

class InBase(BaseModel):
    # Trim cả đầu/cuối cho input từ client
    model_config = ConfigDict(str_strip_whitespace=True)

class OutBase(BaseModel):
    # Trim chỉ khoảng trắng ở CUỐI khi serialize ra JSON
    @model_serializer(mode="wrap", when_used="json")
    def _trim_trailing_spaces(self, handler):
        data = handler(self)

        def trim(v):
            if isinstance(v, str):
                return v.rstrip()
            if isinstance(v, list):
                return [trim(x) for x in v]
            if isinstance(v, dict):
                return {k: trim(x) for k, x in v.items()}
            return v

        return trim(data)
