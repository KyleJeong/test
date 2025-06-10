import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.Qsci import QsciScintilla, QsciLexerPython, QsciLexerCPP, QsciLexerJavaScript

class TestEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QScintilla Test")
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create editor
        self.editor = QsciScintilla()
        layout.addWidget(self.editor)
        
        # Basic editor settings
        self.editor.setMarginWidth(0, 50)  # Line number margin
        self.editor.setMarginLineNumbers(0, True)
        self.editor.setAutoIndent(True)
        self.editor.setIndentationGuides(True)
        self.editor.setTabWidth(4)
        self.editor.setIndentationsUseTabs(False)
        self.editor.setBraceMatching(QsciScintilla.BraceMatch.StrictBraceMatch)
        
        # Test different lexers
        self.test_lexers()
        
        # Load test file if exists
        self.load_test_file()
        
    def test_lexers(self):
        """Test different language lexers"""
        # Python lexer
        python_lexer = QsciLexerPython()
        python_lexer.setDefaultFont(self.editor.font())
        self.editor.setLexer(python_lexer)
        
        # Test code
        test_code = """
def test_function():
    # This is a comment
    x = 10
    y = "Hello, World!"
    if x > 5:
        print(y)
        
class TestClass:
    def __init__(self):
        self.value = 42
        
    def get_value(self):
        return self.value
"""
        self.editor.setText(test_code)
        
    def load_test_file(self):
        """Try to load a test file if it exists"""
        test_file = "test_syntax.py"
        if os.path.exists(test_file):
            try:
                with open(test_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.editor.setText(content)
            except Exception as e:
                print(f"Error loading test file: {e}")

def main():
    app = QApplication(sys.argv)
    window = TestEditor()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 
