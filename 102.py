class Dog:
    # 屬性
    def __init__(self, name, age):
        self.name = name  # 屬性
        self.age = age    # 屬性

    # 方法
    def intro(self):
        print(f"{self.name} is {self.age} years old!")

# 創建物件
dog1 = Dog("Buddy", 3)
dog1.intro()  # 輸出：Buddy is 3 years old!
dog2 = Dog("Candy", 5)
dog2.intro()  # 輸出：Candy is 5 years old!
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton
from PyQt6.QtWidgets import QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 基本 GUI")
        self.resize(400, 300)

        # 建立標籤與按鈕
        self.label = QLabel("按下按鈕開始計數！", self)
        self.button = QPushButton("點擊我", self)

        # 計數變數
        self.counter = 0

        # 設定佈局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # 連接按鈕點擊事件
        self.button.clicked.connect(self.increment_counter)

    def increment_counter(self):
        self.counter += 1
        self.label.setText(f"按鈕已被點擊 {self.counter} 次！")

# 主程式入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
