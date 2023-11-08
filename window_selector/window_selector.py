import json
from screenshot import Window

def run_windowing():
    window = Window()
    return window.run()
    

if __name__ == "__main__":
    points = run_windowing()
    print(points)
    with open('points.json', 'w') as f:
        json.dump(points, f)