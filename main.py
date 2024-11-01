import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt, QRect, QCoreApplication
from PyQt6.QtGui import QFont

class AspectRatioCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seitenverhältnis Rechner 2.0")

        # Hauptlayout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Schriftart und -größe festlegen
        font = QFont()
        font.setPointSize(16)
        self.setFont(font)

        # Linkes Layout für die erste Funktion
        left_layout = QVBoxLayout()

        # Titel für die linke Seite
        left_title = QLabel("Berechne Breite/Höhe")
        left_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(left_title)

        # Eingabe für Breite/Höhe
        dimension_label = QLabel("Breite/Höhe:")
        self.dimension_input = QLineEdit()
        dimension_input_layout = QHBoxLayout()
        dimension_input_layout.addWidget(dimension_label)
        dimension_input_layout.addWidget(self.dimension_input)
        left_layout.addLayout(dimension_input_layout)

        # Eingabe für Seitenverhältnis
        ratio_label = QLabel("Seitenverhältnis (z.B. 16:9):")
        self.ratio_input = QLineEdit()
        ratio_input_layout = QHBoxLayout()
        ratio_input_layout.addWidget(ratio_label)
        ratio_input_layout.addWidget(self.ratio_input)
        left_layout.addLayout(ratio_input_layout)

        # Button zum Berechnen
        calculate_button = QPushButton("Berechnen")
        calculate_button.clicked.connect(self.calculate_other_dimension)
        left_layout.addWidget(calculate_button)

        # Ausgabe des Ergebnisses
        self.result_dimension_label = QLabel("Ergebnis:")
        self.result_dimension_output = QLineEdit()
        self.result_dimension_output.setReadOnly(True)
        self.result_dimension_output.setStyleSheet("background-color: black; color: white;")
        result_dimension_layout = QHBoxLayout()
        result_dimension_layout.addWidget(self.result_dimension_label)
        result_dimension_layout.addWidget(self.result_dimension_output)
        left_layout.addLayout(result_dimension_layout)

        left_layout.addStretch()

        # Rechtes Layout für die zweite Funktion
        right_layout = QVBoxLayout()

        # Titel für die rechte Seite
        right_title = QLabel("Berechne Seitenverhältnis")
        right_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_layout.addWidget(right_title)

        # Eingabe für Breite
        width_label = QLabel("Breite:")
        self.width_input = QLineEdit()
        width_input_layout = QHBoxLayout()
        width_input_layout.addWidget(width_label)
        width_input_layout.addWidget(self.width_input)
        right_layout.addLayout(width_input_layout)

        # Eingabe für Höhe
        height_label = QLabel("Höhe:")
        self.height_input = QLineEdit()
        height_input_layout = QHBoxLayout()
        height_input_layout.addWidget(height_label)
        height_input_layout.addWidget(self.height_input)
        right_layout.addLayout(height_input_layout)

        # Button zum Berechnen des Seitenverhältnisses
        compute_ratio_button = QPushButton("Seitenverhältnis berechnen")
        compute_ratio_button.clicked.connect(self.compute_aspect_ratio)
        right_layout.addWidget(compute_ratio_button)

        # Ausgabe des Seitenverhältnisses
        self.result_ratio_label = QLabel("Seitenverhältnis:")
        self.result_ratio_output = QLineEdit()
        self.result_ratio_output.setReadOnly(True)
        self.result_ratio_output.setStyleSheet("background-color: black; color: white;")
        result_ratio_layout = QHBoxLayout()
        result_ratio_layout.addWidget(self.result_ratio_label)
        result_ratio_layout.addWidget(self.result_ratio_output)
        right_layout.addLayout(result_ratio_layout)

        right_layout.addStretch()

        # Füge die beiden Layouts zum Hauptlayout hinzu
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

    def calculate_other_dimension(self):
        try:
            dimension = float(self.dimension_input.text())
            aspect_ratio = self.ratio_input.text()
            if ':' not in aspect_ratio:
                QMessageBox.warning(self, "Ungültige Eingabe", "Geben Sie ein gültiges Seitenverhältnis ein (z.B. 16:9).")
                return

            width_ratio_str, height_ratio_str = aspect_ratio.split(':')
            width_ratio = float(width_ratio_str)
            height_ratio = float(height_ratio_str)
            ratio = width_ratio / height_ratio

            # Berechne die andere Dimension
            other_dimension = round(dimension / ratio)
            self.result_dimension_output.setText(str(other_dimension))
        except ValueError:
            QMessageBox.warning(self, "Ungültige Eingabe", "Bitte geben Sie gültige Zahlen ein.")

    def compute_aspect_ratio(self):
        try:
            width = int(self.width_input.text())
            height = int(self.height_input.text())

            if width == 0 or height == 0:
                QMessageBox.warning(self, "Ungültige Eingabe", "Breite und Höhe müssen größer als 0 sein.")
                return

            # Größten gemeinsamen Teiler berechnen
            def gcd(a, b):
                while b:
                    a, b = b, a % b
                return a

            divisor = gcd(width, height)
            aspect_width = width // divisor
            aspect_height = height // divisor

            aspect_ratio = f"{aspect_width}:{aspect_height}"
            self.result_ratio_output.setText(aspect_ratio)

        except ValueError:
            QMessageBox.warning(self, "Ungültige Eingabe", "Bitte geben Sie gültige ganze Zahlen für Breite und Höhe ein.")

    def showEvent(self, event):
        super().showEvent(event)
        # Fenster zentrieren
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = AspectRatioCalculator()
    calculator.show()
    sys.exit(app.exec())