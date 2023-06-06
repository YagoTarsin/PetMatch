from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cadastro 📋')
        self.setGeometry(100, 100, 600, 800)
        self.setMinimumSize(600, 800)
        self.setMaximumSize(600, 800)

        icone = QIcon('imagens/icone.png')
        self.setWindowIcon(icone)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 600, 800)
        pixmap = QPixmap('imagens/fundo_cadastro.png')
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

        # Ajusta o tamanho da janela para o tamanho da imagem
        self.resize(pixmap.width(), pixmap.height())

        # Configura a folha de estilo para posicionar a imagem corretamente
        self.setStyleSheet("QMainWindow {background: transparent;}")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()