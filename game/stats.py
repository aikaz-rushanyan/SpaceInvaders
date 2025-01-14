class Stats():
    """Отслеживание статистики"""

    def __init__(self):
        """инициализирует статистику"""
        self.reset_stats()
        self.run_game = True
        with open('record.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """Статистика во время игры"""
        self.players_left = 2
        self.score = 0
