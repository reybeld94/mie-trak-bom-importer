import logging
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.logger = logging.getLogger(__name__)

        self.setWindowTitle("Mie Trak BOM Importer")
        self.resize(1100, 700)
        self.setAcceptDrops(True)

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.drop_label = QLabel("Drop Engineering Packing List Excel file here (.xlsx)")
        self.drop_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.drop_label.setStyleSheet(
            "border: 2px dashed gray; padding: 30px; font-size: 16px;"
        )

        self.status_label = QLabel("No file loaded.")

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            [
                "Status",
                "Source Row",
                "Component",
                "Description",
                "Qty",
                "UOM",
                "Message",
            ]
        )

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

        self.logger.info("Main window initialized")

    def dragEnterEvent(self, event) -> None:  # noqa: N802 (Qt override)
        if event.mimeData().hasUrls():
            files = [Path(url.toLocalFile()) for url in event.mimeData().urls()]
            if any(file.suffix.lower() == ".xlsx" for file in files):
                event.acceptProposedAction()
                return
        event.ignore()

    def dropEvent(self, event) -> None:  # noqa: N802 (Qt override)
        files = [Path(url.toLocalFile()) for url in event.mimeData().urls()]
        if not files:
            self.status_label.setText("No file dropped.")
            return

        excel_files = [file for file in files if file.suffix.lower() == ".xlsx"]
        if not excel_files:
            self.status_label.setText("Please drop a .xlsx file.")
            return

        selected_file = excel_files[0]
        self.status_label.setText(f"Loaded file: {selected_file}")
        self.logger.info("File dropped: %s", selected_file)
