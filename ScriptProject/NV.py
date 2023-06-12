import tkinter as tk
import spam


lat2 = 0
lon2 = 0

def set_point(_lat,_lon) :
    global lat2, lon2
    lat2 = float(_lat)
    lon2 = float(_lon)

def run() :
    def calculate_distance():
        lat1 = float(entry_lat1.get())
        lon1 = float(entry_lon1.get())
        
        distance = spam.distance(lat1, lon1, lat2, lon2)
        
        result_label.config(text=f"거리: {distance:.2f} km")
    
    distance_window = tk.Tk()
    distance_window.title("거리 계산")
    
    label_lat1 = tk.Label(distance_window, text="위도:")
    label_lat1.grid(row=0, column=0)
    entry_lat1 = tk.Entry(distance_window)
    entry_lat1.grid(row=0, column=1)
    
    label_lon1 = tk.Label(distance_window, text="경도:")
    label_lon1.grid(row=1, column=0)
    entry_lon1 = tk.Entry(distance_window)
    entry_lon1.grid(row=1, column=1)
    
    calculate_button = tk.Button(distance_window, text="계산", command=calculate_distance)
    calculate_button.grid(row=4, column=0, columnspan=2)
    
    result_label = tk.Label(distance_window, text="")
    result_label.grid(row=5, column=0, columnspan=2)