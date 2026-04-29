from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QHBoxLayout,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mie Trak BOM Importer")
        self.resize(1100, 700)
        self.setAcceptDrops(True)

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.drop_label = QLabel("Drop Engineering Packing List Excel file here")
        self.drop_label.setStyleSheet(
            "border: 2px dashed gray; padding: 30px; font-size: 16px;"
        )

        self.status_label = QLabel("No file loaded.")

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "Status",
            "Source Row",
            "Component",
            "Description",
            "Qty",
            "UOM",
            "Message",
        ])

        button_layout = QHBoxLayout()

        self.load_button = QPushButton("Load File")
        self.validate_button = QPushButton("Validate")
        self.export_button = QPushButton("Export Preview")
        self.import_button = QPushButton("Import BOM")
        self.import_button.setEnabled(False)

        button_layout.addWidget(self.load_button)
        button_layout.addWidget(self.validate_button)
        button_layout.addWidget(self.export_button)
        button_layout.addWidget(self.import_button)

        layout.addWidget(self.drop_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.table)
        layout.addLayout(button_layout)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        if files:
            self.status_label.setText(f"Loaded file: {files[0]}")