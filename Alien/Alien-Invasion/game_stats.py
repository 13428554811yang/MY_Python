class GameStats:
    """跟踪 Alien Invasion 的统计数据。"""

    def __init__(self, ai_settings):
        """初始化统计信息。"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 在非活动状态下启动游戏。
        self.game_active = False

        # 高分永远不应该被重置。
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏过程中可能更改的统计数据."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
