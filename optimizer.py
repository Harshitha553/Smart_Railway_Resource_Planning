# optimizer.py

def calculate_platform_utilization(df, num_platforms=5):
    total_minutes = 1440  # 24 hours
    utilization = {}

    for platform in range(1, num_platforms + 1):
        platform_df = df[df["Optimized_Platform"] == platform]
        used_time = platform_df["Halt_Duration_Min"].sum()
        utilization[platform] = round((used_time / total_minutes) * 100, 2)

    return utilization


def delay_statistics(df):
    stats = {
        "Average Delay": round(float(df["Delay_Minutes"].mean()), 2),
        "Max Delay": int(df["Delay_Minutes"].max()),
        "Min Delay": int(df["Delay_Minutes"].min()),
    }
    return stats