from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()
        
        # Create Widgets
        distance_label = QLabel("Distance:")
        self.distance_input = QLineEdit()
        time_label = QLabel("Time (hours):")
        self.time_input = QLineEdit()
        
        self.metric_drop = QComboBox()
        self.metric_drop.addItems(['Metric (Km)', 'Imperial (Mi)'])
        
        calc_button = QPushButton("Calculate Speed")
        calc_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")
        
        # Add Widgets to Grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(self.metric_drop, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(calc_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        
        self.setLayout(grid)
        
    def calculate_speed(self):
        speed = float(self.distance_input.text()) / float(self.time_input.text())
        
        if self.metric_drop.currentText() == 'Metric (Km)':
            metric = 'km/h'
            self.output_label.setText(f"Average Speed: {speed} {metric}")
            
        if self.metric_drop.currentText() == 'Imperial (Mi)':
            metric = 'm/h'
            self.output_label.setText(f"Average Speed: {speed} {metric}")

            
app = QApplication(sys.argv)     
speed_calc = SpeedCalculator()
speed_calc.show()
sys.exit(app.exec())

        