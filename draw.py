from application.draw_app import DrawAPP
from pathlib import Path

frame_photo_path = Path(__file__).parent / "frame.png" 
png_path = frame_photo_path.as_posix()

config_path = Path(__file__).parent / "config.yml" 

def main():
    app = DrawAPP(config_path, png_path)
    app.execute()
    
if __name__ == "__main__":
    main()
