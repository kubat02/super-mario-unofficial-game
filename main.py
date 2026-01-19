"""
Super Mario Bros - Ana giriş noktası
"""
from game import Game


def main():
    """Ana fonksiyon"""
    game = Game()
    
    try:
        game.run()
    finally:
        game.quit()


if __name__ == "__main__":
    main()
