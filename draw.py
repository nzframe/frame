from application.draw_app import DrawAPP
from utility.draw import DrawIT
from pathlib import Path

frame_photo_path = Path(__file__).parent / "frame.png" 
td = DrawIT(frame_photo_path.as_posix())

config_path = Path(__file__).parent / "config.yml" 

def main():
    app = DrawAPP(config_path)
    app.execute(td)
    
if __name__ == "__main__":
    main()
