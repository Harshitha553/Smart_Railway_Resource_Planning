🚆 Smart Railway Resource Planning System
📌 Overview

The Smart Railway Resource Planning System is a data-driven application designed to improve railway station operations by optimizing platform allocation, detecting scheduling conflicts, and predicting train delays. Railway stations manage multiple trains, platforms, and tracks daily, and inefficient planning can lead to congestion, delays, and underutilized infrastructure.

This project uses algorithmic scheduling techniques and machine learning to analyze train schedules and improve resource utilization. An interactive Streamlit dashboard is used to visualize scheduling results, platform utilization, and delay predictions.

🎯 Objectives

Optimize platform allocation for incoming and outgoing trains.

Detect platform conflicts when multiple trains overlap in schedule.

Analyze platform utilization efficiency.

Predict potential train delays using machine learning.

Provide an interactive dashboard for visualization and analysis.

⚙️ Features

✔ Train schedule analysis using synthetic dataset
✔ Greedy algorithm for platform optimization
✔ Conflict detection for overlapping train schedules
✔ Platform utilization analysis with visualization
✔ Machine Learning model for delay prediction
✔ Interactive Streamlit dashboard for real-time analysis

📊 Dataset

Since real railway data is confidential, a synthetic dataset was generated for this project.

Dataset Attributes
Train_ID

Train_Type

Arrival_Time_Min

Departure_Time_Min

Halt_Duration_Min

Platform_Assigned

Track_Number

Peak_Hour

Weather

Previous_Delay_Min

Delay_Minutes

The dataset simulates real-world railway operations including peak-hour congestion, weather conditions, and historical delays.

🧠 Methodology
1️⃣ Platform Optimization

A greedy scheduling algorithm assigns trains to the earliest available platform based on arrival time to reduce overlaps and idle time.

2️⃣ Conflict Detection

The system checks if two trains are assigned to the same platform during overlapping time intervals and flags these as conflicts.

3️⃣ Platform Utilization

Platform usage is calculated as:

𝑈
𝑡
𝑖
𝑙
𝑖
𝑧
𝑎
𝑡
𝑖
𝑜
𝑛
=
𝑇
𝑜
𝑡
𝑎
𝑙
 
𝐻
𝑎
𝑙
𝑡
 
𝑇
𝑖
𝑚
𝑒
𝑇
𝑜
𝑡
𝑎
𝑙
 
𝑇
𝑖
𝑚
𝑒
 
𝐴
𝑣
𝑎
𝑖
𝑙
𝑎
𝑏
𝑙
𝑒
×
100
Utilization=
Total Time Available
Total Halt Time
	​

×100

This helps identify heavily used and underutilized platforms.

4️⃣ Delay Prediction

A Random Forest Regression model predicts train delays based on:

Previous delay

Peak hour congestion

Weather conditions
🖥️ Tech Stack
| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Core programming     |
| Pandas       | Data processing      |
| NumPy        | Numerical operations |
| Scikit-learn | Machine learning     |
| Matplotlib   | Data visualization   |
| Streamlit    | Web dashboard        |

📁 Project Structure
railway_project/
│
├── data/
│   └── synthetic_dataset.csv
│
├── models/
│   └── delay_model.pkl
│
├── scheduler.py
├── optimizer.py
├── conflict_detector.py
├── train_model.py
├── app.py
├── requirements.txt
└── README.md

md
🚀 How to Run the Project

1️⃣ Clone the Repository
git clone https://github.com/your-username/railway-resource-planning.git
cd railway-resource-planning
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Train the Delay Prediction Model
streamlit run app.py
The application will open in your browser.

📈 Output

The system provides:

Optimized platform allocation

Conflict detection results

Platform utilization visualization

Delay prediction using machine learning

🔮 Future Improvements

Integration with real-time railway data

Advanced scheduling using graph algorithms

Real-time delay monitoring system

AI-based train traffic forecasting

👩‍💻 Author

Harshitha Nalubala
B.Tech Student | Data Science & Machine Learning Enthusiast