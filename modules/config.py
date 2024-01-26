# config.py

class Config:
    COLUMNS = 11
    ROWS = 6

    GRID_THICKNESS = 2

    RECT_SIZE = 100

    WINDOW_WIDTH = COLUMNS * RECT_SIZE
    WINDOW_HEIGHT = ROWS * RECT_SIZE

    START_POINT = (7,4)
    END_POINT = (4,1)
    BARRIERS_POS = [(3,1),(3,2),(4,2),(5,2),(6,2),(7,2)]