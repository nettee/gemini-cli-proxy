"""
Configuration management module

Manages application configuration
"""


class Config:
    """Application configuration class"""
    
    def __init__(self):
        import os
        
        # Server configuration
        self.host: str = "127.0.0.1"
        self.port: int = 8765
        # Read from environment variable if available (for reload mode)
        self.debug: bool = os.environ.get('GEMINI_CLI_PROXY_DEBUG', 'false').lower() == 'true'
        self.log_level: str = "debug" if self.debug else "info"
        
        # Gemini CLI configuration
        self.gemini_command: str = "gemini"  # Gemini CLI command path
        self.timeout: float = 120.0
        
        # Limit configuration
        self.rate_limit: int = 60  # Requests per minute
        self.max_concurrency: int = 4  # Maximum concurrent subprocesses
        
        # Supported models list
        self.supported_models: list = [
            "gemini-2.5-pro",
            "gemini-2.5-flash",
        ]


# Global configuration instance
config = Config() 