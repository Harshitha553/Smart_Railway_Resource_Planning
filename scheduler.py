# scheduler.py

import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df


def allocate_platforms(df, num_platforms=8):
    """
    Greedy scheduling:
    - Sort by arrival time
    - Assign earliest free platform
    """

    df = df.sort_values(by="Arrival_Time_Min").reset_index(drop=True)

    platform_end_time = {i: 0 for i in range(1, num_platforms + 1)}
    assigned_platforms = []

    for _, row in df.iterrows():
        arrival = row["Arrival_Time_Min"]
        departure = row["Departure_Time_Min"]

        allocated = False
        for platform in platform_end_time:
            if platform_end_time[platform] <= arrival:
                assigned_platforms.append(platform)
                platform_end_time[platform] = departure
                allocated = True
                break

        if not allocated:
            assigned_platforms.append(-1)  # No platform available

    df["Optimized_Platform"] = assigned_platforms
    return df