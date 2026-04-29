import logging
import sys

from PySide6.QtWidgets import QApplication

from app.ui.main_window import MainWindow


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )


def main() -> None:
    configure_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting Mie Trak BOM Importer")

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
