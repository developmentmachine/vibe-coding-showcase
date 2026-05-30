from pydantic import BaseModel, Field, field_validator
from typing import Literal

class StockAnalysisRequest(BaseModel):
    """
    输入契约：规定了 AI 接收到的参数形态
    """
    symbol: str = Field(..., description="股票代码，例如 sh600519")
    market: Literal["sh", "sz", "bj"] = Field(..., description="所属市场")

    @field_validator('symbol')
    @classmethod
    def validate_symbol_format(cls, v: str) -> str:
        if not v.startswith(('sh', 'sz', 'bj')):
            raise ValueError("股票代码必须以 sh, sz 或 bj 开头")
        if len(v) != 8:
            raise ValueError("股票代码总长度必须为8位（2位市场代码+6位数字）")
        return v

class StockSentimentResponse(BaseModel):
    """
    输出契约：规定了 AI 生成的返回数据形态
    """
    symbol: str
    sentiment_score: float = Field(..., ge=-1.0, le=1.0, description="情绪得分 -1 到 1")
    summary: str = Field(..., max_length=200, description="一句话分析总结")
    is_hot: bool = Field(default=False, description="是否属于当前热门板块")
