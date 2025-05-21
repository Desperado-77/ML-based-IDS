
# ML-based IDS

A **Machine Learning-based Intrusion Detection System** with a customized PySide6 GUI interface. The system visualizes data distributions, supports multiple ML model evaluation, and presents comparison metrics like accuracy, false positive rate, and more.

---

## 🚀 Features

- ⚙️ Frameless, draggable, and styled PySide6 GUI (based on `qframelesswindow`)
- 📊 One-click statistical chart generation for data exploration
- 🔍 Switchable model evaluation: Decision Tree, Logistic Regression, Neural Network
- 📈 Confusion matrix and model comparison visualization
- 📂 Easy model selection via radio buttons and dropdowns
- 📑 Supports modular data mining via `data_mining.py`
- 🖼️ All output results shown in the GUI as image plots

---

## 📂 Project Structure

```
ML-based-IDS/
├── app.py                # Main GUI application entry
├── data_mining.py        # Core logic: image path routing for analysis
├── ui_window.py          # Auto-generated GUI layout
├── style.qss             # Qt stylesheet for GUI
├── requirements.txt      # Required Python packages
├── 调参.ipynb             # Jupyter Notebook for hyperparameter tuning
└── .img/                 # Output image folder (used by GUI)
```

---

## 🛠 Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python app.py
```

---

## ✅ Dependencies

Main dependencies (from `requirements.txt`):

- `PySide6` GUI framework
- `PySideSix-Frameless-Window`
- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `scikit-learn`

---

## 📷 Screenshots

> You can generate charts such as:
- Service, Label, Protocol, Flag, Target, Attack type statistics
- Model-specific evaluations
- Confusion matrices
- Accuracy and FPR/DR comparison charts

---

## 🧪 Models Supported

| ID | Model                |
|----|----------------------|
| 1  | Decision Tree        |
| 2  | Logistic Regression  |
| 3  | Artificial Neural Net|

Use radio buttons and dropdowns in the GUI to select model and evaluation type.

---

## 📌 Author

**杨琪 (Yang Qi)**  
School Project: Machine Learning-based Intrusion Detection System

---

## 📎 Notes

- All output images are saved in `.img/` folder and loaded dynamically.
- GUI title: `基于机器学习的入侵检测系统` (Intrusion Detection System Based on Machine Learning)

---

## 🔒 License

This project is for educational and academic use only.
