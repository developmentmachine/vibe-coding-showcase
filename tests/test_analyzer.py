import pytest
from src.schemas import StockAnalysisRequest

# 这是一个 TDD 的契约边界。
# AI 的任务就是让测试变绿。它必须处理异常情况，否则无法通过 test_analyze_invalid_stock。

@pytest.mark.asyncio
async def test_analyze_valid_stock():
    """测试快乐路径：合法的热门股票"""
    from src.analyzer import AShareAnalyzer # 假设 AI 将会实现这个类
    
    analyzer = AShareAnalyzer()
    req = StockAnalysisRequest(symbol="sh600519", market="sh")
    
    response = await analyzer.analyze(req)
    
    assert response.symbol == "sh600519"
    assert -1.0 <= response.sentiment_score <= 1.0
    assert response.is_hot is True

@pytest.mark.asyncio
async def test_analyze_invalid_stock():
    """测试边界异常：不存在的股票代码"""
    from src.analyzer import AShareAnalyzer
    from src.exceptions import StockNotFoundError # 规定 AI 必须实现这个异常类
    
    analyzer = AShareAnalyzer()
    req = StockAnalysisRequest(symbol="sh999999", market="sh")
    
    with pytest.raises(StockNotFoundError):
        await analyzer.analyze(req)
