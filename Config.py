parameters = {
    "animation": True,
    "God":
        {
            "size": [30, 20],
            "dt": 0.005,
            "ct": 0.05,
            "pt": 0.005,
            "latency": 0.02,
            "errorrate": 0.05,
            "k_p": 5,
            "k_d": 0.2,
            "Layout": True,
            "Path": False
        },
    "SpaceFree2D":
        {
            "px_width": 800,
            "fps": 50
        },
    "Layout":
        {
            "Obstacles_in_x_direction": 5,
            "Obstacles_in_y_direction": 4
        },
    "DC-Motor":
        {
            "Jm": 0.03,
            "Bm": 0.1,
            "Kme": 0.01,
            "Kmt": 0.01,
            "Rm": 1,
            "Lm": 0.5,
            "Kdm": 20,
            "Kpm": 170,
            "Kim": 330,
            "Nm": 83
        },
    "Cars":
        [
            {
                "index": 0,
                "spawn_x": 1.4,
                "spawn_y": 5.5,
                "start_direction": "west",
                "end_direction": "east",
                "start_time": 0,
                "angle": 3.142,
                "length": 1,
                "width": 0.5,
                "max_vel": 4,
                "max_acc": 2,
                "color": "#FFAF00",
                "start": [0, 0],
                "finish": [4, 3],
                "max_latency": 0.02,
                "min_latency": 0.02,
                "errorrate": 0.05
            },
            {
                "index": 1,
                "spawn_x": 1.4,
                "spawn_y": 5.5,
                "start_direction": "east",
                "end_direction": "south",
                "start_time": 3,
                "angle": 0,
                "length": 1,
                "width": 0.5,
                "max_vel": 4,
                "max_acc": 2,
                "color": "#FFAFFF",
                "start": [4, 3],
                "finish": [0, 3],
                "max_latency": 0.02,
                "min_latency": 0.02,
                "errorrate": 0.05
            }
        ],
    "Path":
        [
            {
                "car_id": 0,
                "pos_x": 10.0,
                "pos_y": 10.0
            },
            {
                "car_id": 0,
                "pos_x": 25.0,
                "pos_y": 10.0
            },
            {
                "car_id": 0,
                "pos_x": 23.2,
                "pos_y": 14.4
            },
            {
                "car_id": 0,
                "pos_x": 15.0,
                "pos_y": 15.0
            }
        ],
    "Obstacles":
        [
            {
                "corners": [10, 15, 12, 15, 12, 17, 10, 17],
                "color": "red"
            },
            {
                "corners": [15, 15, 17, 15, 17, 17, 15, 17],
                "color": "red"
            },
            {
                "corners": [20, 15, 22, 15, 22, 17, 20, 17],
                "color": "red"
            }
        ],
    "CollisionControl":
        {
            "activated": False,
            "obstacle_spacing": 0.1,
            "car_spacing": 0.5,
            "polling_dif": 0.001,
            "collision_detection_frequency": 0.2
        }
}