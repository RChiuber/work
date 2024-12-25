from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QListWidgetItem
from PyQt6 import uic
import sys
import datetime
from PyQt6.QtGui import QFont

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        # 載入 UI
        uic.loadUi('todo_app.ui', self)

        # 連接功能
        self.addButton.clicked.connect(self.add_task)
        self.deleteButton.clicked.connect(self.delete_task)
        self.markCompleteButton.clicked.connect(self.mark_complete)

    def add_task(self):
        task = self.taskInput.text()
        if task.strip():
            # 获取当前时间，并格式化为字符串
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            task_with_time = f"{task} (Added: {current_time})"
            item = QListWidgetItem(task_with_time)  # 创建任务项
            self.taskList.addItem(item)
            self.taskInput.clear()
        else:
            QMessageBox.warning(self, "Error", "Task cannot be empty")

    def delete_task(self):
        selected_task = self.taskList.currentItem()
        if selected_task:
            self.taskList.takeItem(self.taskList.row(selected_task))
        else:
            QMessageBox.warning(self, "Error", "No task selected")

    def mark_complete(self):
        selected_task = self.taskList.currentItem()
        if selected_task:
            # 获取当前字体并设置删除线
            font = selected_task.font()
            font.setStrikeOut(True)  # 设置删除线
            selected_task.setFont(font)
            # 将任务标记为已完成
            selected_task.setText(f"{selected_task.text()} (Completed)")
        else:
            QMessageBox.warning(self, "Error", "No task selected")

# 主程式
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())
