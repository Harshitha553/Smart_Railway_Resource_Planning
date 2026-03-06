# conflict_detector.py

def detect_conflicts(df):
    """
    Detect time overlap conflicts on same platform
    """

    conflicts = []

    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            if df.loc[i, "Optimized_Platform"] == df.loc[j, "Optimized_Platform"]:
                if (
                    df.loc[i, "Departure_Time_Min"] > df.loc[j, "Arrival_Time_Min"]
                    and df.loc[i, "Arrival_Time_Min"] < df.loc[j, "Departure_Time_Min"]
                ):
                    conflicts.append(
              
                        (
                            df.loc[i, "Train_ID"],
                            df.loc[j, "Train_ID"],
                        )
                    )

    return conflicts