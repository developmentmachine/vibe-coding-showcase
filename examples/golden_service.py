import logging
from typing import Optional
from httpx import AsyncClient, HTTPStatusError

# 初始化完美的日志格式（AI 会模仿这个）
logger = logging.getLogger("agent.golden_service")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class BaseServiceError(Exception):
    """基础异常类，AI 需要模仿这种异常封装"""
    pass

class DataFetchError(BaseServiceError):
    pass

class GoldenBaseService:
    """
    黄金示例：这是你希望 AI 模仿的完美代码风格。
    包含了：
    1. 依赖注入 (httpx.AsyncClient)
    2. 防御性编程与优雅的异常捕获
    3. 清晰的 Type Hinting
    4. 结构化的 Logger
    """
    def __init__(self, client: Optional[AsyncClient] = None):
        # 依赖注入，便于 Mock 和测试
        self._client = client or AsyncClient(timeout=10.0)

    async def fetch_remote_data(self, endpoint: str) -> dict:
        logger.info(f"Fetching data from endpoint: {endpoint}")
        try:
            response = await self._client.get(endpoint)
            response.raise_for_status()
            return response.json()
        except HTTPStatusError as e:
            logger.error(f"HTTP error occurred: {e.response.status_code}")
            # 必须封装为内部业务异常，不能向外裸露第三方异常
            raise DataFetchError(f"Failed to fetch data: HTTP {e.response.status_code}")
        except Exception as e:
            logger.exception("An unexpected error occurred during data fetch.")
            raise DataFetchError(f"Unexpected error: {str(e)}")
        finally:
            # 演示完备的生命周期意识
            logger.debug(f"Fetch operation finished for {endpoint}")
